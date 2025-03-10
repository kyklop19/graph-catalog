from pathlib import Path
from typing import Any

import yaml
from constants import CATALOG_PATH, IncMat


def load(id: str):
    """test

    Args:
        name (str): test
    """

    index_name = "name_index"

    with open(CATALOG_PATH / f"{index_name}.yaml", "r") as index_file:
        index = yaml.safe_load(index_file.read())

    filename = index[id]["filename"]
    key = index[id]["key"]

    with open(CATALOG_PATH / "graphs" / f"{filename}.yaml", "r") as graphs_file:
        graphs = yaml.safe_load(graphs_file.read())

    graph = graphs[key]
    del graph["name"]
    del graph["number"]

    # with open(CATALOG_PATH / "catalog.yaml", "r") as catalog:
    #     data = yaml.safe_load(catalog.read())

    # res = None
    # for record in data:
    #     if record["name"] == id:
    #         res = record
    #         break

    return graph


# def add_to_yaml(path: Path, record: dict[str, Any]):
#     with open(path, "r+") as f:
#         data = yaml.safe_load(f.read())
#         f.seek(0)
#         # if data is None:
#         #     data = []
#         data[ids[0]] = {"filename": filename, "key": key}
#         index.write(yaml.safe_dump(data))


def save(
    ids: tuple[str, str], filename: str, graph: IncMat, metadata: dict[str, Any] = {}
):

    record = metadata | {
        "name": ids[0],
        "number": ids[1],
        "graph": graph,
    }

    # with open(CATALOG_PATH / "catalog.yaml", "r+") as catalog:
    #     data = yaml.safe_load(catalog.read())
    #     if data is None:
    #         data = []
    #     data.append(record)
    #     catalog.write(yaml.safe_dump(data, default_flow_style=None, sort_keys=False))
    key = str(ids[1]) + ids[0]

    with open(CATALOG_PATH / "name_index.yaml", "r+") as index:
        data = yaml.safe_load(index.read())
        index.seek(0)
        if data is None:
            data = {}
        data[ids[0]] = {"filename": filename, "key": key}
        index.write(yaml.safe_dump(data))

    GRAPHS_PATH = CATALOG_PATH / "graphs" / f"{filename}.yaml"

    if not GRAPHS_PATH.exists():
        raise FileNotFoundError(f'Graph file "{filename}" doesn\'t exist.')

    with open(GRAPHS_PATH, "r+") as graphs_file:
        graphs = yaml.safe_load(graphs_file.read())
        graphs_file.seek(0)
        if graphs is None:
            graphs = {}
        graphs[key] = record
        graphs_file.write(yaml.safe_dump(graphs))


# save("test", [[1, 2], [3, 4]])
# print(load("test2"))
# save(("PATH", 123), "cycles", [[]])
# print(load("PATH"))
