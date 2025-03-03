import unittest

from algorithms.bipartite import is_bipartite
from constants import NbrTuple

EMPTY_GRAPH = [[], [], [], [], [], []]

UNDIRECTED_GRAPH = [
    [NbrTuple(vertex=5, weights={"index": 0})],
    [],
    [NbrTuple(vertex=4, weights={"index": 2})],
    [NbrTuple(vertex=4, weights={"index": 1})],
    [
        NbrTuple(vertex=3, weights={"index": 1}),
        NbrTuple(vertex=2, weights={"index": 2}),
    ],
    [NbrTuple(vertex=0, weights={"index": 0})],
]


class TestBipartite(unittest.TestCase):

    def test_is_bipartite(self):
        self.assertTrue(is_bipartite(EMPTY_GRAPH))
        self.assertTrue(is_bipartite(UNDIRECTED_GRAPH))


if __name__ == "__main__":
    unittest.main()
