from __future__ import annotations
from typing import overload, Union
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

    def min_dist_sq(self, point: np.array) -> float:
        dx: float = max(self.min_pos[0] - point[0], 0)
        dx = max(dx, point[0] - self.max_pos[0])
        dy: float = max(self.min_pos[1] - point[1], 0)
        dy = max(dy, point[1] - self.max_pos[1])
        return dx ** 2 + dy ** 2

@overload
def intersect(a: AABB, b: AABB) -> bool:
    pass

@overload
def intersect(s: Sphere, box: AABB) -> bool:
    pass

@overload
def intersect(a: Sphere, b: Sphere) -> bool:
    pass

def intersect(a: Union[AABB, Sphere], b: Union[AABB, Sphere]) -> bool:
    if isinstance(a, AABB) and isinstance(b, AABB):
        no = a.max_pos[0] < b.min_pos[0] or a.max_pos[1] < b.min_pos[1] or b.max_pos[0] < a.min_pos[0] or b.max_pos[1] < a.min_pos[1]
        return not no
    
    if isinstance(a, Sphere) and isinstance(b, AABB):
        distSq = b.min_dist_sq(a.center)
        return distSq <= (a.radius ** 2)
    
    if isinstance(a, Sphere) and isinstance(b, Sphere):
        dist_sq = np.sum((a.center - b.center) ** 2)
        sum_radii = a.radius + b.radius
        return dist_sq <= (sum_radii ** 2)

    return False
