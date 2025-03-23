import re
from contextlib import contextmanager
from enum import Enum, auto
from pathlib import Path
from typing import Any, Iterator

import yaml

from graph_catalog.constants import CATALOG_PATH, IncMat, OverwriteError

ANONYMOUS_METADATA_FIELDS = ("name", "number", "description")


class SaveOpts(Enum):
    CREATE_NEW_FILE = auto()
    OVERWRITE_GRAPH = auto()


def _load_from_file(filename: str, key: str) -> dict[str, Any]:
    with open(CATALOG_PATH / "graphs" / f"{filename}.yaml", "r") as graphs_file:
        graphs = yaml.safe_load(graphs_file.read())

    graph = graphs[key]

    return graph


@contextmanager
def _open_catalog_yaml(path: Path, **opts) -> Iterator[dict[str, Any]]:
    with open(path, "r+") as yaml_file:
        data = yaml.safe_load(yaml_file.read())
        yaml_file.seek(0)
        if data is None:
            data = {}
        yield data
        yaml_file.truncate(0)
        yaml_file.write(yaml.safe_dump(data, **opts))


def load_with_name(name: str) -> dict[str, Any]:
    """Loads graph and all of it's metadata using it's name

    Args:
        name (str): Name of the graph

    Raises:
        KeyError: Raises when graph with such name doesn't exist

    Returns:
        dict[str, Any]: Dictionary with graph in `IncMat` representation and all of it's metadata
    """

    with _open_catalog_yaml(CATALOG_PATH / "name_index.yaml") as index:
        if name not in index:
            raise KeyError("Graph with such name doesn't exist")
        else:
            filename = index[name]["filename"]
            key = index[name]["key"]

    graph = _load_from_file(filename, key)

    return graph


def load_with_number(number: str) -> dict[str, Any]:
    """Loads graph and metadata from catalog using graph's number

    To make loading with number anonymous, the function doesn't deletes
    anonymous fields from the metadata before returning.

    Args:
        number (str): Number of the graph in format "<number>.<number>"

    Raises:
        KeyError: Raises when `number` is in a wrong format
        KeyError: Raises when graph with such `number` doesn't exist

    Returns:
        dict[str, Any]: Dictionary with the graph in `IncMat` representation and
        it's metadata except the anonymous fields
    """

    if re.fullmatch(r"\d+\.\d+", number) is None:
        raise KeyError("The number of graph is in a wrong format")

    with _open_catalog_yaml(CATALOG_PATH / "number_index.yaml") as index:
        if number not in index:
            raise KeyError("Graph with such number doesn't exist")
        else:
            filename = index[number]["filename"]
            key = index[number]["key"]

    graph = _load_from_file(filename, key)
    for field in ANONYMOUS_METADATA_FIELDS:
        graph.pop(field, None)

    return graph


def save(
    name: str,
    filename: str,
    graph: IncMat,
    metadata: dict[str, Any] = {},
    opts: SaveOpts | None = None,
) -> str:
    """Save `graph` as `IncMat` to the catalog

    The `graph` is saved under the name of `name` into the file `filename.yaml`.

    `metadata` are saved with graph into `filename.yaml`

    `number` of the graph is generated and returned.

    By default graph can't be overwritten resp. can't be written into
    nonexisting file. By setting `opts` to `SaveOpts.OVERWRITE_GRAPH` resp.
    `SaveOpts.CREATE_NEW_FILE` this behavior can be turned off.

    Args:
        name (str): Name of the graph
        filename (str): Name of the file where graph is saved (without the extension)
        graph (IncMat): Graph as `IncMat`
        metadata (dict[str, Any], optional): Dictionary with field names as keys and any data as values. Defaults to {}.
        opts (SaveOpts, optional): Options to either allow overwriting a graph or creating new graph file. Defaults to None.

    Raises:
        FileNotFoundError: Raises if `filename.yaml` doesn't exists unless
            `SaveOpts.CREATE_NEW_FILE` is set as option
        OverwriteError: Raises if `name` graph already exists unless `SaveOpts.OVERWRITE_GRAPH` is set as
            option

    Returns:
        str: The `number` of the graph automatically generated based of `filename.yaml` and number of already saved files in it
    """
    GRAPHS_PATH = CATALOG_PATH / "graphs" / f"{filename}.yaml"

    create_new_file = False
    if not GRAPHS_PATH.exists():
        if SaveOpts.CREATE_NEW_FILE is not opts:
            raise FileNotFoundError(f'Graph file "{filename}" doesn\'t exist.')
        else:
            create_new_file = True

    if create_new_file:
        with open(GRAPHS_PATH, "w") as graph_file:
            graph_file.write(yaml.safe_dump({}))

    with _open_catalog_yaml(CATALOG_PATH / "graphs_files_index.yaml") as records:
        if create_new_file:
            records[filename] = len(records)
        file_number = records[filename]

    overwriting = False
    with _open_catalog_yaml(CATALOG_PATH / "name_index.yaml") as records:
        if name in records:
            if SaveOpts.OVERWRITE_GRAPH is not opts:
                raise OverwriteError(
                    "Can't overwrite already existing graph unless explicitly enabling overwrite option"
                )
            else:
                key = records[name]["key"]
                overwriting = True

    with _open_catalog_yaml(
        GRAPHS_PATH, default_flow_style=None, sort_keys=False
    ) as graphs:
        if not overwriting:
            num_of_graphs = len(graphs)
            number = f"{file_number}.{num_of_graphs}"

            key = number + name.replace(" ", "_")
        else:
            number = graphs[key]["number"]

        record = metadata | {
            "name": name,
            "number": number,
            "graph": graph,
        }

        graphs[key] = record

    with _open_catalog_yaml(CATALOG_PATH / "name_index.yaml") as records:
        records[name] = {"filename": filename, "key": key}

    with _open_catalog_yaml(CATALOG_PATH / "number_index.yaml") as records:
        records[number] = {"filename": filename, "key": key}

    return number
