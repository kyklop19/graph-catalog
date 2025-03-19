from constants import ConversionError, EdgeTuple, NbrTuple
from graph import Edge, Graph, Vertex

SEARCHING_GRAPHS = [[[], [], [], [], [], [], [], [], [], [], []]]

BACK_EDGE = [
    [NbrTuple(vertex=1, weights={"index": 0})],
    [NbrTuple(vertex=2, weights={"index": 1})],
    [NbrTuple(vertex=3, weights={"index": 2})],
    [NbrTuple(vertex=0, weights={"index": 3})],
]

CROSS_EDGE = [
    [
        NbrTuple(vertex=1, weights={"index": 0}),
        NbrTuple(vertex=3, weights={"index": 2}),
    ],
    [NbrTuple(vertex=2, weights={"index": 1})],
    [],
    [NbrTuple(vertex=2, weights={"index": 3})],
]

FORWARD_EDGE = [
    [
        NbrTuple(vertex=1, weights={"index": 0}),
        NbrTuple(vertex=3, weights={"index": 3}),
    ],
    [NbrTuple(vertex=2, weights={"index": 1})],
    [NbrTuple(vertex=3, weights={"index": 2})],
    [],
]

UNDIRECTED = Graph()

for __ in range(3):
    UNDIRECTED.add_vertex()

UNDIRECTED.add_undirected_edge(0, 1)
UNDIRECTED.add_undirected_edge(0, 2)
UNDIRECTED.add_undirected_edge(1, 2)

DIRECTED = Graph()

for __ in range(3):
    DIRECTED.add_vertex()

DIRECTED.add_directed_edge(0, 1)
DIRECTED.add_directed_edge(0, 2)
DIRECTED.add_directed_edge(1, 2)

MIXED = Graph()

for __ in range(4):
    MIXED.add_vertex()

MIXED.add_undirected_edge(0, 1)
MIXED.add_undirected_edge(0, 2)
MIXED.add_directed_edge(1, 2)
MIXED.add_directed_edge(2, 3)

LOOP = Graph()


for __ in range(3):
    LOOP.add_vertex()

LOOP.add_undirected_edge(0, 1)
LOOP.add_undirected_edge(0, 2)
LOOP.add_loop(2)

graphs = [
    # {
    #     "EdgeList": [],
    #     "AdjList": [[], [], []],
    #     "AdjMat": [],
    #     "IncMat": [],
    #     "Graph": Graph([]),
    # },
    # Empty
    # {
    #     "EdgeList": ConversionError,
    #     "AdjList": [[], [], []],
    #     "AdjMat": [
    #         [0, 0, 0],
    #         [0, 0, 0],
    #         [0, 0, 0],
    #     ],
    #     "IncMat": [[], [], []],
    #     "Graph": Graph(
    #         [
    #             Vertex(0),
    #             Vertex(1),
    #             Vertex(2),
    #         ]
    #     ),
    # },
    {
        "name": "Undirected",
        "EdgeList": [
            EdgeTuple(0, 1, {"directed": False}),
            EdgeTuple(0, 2, {"directed": False}),
            EdgeTuple(1, 2, {"directed": False}),
        ],
        "AdjList": [
            [NbrTuple(1, {"index": 0}), NbrTuple(2, {"index": 1})],
            [NbrTuple(0, {"index": 0}), NbrTuple(2, {"index": 2})],
            [NbrTuple(0, {"index": 1}), NbrTuple(1, {"index": 2})],
        ],
        "AdjMat": [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ],
        "IncMat": [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1],
        ],
        "Graph": UNDIRECTED,
    },
    {
        "name": "Directed",
        "EdgeList": [
            EdgeTuple(0, 1, {"directed": True}),
            EdgeTuple(0, 2, {"directed": True}),
            EdgeTuple(1, 2, {"directed": True}),
        ],
        "AdjList": [
            [NbrTuple(1, {"index": 0}), NbrTuple(2, {"index": 1})],
            [NbrTuple(2, {"index": 2})],
            [],
        ],
        "AdjMat": [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
        ],
        "IncMat": [
            [1, 1, 0],
            [-1, 0, 1],
            [0, -1, -1],
        ],
        "Graph": DIRECTED,
    },
    {
        "name": "Mixed",
        "EdgeList": [
            EdgeTuple(0, 1, {"directed": False}),
            EdgeTuple(0, 2, {"directed": False}),
            EdgeTuple(1, 2, {"directed": True}),
            EdgeTuple(2, 3, {"directed": True}),
        ],
        "AdjList": [
            [NbrTuple(1, {"index": 0}), NbrTuple(2, {"index": 1})],
            [NbrTuple(0, {"index": 0}), NbrTuple(2, {"index": 2})],
            [NbrTuple(0, {"index": 1}), NbrTuple(3, {"index": 3})],
            [],
        ],
        "AdjMat": [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 0, 0, 0],
        ],
        "IncMat": [
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, -1, 1],
            [0, 0, 0, -1],
        ],
        "Graph": MIXED,
    },
    {
        "name": "Loop",
        "EdgeList": [
            EdgeTuple(0, 1, {"directed": False}),
            EdgeTuple(0, 2, {"directed": False}),
            EdgeTuple(2, 2, {"directed": True}),
        ],
        "AdjList": [
            [NbrTuple(1, {"index": 0}), NbrTuple(2, {"index": 1})],
            [NbrTuple(0, {"index": 0})],
            [NbrTuple(0, {"index": 1}), NbrTuple(2, {"index": 2})],
        ],
        "AdjMat": [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
        ],
        "IncMat": [
            [1, 1, 0],
            [1, 0, 0],
            [0, 1, 2],
        ],
        "Graph": LOOP,
    },
]
