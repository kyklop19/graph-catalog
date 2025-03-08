import unittest

from algorithms.topological_ordering import find_topological_ordering
from constants import NbrTuple

EMPTY = [[], [], [], [], [], []]

PATH = [
    [NbrTuple(vertex=1, weights={"index": 0})],
    [NbrTuple(vertex=2, weights={"index": 1})],
    [NbrTuple(vertex=3, weights={"index": 2})],
    [],
]


class TestTopologicalOrdering(unittest.TestCase):

    def test_find_topological_ordering(self):
        self.assertEqual(find_topological_ordering(EMPTY), [0, 1, 2, 3, 4, 5])
        self.assertEqual(find_topological_ordering(PATH), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
