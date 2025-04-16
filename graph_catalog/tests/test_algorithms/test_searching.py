import unittest
from itertools import zip_longest
from math import inf

from graph_catalog.algorithms.searching import (
    BFSStates,
    DFSStates,
    bfs,
    bfs_component,
    dfs,
    dfs_component,
)
from graph_catalog.constants import NbrTuple
from graph_catalog.tests.testing_data import SEARCHING_GRAPHS


class TestSearching(unittest.TestCase):

    def setUp(self):
        self.UNDIRECTED = [
            [
                NbrTuple(vertex=1, weights={"index": 0}),
                NbrTuple(vertex=3, weights={"index": 3}),
                NbrTuple(vertex=4, weights={"index": 4}),
                NbrTuple(vertex=5, weights={"index": 6}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
            ],
            [NbrTuple(vertex=1, weights={"index": 1})],
            [
                NbrTuple(vertex=1, weights={"index": 2}),
                NbrTuple(vertex=0, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 4}),
                NbrTuple(vertex=5, weights={"index": 5}),
            ],
            [
                NbrTuple(vertex=4, weights={"index": 5}),
                NbrTuple(vertex=0, weights={"index": 6}),
            ],
        ]

        self.DISCONNECTED = [[], []]

    def test_dfs_component(self):

        UNDIRECTED_RUN = [
            (
                0,
                DFSStates(
                    [None, None, None, None, None, None],
                    [0, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                1,
                DFSStates(
                    [None, 0, None, 0, 0, 0],
                    [0, 1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                2,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                3,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, 3, -1, -1],
                    [-1, -1, 0, -1, -1, -1],
                ),
            ),
            (
                4,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, 3, 4, -1],
                    [-1, 2, 0, 1, -1, -1],
                ),
            ),
            (
                5,
                DFSStates(
                    [None, 0, 1, 1, 0, 4],
                    [0, 1, 2, 3, 4, 5],
                    [-1, 2, 0, 1, -1, -1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            dfs_component(self.UNDIRECTED), UNDIRECTED_RUN
        ):
            self.assertEqual(res, expected_res)

        DISCONNECTED_RUN = [
            (
                0,
                DFSStates(
                    [None, None],
                    [0, -1],
                    [-1, -1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            dfs_component(self.DISCONNECTED), DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)

        START_DISCONNECTED_RUN = [
            (
                1,
                DFSStates(
                    [None, None],
                    [-1, 0],
                    [-1, -1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            dfs_component(self.DISCONNECTED, start_vertex=1), START_DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)

    def test_dfs(self):

        UNDIRECTED_RUN = [
            (
                0,
                DFSStates(
                    [None, None, None, None, None, None],
                    [0, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                1,
                DFSStates(
                    [None, 0, None, 0, 0, 0],
                    [0, 1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                2,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                ),
            ),
            (
                3,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, 3, -1, -1],
                    [-1, -1, 0, -1, -1, -1],
                ),
            ),
            (
                4,
                DFSStates(
                    [None, 0, 1, 1, 0, 0],
                    [0, 1, 2, 3, 4, -1],
                    [-1, 2, 0, 1, -1, -1],
                ),
            ),
            (
                5,
                DFSStates(
                    [None, 0, 1, 1, 0, 4],
                    [0, 1, 2, 3, 4, 5],
                    [-1, 2, 0, 1, -1, -1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(dfs(self.UNDIRECTED), UNDIRECTED_RUN):
            self.assertEqual(res, expected_res)

        DISCONNECTED_RUN = [
            (
                0,
                DFSStates(
                    [None, None],
                    [0, -1],
                    [-1, -1],
                ),
            ),
            (
                1,
                DFSStates(
                    [None, None],
                    [0, 1],
                    [0, -1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(dfs(self.DISCONNECTED), DISCONNECTED_RUN):
            self.assertEqual(res, expected_res)

        START_DISCONNECTED_RUN = [
            (
                1,
                DFSStates(
                    [None, None],
                    [-1, 0],
                    [-1, -1],
                ),
            ),
            (
                0,
                DFSStates(
                    [None, None],
                    [1, 0],
                    [-1, 0],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            dfs(self.DISCONNECTED, start_vertex=1), START_DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)

    def test_bfs_component(self):
        UNDIRECTED_RUN = [
            (
                0,
                BFSStates(
                    [None, None, None, None, None, None],
                    [0, inf, inf, inf, inf, inf],
                ),
            ),
            (
                1,
                BFSStates(
                    [None, 0, None, 0, 0, 0],
                    [0, 1, inf, 1, 1, 1],
                ),
            ),
            (
                3,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                4,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                5,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                2,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            bfs_component(self.UNDIRECTED), UNDIRECTED_RUN
        ):
            self.assertEqual(res, expected_res)

        DISCONNECTED_RUN = [
            (
                0,
                BFSStates(
                    [None, None],
                    [0, inf],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            bfs_component(self.DISCONNECTED), DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)

        START_DISCONNECTED_RUN = [
            (
                1,
                BFSStates(
                    [None, None],
                    [inf, 0],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            bfs_component(self.DISCONNECTED, start_vertex=1), START_DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)

    def test_bfs(self):
        UNDIRECTED_RUN = [
            (
                0,
                BFSStates(
                    [None, None, None, None, None, None],
                    [0, inf, inf, inf, inf, inf],
                ),
            ),
            (
                1,
                BFSStates(
                    [None, 0, None, 0, 0, 0],
                    [0, 1, inf, 1, 1, 1],
                ),
            ),
            (
                3,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                4,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                5,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
            (
                2,
                BFSStates(
                    [None, 0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 1, 1],
                ),
            ),
        ]

        for res, expected_res in zip_longest(bfs(self.UNDIRECTED), UNDIRECTED_RUN):
            self.assertEqual(res, expected_res)

        DISCONNECTED_RUN = [
            (
                0,
                BFSStates(
                    [None, None],
                    [0, inf],
                ),
            ),
            (
                1,
                BFSStates(
                    [None, None],
                    [0, 0],
                ),
            ),
        ]

        for res, expected_res in zip_longest(bfs(self.DISCONNECTED), DISCONNECTED_RUN):
            self.assertEqual(res, expected_res)

        START_DISCONNECTED_RUN = [
            (
                1,
                BFSStates(
                    [None, None],
                    [inf, 0],
                ),
            ),
            (
                0,
                BFSStates(
                    [None, None],
                    [0, 0],
                ),
            ),
        ]

        for res, expected_res in zip_longest(
            bfs(self.DISCONNECTED, start_vertex=1), START_DISCONNECTED_RUN
        ):
            self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
