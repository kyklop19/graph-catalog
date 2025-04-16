import unittest

from graph_catalog.algorithms.minimum_spanning_tree import find_minimum_spanning_tree
from graph_catalog.constants import EdgeTuple


class TestMinimumSpanningTree(unittest.TestCase):

    def setUp(self):
        self.CYCLE = [
            EdgeTuple(
                start_vertex=0, end_vertex=1, weights={"directed": False, "length": 30}
            ),
            EdgeTuple(
                start_vertex=1, end_vertex=2, weights={"directed": False, "length": 40}
            ),
            EdgeTuple(
                start_vertex=2, end_vertex=3, weights={"directed": False, "length": 60}
            ),
            EdgeTuple(
                start_vertex=0, end_vertex=3, weights={"directed": False, "length": 50}
            ),
        ]

        self.DOUBLE_CYCLE = [
            EdgeTuple(
                start_vertex=0, end_vertex=1, weights={"directed": False, "length": 36}
            ),
            EdgeTuple(
                start_vertex=1, end_vertex=2, weights={"directed": False, "length": 4}
            ),
            EdgeTuple(
                start_vertex=2, end_vertex=3, weights={"directed": False, "length": 62}
            ),
            EdgeTuple(
                start_vertex=3, end_vertex=4, weights={"directed": False, "length": 73}
            ),
            EdgeTuple(
                start_vertex=4, end_vertex=5, weights={"directed": False, "length": 91}
            ),
            EdgeTuple(
                start_vertex=0, end_vertex=5, weights={"directed": False, "length": 45}
            ),
            EdgeTuple(
                start_vertex=3, end_vertex=6, weights={"directed": False, "length": 65}
            ),
            EdgeTuple(
                start_vertex=6, end_vertex=7, weights={"directed": False, "length": 19}
            ),
            EdgeTuple(
                start_vertex=7, end_vertex=8, weights={"directed": False, "length": 10}
            ),
            EdgeTuple(
                start_vertex=8, end_vertex=9, weights={"directed": False, "length": 35}
            ),
            EdgeTuple(
                start_vertex=4, end_vertex=9, weights={"directed": False, "length": 14}
            ),
        ]

    def test_cycle(self):
        print(find_minimum_spanning_tree(self.CYCLE))
        self.assertCountEqual(
            find_minimum_spanning_tree(self.CYCLE),
            [
                EdgeTuple(
                    start_vertex=0,
                    end_vertex=1,
                    weights={"directed": False, "length": 30},
                ),
                EdgeTuple(
                    start_vertex=1,
                    end_vertex=2,
                    weights={"directed": False, "length": 40},
                ),
                EdgeTuple(
                    start_vertex=0,
                    end_vertex=3,
                    weights={"directed": False, "length": 50},
                ),
            ],
        )

    def test_double_cycle(self):
        self.assertCountEqual(
            find_minimum_spanning_tree(self.DOUBLE_CYCLE),
            [
                EdgeTuple(
                    start_vertex=0,
                    end_vertex=1,
                    weights={"directed": False, "length": 36},
                ),
                EdgeTuple(
                    start_vertex=1,
                    end_vertex=2,
                    weights={"directed": False, "length": 4},
                ),
                EdgeTuple(
                    start_vertex=2,
                    end_vertex=3,
                    weights={"directed": False, "length": 62},
                ),
                EdgeTuple(
                    start_vertex=0,
                    end_vertex=5,
                    weights={"directed": False, "length": 45},
                ),
                EdgeTuple(
                    start_vertex=3,
                    end_vertex=6,
                    weights={"directed": False, "length": 65},
                ),
                EdgeTuple(
                    start_vertex=6,
                    end_vertex=7,
                    weights={"directed": False, "length": 19},
                ),
                EdgeTuple(
                    start_vertex=7,
                    end_vertex=8,
                    weights={"directed": False, "length": 10},
                ),
                EdgeTuple(
                    start_vertex=8,
                    end_vertex=9,
                    weights={"directed": False, "length": 35},
                ),
                EdgeTuple(
                    start_vertex=4,
                    end_vertex=9,
                    weights={"directed": False, "length": 14},
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
