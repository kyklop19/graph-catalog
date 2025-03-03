import unittest

from algorithms.searching import DFSStates, dfs, dfs_component
from constants import NbrTuple
from testing_data import SEARCHING_GRAPHS


class TestSearching(unittest.TestCase):

    def test_dfs_component(self):
        UNDIRECTED = [
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

        RUN = [
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

        for res, expected_res in zip(dfs_component(UNDIRECTED), RUN):
            self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
