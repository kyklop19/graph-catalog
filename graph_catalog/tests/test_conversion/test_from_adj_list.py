import unittest

from conversion.from_adj_list import (
    AdjList2AdjMat,
    AdjList2EdgeList,
    AdjList2Graph,
    AdjList2IncMat,
)
from testing_data import graphs


class TestFromAdjList(unittest.TestCase):

    def test_AdjList2AdjMat(self):
        for graph in graphs:
            self.assertEqual(AdjList2AdjMat(graph["AdjList"]), graph["AdjMat"])

    def test_AdjList2EdgeList(self):
        for graph in graphs:
            self.assertEqual(AdjList2EdgeList(graph["AdjList"]), graph["EdgeList"])

    def test_AdjList2Graph(self):
        for graph in graphs:
            self.assertEqual(AdjList2Graph(graph["AdjList"]), graph["Graph"])

    def test_AdjList2IncMat(self):
        for graph in graphs:
            self.assertEqual(AdjList2IncMat(graph["AdjList"]), graph["IncMat"])


if __name__ == "__main__":
    unittest.main()
