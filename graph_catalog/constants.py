from collections import namedtuple
from pathlib import Path
from typing import Any

ROOT_PATH = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT_PATH / "data" / "catalog"

type Weights = dict[str, Any]

EdgeTuple = namedtuple("EdgeTuple", ("start_vertex", "end_vertex", "weights"))

type EdgeList = list[EdgeTuple[int, int, Weights]]
"""Type alias for graph that is in edge list representation."""

NbrTuple = namedtuple("NbrTuple", ("vertex", "weights"))
type AdjList = list[list[NbrTuple[int, Weights]]]
"""Type alias for graph that is in adjacency list representation."""

type AdjMat = list[list[int]]
"""Type alias for graph that is in adjacency matrix representation."""

type IncMat = list[list[int]]
"""Type alias for graph that is in incidence matrix representation."""


class ConversionError(Exception):
    """Raised if conversion between two graph representations isn't supported"""

    pass
