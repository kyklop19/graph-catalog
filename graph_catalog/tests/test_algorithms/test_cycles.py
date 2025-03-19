import unittest

from algorithms.cycles import has_cycle
from constants import NbrTuple
from testing_data import BACK_EDGE, CROSS_EDGE, FORWARD_EDGE

EMPTY = [[], [], [], [], [], [], []]

LOOP = [[NbrTuple(vertex=0, weights={"index": 0})]]
DIRECTED_PATH = [
    [NbrTuple(1, {"index": 0})],
    [NbrTuple(2, {"index": 1})],
    [NbrTuple(3, {"index": 2})],
    [NbrTuple(4, {"index": 3})],
    [],
]


class TestCycles(unittest.TestCase):

    def test_has_cycle(self):
        self.assertFalse(has_cycle(EMPTY))
        self.assertTrue(has_cycle(LOOP))
        self.assertFalse(has_cycle(DIRECTED_PATH))

        self.assertTrue(has_cycle(BACK_EDGE))
        self.assertFalse(has_cycle(CROSS_EDGE))
        self.assertFalse(has_cycle(FORWARD_EDGE))


if __name__ == "__main__":
    unittest.main()
