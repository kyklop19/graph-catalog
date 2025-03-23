import unittest

from graph_catalog.conversion.from_edge_list import (
    EdgeList2AdjList,
    EdgeList2AdjMat,
    EdgeList2Graph,
    EdgeList2IncMat,
)
from graph_catalog.tests.testing_data import graphs


class TestFromEdgeList(unittest.TestCase):

    def test_EdgeList2AdjList(self):
        for graph in graphs:
            from_rep = graph["EdgeList"]
            to_rep = graph["AdjList"]
            if isinstance(from_rep, Exception):
                continue
            if isinstance(to_rep, Exception):
                with self.assertRaises(to_rep):
                    EdgeList2AdjList(from_rep)
            else:
                self.assertEqual(EdgeList2AdjList(from_rep), to_rep)

    def test_EdgeList2AdjMat(self):
        for graph in graphs:
            from_rep = graph["EdgeList"]
            to_rep = graph["AdjMat"]
            if isinstance(from_rep, Exception):
                continue
            if isinstance(to_rep, Exception):
                with self.assertRaises(to_rep):
                    EdgeList2AdjList(from_rep)
            else:
                self.assertEqual(EdgeList2AdjMat(from_rep), to_rep)

    def test_EdgeList2Graph(self):
        for graph in graphs:
            from_rep = graph["EdgeList"]
            to_rep = graph["Graph"]
            if isinstance(from_rep, Exception):
                continue
            if isinstance(to_rep, Exception):
                with self.assertRaises(to_rep):
                    EdgeList2AdjList(from_rep)
            else:
                self.assertEqual(EdgeList2Graph(from_rep), to_rep)

    def test_EdgeList2IncMat(self):
        for graph in graphs:
            from_rep = graph["EdgeList"]
            to_rep = graph["IncMat"]
            if isinstance(from_rep, Exception):
                continue
            if isinstance(to_rep, Exception):
                with self.assertRaises(to_rep):
                    EdgeList2AdjList(from_rep)
            else:
                self.assertEqual(EdgeList2IncMat(from_rep), to_rep)


if __name__ == "__main__":
    unittest.main()
