from __future__ import annotations
import numpy as np

class Sphere :
    center = np.array([0.0, 0.0])
    radius: float = 0.0

class AABB :
    min_pos = np.array([0.0, 0.0])
    max_pos = np.array([0.0, 0.0])

    def update_min_max(self, point: np.array) -> None:
        self.min_pos[0] = min(self.min_pos[0], point[0])
        self.min_pos[1] = min(self.min_pos[1], point[1])
        self.max_pos[0] = max(self.max_pos[0], point[0])
        self.max_pos[1] = max(self.max_pos[1], point[1])
