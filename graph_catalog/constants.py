from collections import namedtuple
from pathlib import Path
from typing import Any

ROOT_PATH = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT_PATH / "data" / "catalog"

type Weights = dict[str, Any]

EdgeTuple = namedtuple("EdgeTuple", ("start_vertex", "end_vertex", "weights"))
type EdgeList = list[EdgeTuple[int, int, Weights]]

NbrTuple = namedtuple("NbrTuple", ("vertex", "weights"))
type AdjList = list[list[NbrTuple[int, Weights]]]

type AdjMat = list[list[int]]
type IncMat = list[list[int]]
