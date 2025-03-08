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

    filename, key = index[id]

    with open(CATALOG_PATH / "graphs" / "{filename}.yaml", "r") as graphs_file:
        graphs = yaml.safe_load(graphs_file.read())

    graph = graphs[key]

    # with open(CATALOG_PATH / "catalog.yaml", "r") as catalog:
    #     data = yaml.safe_load(catalog.read())

    # res = None
    # for record in data:
    #     if record["name"] == id:
    #         res = record
    #         break

    return graph


def save(ids: tuple[str, str], graphs_name: str, graph: IncMat):

    record = {
        "name": ids,
        "graph": graph,
    }

    # with open(CATALOG_PATH / "catalog.yaml", "r+") as catalog:
    #     data = yaml.safe_load(catalog.read())
    #     if data is None:
    #         data = []
    #     data.append(record)
    #     catalog.write(yaml.safe_dump(data, default_flow_style=None, sort_keys=False))
    key = "test"

    with open(CATALOG_PATH / "name_index.yaml", "r+") as index:
        data = yaml.safe_load(index.read())
        index.seek(0)
        # if data is None:
        #     data = []
        data[ids[0]] = {"filename": graphs_name, "key": key}
        index.write(yaml.safe_dump(data))

    with open(CATALOG_PATH / "graphs" / f"{graphs_name}.yaml", "r+") as graphs_file:
        graphs = yaml.safe_load(graphs_file.read())
        graphs_file.seek(0)
        # if graphs is None:
        #     graphs = []
        graphs[key] = record
        graphs_file.write(yaml.safe_dump(graphs))


# save("test", [[1, 2], [3, 4]])
# print(load("test2"))
# save(("PATH", 123), "cycles", [[]])
