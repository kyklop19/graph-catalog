from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT_PATH / "data" / "catalog"


type AdjList = list[list[int]]
type AdjMat = list[list[int]]
type IncMat = list[list[int]]