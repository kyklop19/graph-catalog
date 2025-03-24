import unittest

from graph_catalog.conversion.from_graph import (
    Graph2AdjList,
    Graph2AdjMat,
    Graph2EdgeList,
    Graph2IncMat,
)
from graph_catalog.tests.testing_data import graphs


class TestFromIncMat(unittest.TestCase):

    def test_IncMat2AdjList(self):
        for graph in graphs:
            self.assertEqual(Graph2AdjList(graph["Graph"]), graph["AdjList"])

    def test_Graph2AdjMat(self):
        for graph in graphs:
            self.assertEqual(Graph2AdjMat(graph["Graph"]), graph["AdjMat"])

    def test_Graph2IncMat(self):
        for graph in graphs:
            self.assertEqual(Graph2IncMat(graph["Graph"]), graph["IncMat"])

    def test_Graph2EdgeList(self):
        for graph in graphs:
            self.assertEqual(Graph2EdgeList(graph["Graph"]), graph["EdgeList"])


if __name__ == "__main__":
    unittest.main()
