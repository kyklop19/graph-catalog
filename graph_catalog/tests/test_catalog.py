import unittest
from textwrap import dedent

from pyfakefs.fake_filesystem_unittest import TestCase

from graph_catalog.catalog import SaveOpts, load_with_name, load_with_number, save
from graph_catalog.constants import CATALOG_PATH, OverwriteError


class TestCatalog(TestCase):

    def setUp(self):
        self.setUpPyfakefs()
        self.fs.create_file(
            CATALOG_PATH / "graphs_files_index.yaml",
            contents=dedent(
                """\
            test_category: 0
            test_category2: 1
            """
            ),
        )
        self.fs.create_file(
            CATALOG_PATH / "name_index.yaml",
            contents=dedent(
                """\
            test_name1:
              filename: test_category
              key: 0.0test_name1
            test_name2:
              filename: test_category
              key: 0.1test_name2
            test_name3:
              filename: test_category2
              key: 1.0test_name3
            """
            ),
        )
        self.fs.create_file(
            CATALOG_PATH / "number_index.yaml",
            contents=dedent(
                """\
            '0.0':
              filename: test_category
              key: 0.0test_name1
            '0.1':
              filename: test_category
              key: 0.1test_name2
            '1.0':
              filename: test_category2
              key: 1.0test_name3
            """
            ),
        )
        self.fs.create_file(
            CATALOG_PATH / "graphs" / "test_category.yaml",
            contents=dedent(
                """\
            0.0test_name1:
              name: test_name1
              number: '0.0'
              graph:
              - [1, 2]
              - [1, 0]
            0.1test_name2:
              name: test_name2
              number: '0.1'
              graph:
              - [1, 1, 0]
              - [-1, 1, 2]
              description: |
                Cupidatat in anim
                adipisicing eu et minim nostrud
                aliqua dolore dolor occaecat.
                Exercitation consequat culpa nisi
                duis mollit dolore ex voluptate.
                Elit minim reprehenderit officia
                ex aliquip adipisicing et.
                Deserunt do est velit quis tempor
                exercitation deserunt elit eu
                excepteur eiusmod esse non. Mollit
                occaecat incididunt est ex officia
                ipsum veniam in eiusmod incididunt velit.
            """
            ),
        )
        self.fs.create_file(
            CATALOG_PATH / "graphs" / "test_category2.yaml",
            contents=dedent(
                """\
            1.0test_name3:
              name: test_name3
              number: '1.0'
              graph:
              - [1, 0]
              - [0, -1]
              - [1, 1]
            """
            ),
        )

    def test_load_with_name(self):

        self.assertEqual(
            load_with_name("test_name1"),
            {
                "name": "test_name1",
                "number": "0.0",
                "graph": [
                    [1, 2],
                    [1, 0],
                ],
            },
        )
        self.assertEqual(
            load_with_name("test_name2"),
            {
                "name": "test_name2",
                "number": "0.1",
                "graph": [
                    [1, 1, 0],
                    [-1, 1, 2],
                ],
                "description": dedent(
                    """\
                Cupidatat in anim
                adipisicing eu et minim nostrud
                aliqua dolore dolor occaecat.
                Exercitation consequat culpa nisi
                duis mollit dolore ex voluptate.
                Elit minim reprehenderit officia
                ex aliquip adipisicing et.
                Deserunt do est velit quis tempor
                exercitation deserunt elit eu
                excepteur eiusmod esse non. Mollit
                occaecat incididunt est ex officia
                ipsum veniam in eiusmod incididunt velit.
                """
                ),
            },
        )
        self.assertEqual(
            load_with_name("test_name3"),
            {
                "name": "test_name3",
                "number": "1.0",
                "graph": [
                    [1, 0],
                    [0, -1],
                    [1, 1],
                ],
            },
        )

        with self.assertRaisesRegex(KeyError, "Graph with such name doesn't exist"):
            load_with_name("test_name_error")

    def test_load_with_number(self):
        self.assertEqual(
            load_with_number("0.0"),
            {
                "graph": [
                    [1, 2],
                    [1, 0],
                ],
            },
        )
        self.assertEqual(
            load_with_number("0.1"),
            {
                "graph": [
                    [1, 1, 0],
                    [-1, 1, 2],
                ],
            },
        )
        self.assertEqual(
            load_with_number("1.0"),
            {
                "graph": [
                    [1, 0],
                    [0, -1],
                    [1, 1],
                ],
            },
        )

        with self.assertRaisesRegex(
            KeyError, "The number of graph is in a wrong format"
        ):
            load_with_number("25")
        with self.assertRaisesRegex(KeyError, "Graph with such number doesn't exist"):
            load_with_number("0.2")

    def test_save_non_existing(self):
        save("new_test_name", "test_category2", [[4, 3], [2, 1]])
        with open(CATALOG_PATH / "graphs" / "test_category2.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            1.0test_name3:
              name: test_name3
              number: '1.0'
              graph:
              - [1, 0]
              - [0, -1]
              - [1, 1]
            1.1new_test_name:
              name: new_test_name
              number: '1.1'
              graph:
              - [4, 3]
              - [2, 1]
            """
                ),
            )
        with open(CATALOG_PATH / "name_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            new_test_name:
              filename: test_category2
              key: 1.1new_test_name
            test_name1:
              filename: test_category
              key: 0.0test_name1
            test_name2:
              filename: test_category
              key: 0.1test_name2
            test_name3:
              filename: test_category2
              key: 1.0test_name3
            """
                ),
            )
        with open(CATALOG_PATH / "number_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            '0.0':
              filename: test_category
              key: 0.0test_name1
            '0.1':
              filename: test_category
              key: 0.1test_name2
            '1.0':
              filename: test_category2
              key: 1.0test_name3
            '1.1':
              filename: test_category2
              key: 1.1new_test_name
            """
                ),
            )

    def test_save_existing_name(self):
        with self.assertRaisesRegex(
            OverwriteError,
            "Can't overwrite already existing graph unless explicitly enabling overwrite option",
        ):
            save("test_name3", "test_category2", [[4, 3], [2, 1]])

    def test_save_non_existing_file(self):
        with self.assertRaisesRegex(
            FileNotFoundError, f'Graph file "test_category3" doesn\'t exist.'
        ):
            save("new_test_name", "test_category3", [[4, 3], [2, 1]])

    def test_save_create_new_file(self):
        save(
            "new_test_name",
            "test_category3",
            [[4, 3], [2, 1]],
            opts=SaveOpts.CREATE_NEW_FILE,
        )
        with open(CATALOG_PATH / "graphs" / "test_category3.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            2.0new_test_name:
              name: new_test_name
              number: '2.0'
              graph:
              - [4, 3]
              - [2, 1]
            """
                ),
            )
        with open(CATALOG_PATH / "name_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            new_test_name:
              filename: test_category3
              key: 2.0new_test_name
            test_name1:
              filename: test_category
              key: 0.0test_name1
            test_name2:
              filename: test_category
              key: 0.1test_name2
            test_name3:
              filename: test_category2
              key: 1.0test_name3
            """
                ),
            )
        with open(CATALOG_PATH / "number_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            '0.0':
              filename: test_category
              key: 0.0test_name1
            '0.1':
              filename: test_category
              key: 0.1test_name2
            '1.0':
              filename: test_category2
              key: 1.0test_name3
            '2.0':
              filename: test_category3
              key: 2.0new_test_name
            """
                ),
            )
        with open(CATALOG_PATH / "graphs_files_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            test_category: 0
            test_category2: 1
            test_category3: 2
            """
                ),
            )

    def test_save_overwrite_existing(self):
        save(
            "test_name3",
            "test_category2",
            [[4, 3], [2, 1]],
            opts=SaveOpts.OVERWRITE_GRAPH,
        )
        with open(CATALOG_PATH / "graphs" / "test_category2.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            1.0test_name3:
              name: test_name3
              number: '1.0'
              graph:
              - [4, 3]
              - [2, 1]
            """
                ),
            )
        with open(CATALOG_PATH / "name_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            test_name1:
              filename: test_category
              key: 0.0test_name1
            test_name2:
              filename: test_category
              key: 0.1test_name2
            test_name3:
              filename: test_category2
              key: 1.0test_name3
            """
                ),
            )
        with open(CATALOG_PATH / "number_index.yaml", "r") as f:
            self.assertEqual(
                f.read(),
                dedent(
                    """\
            '0.0':
              filename: test_category
              key: 0.0test_name1
            '0.1':
              filename: test_category
              key: 0.1test_name2
            '1.0':
              filename: test_category2
              key: 1.0test_name3
            """
                ),
            )


if __name__ == "__main__":
    unittest.main()
