from pathlib import Path
from typing import Any

ROOT_PATH = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT_PATH / "data" / "catalog"


type EdgeList = list[tuple[int, int]]
type AdjList = list[list[int]]
type AdjMat = list[list[int]]
type IncMat = list[list[int]]

type Weight = dict[str, Any]
