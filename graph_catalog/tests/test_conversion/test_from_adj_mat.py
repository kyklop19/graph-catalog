import unittest

from conversion.from_adj_mat import (
    AdjMat2AdjList,
    AdjMat2EdgeList,
    AdjMat2Graph,
    AdjMat2IncMat,
)
from testing_data import graphs


class TestFromAdjMat(unittest.TestCase):

    def test_AdjMat2AdjList(self):
        for graph in graphs:
            self.assertEqual(AdjMat2AdjList(graph["AdjMat"]), graph["AdjList"])

    def test_AdjMat2EdgeList(self):
        for graph in graphs:
            self.assertEqual(
                AdjMat2EdgeList(graph["AdjMat"]), graph["EdgeList"], graph["name"]
            )

    def test_AdjMat2Graph(self):
        for graph in graphs:
            self.assertEqual(AdjMat2Graph(graph["AdjMat"]), graph["Graph"])

    def test_AdjMat2IncMat(self):
        for graph in graphs:
            self.assertEqual(AdjMat2IncMat(graph["AdjMat"]), graph["IncMat"])


if __name__ == "__main__":
    unittest.main()
