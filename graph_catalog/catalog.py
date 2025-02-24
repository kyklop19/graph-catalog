import yaml
from constants import CATALOG_PATH, IncMat


def load(name: str):
    """test

    Args:
        name (str): test
    """

    with open(CATALOG_PATH / "catalog.yaml", "r") as catalog:
        data = yaml.safe_load(catalog.read())

    res = None
    for record in data:
        if record["name"] == name:
            res = record
            break

    return res


def save(name: str, graph: IncMat):

    record = {
        "name": name,
        "graph": graph,
    }

    with open(CATALOG_PATH / "catalog.yaml", "r+") as catalog:
        data = yaml.safe_load(catalog.read())
        if data is None:
            data = []
        data.append(record)
        catalog.write(yaml.safe_dump(data, default_flow_style=None, sort_keys=False))


# save("test", [[1, 2], [3, 4]])
# print(load("test2"))
