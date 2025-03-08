import unittest

from algorithms.bipartite import is_bipartite
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


class TestBipartite(unittest.TestCase):

    def test_is_bipartite(self):
        self.assertTrue(is_bipartite(EMPTY_GRAPH))
        self.assertTrue(is_bipartite(UNDIRECTED_GRAPH))

        PATH = [
            [NbrTuple(vertex=1, weights={"index": 0})],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
            ],
            [NbrTuple(vertex=2, weights={"index": 2})],
        ]
        self.assertTrue(is_bipartite(PATH))

        EVEN_CYCLE = [
            [
                NbrTuple(vertex=1, weights={"index": 0}),
                NbrTuple(vertex=3, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 2}),
                NbrTuple(vertex=0, weights={"index": 3}),
            ],
        ]

        self.assertTrue(is_bipartite(EVEN_CYCLE))

        ODD_CYCLE = [
            [
                NbrTuple(vertex=1, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=0, weights={"index": 2}),
            ],
        ]

        self.assertFalse(is_bipartite(ODD_CYCLE))

        MULTIPLE_BIPARTITE_COMPONENTS = [
            [],
            [NbrTuple(vertex=2, weights={"index": 0})],
            [NbrTuple(vertex=1, weights={"index": 0})],
            [
                NbrTuple(vertex=4, weights={"index": 1}),
                NbrTuple(vertex=6, weights={"index": 4}),
            ],
            [
                NbrTuple(vertex=3, weights={"index": 1}),
                NbrTuple(vertex=5, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=4, weights={"index": 2}),
                NbrTuple(vertex=6, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=5, weights={"index": 3}),
                NbrTuple(vertex=3, weights={"index": 4}),
            ],
        ]
        self.assertTrue(is_bipartite(MULTIPLE_BIPARTITE_COMPONENTS))

        MULTIPLE_NOT_ALL_BIPARTITE_COMPONENTS = [
            [NbrTuple(vertex=1, weights={"index": 0})],
            [NbrTuple(vertex=0, weights={"index": 0})],
            [
                NbrTuple(vertex=3, weights={"index": 1}),
                NbrTuple(vertex=5, weights={"index": 4}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 1}),
                NbrTuple(vertex=4, weights={"index": 2}),
            ],
            [
                NbrTuple(vertex=3, weights={"index": 2}),
                NbrTuple(vertex=5, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=4, weights={"index": 3}),
                NbrTuple(vertex=2, weights={"index": 4}),
            ],
            [
                NbrTuple(vertex=7, weights={"index": 5}),
                NbrTuple(vertex=8, weights={"index": 7}),
            ],
            [
                NbrTuple(vertex=6, weights={"index": 5}),
                NbrTuple(vertex=8, weights={"index": 6}),
            ],
            [
                NbrTuple(vertex=7, weights={"index": 6}),
                NbrTuple(vertex=6, weights={"index": 7}),
            ],
        ]

        self.assertFalse(is_bipartite(MULTIPLE_NOT_ALL_BIPARTITE_COMPONENTS))

        DOUBLE_CYCLE = [
            [
                NbrTuple(vertex=1, weights={"index": 0}),
                NbrTuple(vertex=3, weights={"index": 3}),
            ],
            [
                NbrTuple(vertex=0, weights={"index": 0}),
                NbrTuple(vertex=2, weights={"index": 1}),
            ],
            [
                NbrTuple(vertex=1, weights={"index": 1}),
                NbrTuple(vertex=3, weights={"index": 2}),
                NbrTuple(vertex=4, weights={"index": 4}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 2}),
                NbrTuple(vertex=0, weights={"index": 3}),
                NbrTuple(vertex=4, weights={"index": 5}),
            ],
            [
                NbrTuple(vertex=2, weights={"index": 4}),
                NbrTuple(vertex=3, weights={"index": 5}),
            ],
        ]

        self.assertFalse(is_bipartite(DOUBLE_CYCLE))


if __name__ == "__main__":
    unittest.main()
