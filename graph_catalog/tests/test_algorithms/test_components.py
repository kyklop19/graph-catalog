import unittest

from algorithms.components import divide_into_components, get_num_of_components
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


class TestComponents(unittest.TestCase):

    def test_get_num_of_components(self):
        self.assertEqual(get_num_of_components(EMPTY_GRAPH), 6)

        self.assertEqual(
            get_num_of_components(UNDIRECTED_GRAPH),
            3,
        )

    def test_divide_into_components(self):
        self.assertEqual(divide_into_components(EMPTY_GRAPH), [0, 1, 2, 3, 4, 5])

        self.assertEqual(
            divide_into_components(UNDIRECTED_GRAPH),
            [0, 1, 2, 2, 2, 0],
        )


if __name__ == "__main__":
    unittest.main()
