class BBox:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def intersect(self, ray):
        tmin = (self.min.x - ray.origin.x) / ray.direction.x if ray.direction.x != 0 else float('-inf')
        tmax = (self.max.x - ray.origin.x) / ray.direction.x if ray.direction.x != 0 else float('inf')
        if tmin > tmax: tmin, tmax = tmax, tmin

        tymin = (self.min.y - ray.origin.y) / ray.direction.y if ray.direction.y != 0 else float('-inf')
        tymax = (self.max.y - ray.origin.y) / ray.direction.y if ray.direction.y != 0 else float('inf')
        if tymin > tymax: tymin, tymax = tymax, tymin

        if (tmin > tymax) or (tymin > tmax):
            return False

        tmin = max(tmin, tymin)
        tmax = min(tmax, tymax)

        tzmin = (self.min.z - ray.origin.z) / ray.direction.z if ray.direction.z != 0 else float('-inf')
        tzmax = (self.max.z - ray.origin.z) / ray.direction.z if ray.direction.z != 0 else float('inf')
        if tzmin > tzmax: tzmin, tzmax = tzmax, tzmin

        if (tmin > tzmax) or (tzmin > tmax):
            return False

        return True
