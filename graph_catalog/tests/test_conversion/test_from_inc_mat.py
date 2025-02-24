import unittest

from conversion.from_inc_mat import (
    IncMat2AdjList,
    IncMat2AdjMat,
    IncMat2EdgeList,
    IncMat2Graph,
)
from testing_data import graphs


class TestFromIncMat(unittest.TestCase):

    def test_IncMat2AdjList(self):
        for graph in graphs:
            self.assertEqual(IncMat2AdjList(graph["IncMat"]), graph["AdjList"])

    def test_IncMat2AdjMat(self):
        for graph in graphs:
            self.assertEqual(IncMat2AdjMat(graph["IncMat"]), graph["AdjMat"])

    def test_IncMat2Graph(self):
        for graph in graphs:
            self.assertEqual(IncMat2Graph(graph["IncMat"]), graph["Graph"])

    def test_IncMat2EdgeList(self):
        for graph in graphs:
            self.assertEqual(IncMat2EdgeList(graph["IncMat"]), graph["EdgeList"])


if __name__ == "__main__":
    unittest.main()
