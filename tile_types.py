from os import walk
from typing import Tuple

import numpy as np # type: ignore

# tile graphics structured type compatible with Console.tile_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # unicode code point
        ("fg", "3B"), # 3 unisigned bytes, for RGB colors
        ("bg", "3B")
    ]
)

# tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), # true if tile is walkable
        ("transparent", np.bool), # true if not blocking FOV
        ("dark", graphic_dt), # graphics for when tile is no in FOV
    ]
)

def new_tile(
    *, # enforce the use of keywords, so the paramater order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual file types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255,), (0, 0, 100)),
)
