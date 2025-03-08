import unittest

from algorithms.cycles import check_for_cycle_directed, check_for_cycle_undirected
from constants import NbrTuple

EMPTY = [[], [], [], [], [], [], []]

LOOP = [[NbrTuple(vertex=0, weights={"index": 0})]]


class TestCycles(unittest.TestCase):

    def test_check_for_cycle_undirected(self):
        self.assertFalse(check_for_cycle_undirected(EMPTY))
        self.assertTrue(check_for_cycle_undirected(LOOP))

    def test_check_for_cycle_check_for_cycle_directed(self):
        self.assertFalse(check_for_cycle_directed(EMPTY))
        self.assertTrue(check_for_cycle_directed(LOOP))


if __name__ == "__main__":
    unittest.main()
