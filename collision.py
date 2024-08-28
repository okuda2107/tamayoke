from __future__ import annotations
import numpy as np

class Sphere :
    center = np.array([0.0, 0.0])
    radius: float = 0.0

class AABB :
    min_pos = np.array([0.0, 0.0])
    max_pos = np.array([0.0, 0.0])

    def __init__(self, size: np.array, screensize: np.array):
        normalize_size = size / screensize
        self.min_pos = - normalize_size / 2
        self.max_pos = normalize_size / 2

    def update_min_max(self, point: np.array) -> None:
        self.min_pos[0] = min(self.min_pos[0], point[0])
        self.min_pos[1] = min(self.min_pos[1], point[1])
        self.max_pos[0] = max(self.max_pos[0], point[0])
        self.max_pos[1] = max(self.max_pos[1], point[1])

def intersect(a: AABB, b: AABB) -> bool:
    no = a.max_pos[0] < b.min_pos[0] or a.max_pos[1] < b.min_pos[1] or b.max_pos[0] < a.min_pos[0] or b.max_pos[1] < a.min_pos[1]
    return not no
