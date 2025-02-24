from constants import EdgeTuple, NbrTuple
from graph import Edge, Graph, Vertex

graphs = [
    # {
    #     "EdgeList": [],
    #     "AdjList": [[], [], []],
    #     "AdjMat": [],
    #     "IncMat": [],
    #     "Graph": Graph([]),
    # },
    # Empty
    {
        "EdgeList": [],
        "AdjList": [[], [], []],
        "AdjMat": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "IncMat": [[], [], []],
        "Graph": Graph(
            [
                Vertex(0),
                Vertex(1),
                Vertex(2),
            ]
        ),
    },
    # Undirected
    {
        "EdgeList": [
            EdgeTuple(0, 1, {"directed": False}),
            EdgeTuple(1, 2, {"directed": False}),
            EdgeTuple(2, 0, {"directed": False}),
        ],
        "AdjList": [
            [NbrTuple(1, {"index": 0}), NbrTuple(2, {"index": 1})],
            [NbrTuple(2, {"index": 2}), NbrTuple(0, {"index": 0})],
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
        "Graph": Graph([]),  #! TODO
    },
    # Directed
    {
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
        "Graph": Graph([]),  #! TODO
    },
    # Mixed
    {
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
        "Graph": Graph([]),  #! TODO
    },
    # Loop
    {
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
        "Graph": Graph([]),  #! TODO
    },
]
