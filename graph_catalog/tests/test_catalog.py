import unittest
from unittest.mock import call, mock_open, patch

from catalog import load, save
from constants import CATALOG_PATH

DATA = """\
- name: test
  graph:
  - [1, 2]
  - [3, 4]
"""


class TestCatalog(unittest.TestCase):

    def test_load(self):
        m = mock_open(read_data=DATA)
        with patch("builtins.open", m):
            graph = load("test")

        m.assert_called_once_with(CATALOG_PATH / "catalog.yaml", "r")
        self.assertEqual(graph, [[1, 2], [3, 4]])

    def test_save(self):
        with patch("builtins.open", mock_open(read_data=DATA)) as m:
            save("name", [])

        m.assert_has_calls(
            [
                call(CATALOG_PATH / "catalog.yaml", "r+"),
                call().__enter__(),
                call().__enter__().read(),
                call().__enter__().write(""),
                call().__exit__(None, None, None),
            ]
        )


if __name__ == "__main__":
    unittest.main()
