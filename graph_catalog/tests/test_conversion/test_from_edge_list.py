import unittest

from conversion.from_edge_list import (
    EdgeList2AdjList,
    EdgeList2AdjMat,
    EdgeList2Graph,
    EdgeList2IncMat,
)
from testing_data import graphs


class TestFromEdgeList(unittest.TestCase):

    def test_EdgeList2AdjList(self):
        for graph in graphs:
            self.assertEqual(EdgeList2AdjList(graph["EdgeList"]), graph["AdjList"])

    def test_EdgeList2AdjMat(self):
        for graph in graphs:
            self.assertEqual(EdgeList2AdjMat(graph["EdgeList"]), graph["AdjMat"])

    def test_EdgeList2Graph(self):
        for graph in graphs:
            self.assertEqual(EdgeList2Graph(graph["EdgeList"]), graph["Graph"])

    def test_EdgeList2IncMat(self):
        for graph in graphs:
            self.assertEqual(EdgeList2IncMat(graph["EdgeList"]), graph["IncMat"])


if __name__ == "__main__":
    unittest.main()
