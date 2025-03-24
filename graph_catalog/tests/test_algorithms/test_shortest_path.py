import unittest

from graph_catalog.algorithms.shortest_path import (
    find_shortest_path,
    find_shortest_path_weighted,
)
from graph_catalog.constants import NbrTuple


class TestFindShortestPath(unittest.TestCase):

    def setUp(self):
        self.PATH = [
            [NbrTuple(vertex=1, weights={"index": 0})],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 2}),
                NbrTuple(vertex=4, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=3, weights={"index": 3}),
                NbrTuple(vertex=5, weights={"index": 4}),
            ],
            [NbrTuple(vertex=4, weights={"index": 4})],
        ]

        self.CYCLE = [
            [
                NbrTuple(vertex=1, weights={"index": 0}),
                NbrTuple(vertex=6, weights={"index": 6}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 2}),
                NbrTuple(vertex=4, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=3, weights={"index": 3}),
                NbrTuple(vertex=5, weights={"index": 4}),
            ],
            [
                NbrTuple(vertex=4, weights={"index": 4}),
                NbrTuple(vertex=6, weights={"index": 5}),
            ],
            [
                NbrTuple(vertex=5, weights={"index": 5}),
                NbrTuple(vertex=0, weights={"index": 6}),
            ],
        ]

        self.DIRECTED_CYCLE = [
            [NbrTuple(vertex=1, weights={"index": 0})],
            [NbrTuple(vertex=2, weights={"index": 1})],
            [NbrTuple(vertex=3, weights={"index": 2})],
            [NbrTuple(vertex=4, weights={"index": 3})],
            [NbrTuple(vertex=0, weights={"index": 4})],
        ]

    def test_path(self):
        self.assertEqual(find_shortest_path(self.PATH, 0, 5), [0, 1, 2, 3, 4, 5])

    def test_path_part(self):
        self.assertEqual(find_shortest_path(self.PATH, 0, 4), [0, 1, 2, 3, 4])

    def test_not_on_path(self):
        self.assertIsNone(find_shortest_path(self.PATH, 0, 6))

    def test_cycle(self):
        self.assertEqual(find_shortest_path(self.CYCLE, 0, 4), [0, 6, 5, 4])

    def test_directed_cycle(self):
        self.assertEqual(find_shortest_path(self.DIRECTED_CYCLE, 0, 4), [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
