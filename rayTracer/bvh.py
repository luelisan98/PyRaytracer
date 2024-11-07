from rayTracer.intersection import Intersection

class BVHNode:
    def __init__(self, left=None, right=None, bbox=None):
        self.left = left
        self.right = right
        self.bbox = bbox

class BVH:
    def __init__(self, objects):
        self.objects = objects
        self.root = self.build_tree(objects)

    def build_tree(self, objects):
        if len(objects) == 1:
            return BVHNode(bbox=objects[0].bbox)
        elif len(objects) == 2:
            left, right = objects
            return BVHNode(left=self.build_tree([left]), right=self.build_tree([right]), bbox=left.bbox.union(right.bbox))
        else:
            mid = len(objects) // 2
            left = self.build_tree(objects[:mid])
            right = self.build_tree(objects[mid:])
            return BVHNode(left=left, right=right, bbox=left.bbox.union(right.bbox))

    def intersect(self, ray):
        if self.root.bbox.intersect(ray):
            return self.intersect_node(ray, self.root)
        return []

    def intersect_node(self, ray, node):
        if node.left is None and node.right is None:
            return node.bbox.intersect(ray)
        results = []
        if node.left and node.left.bbox.intersect(ray):
            results.extend(self.intersect_node(ray, node.left))
        if node.right and node.right.bbox.intersect(ray):
            results.extend(self.intersect_node(ray, node.right))
        return results

class Object:
    def __init__(self, bbox):
        self.bbox = bbox

    def intersect(self, ray):
        intersections = Intersection().intersect(self, ray)
        return intersections

class BBox:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def union(self, other):
        min_x = min(self.min[0], other.min[0])
        min_y = min(self.min[1], other.min[1])
        min_z = min(self.min[2], other.min[2])
        max_x = max(self.max[0], other.max[0])
        max_y = max(self.max[1], other.max[1])
        max_z = max(self.max[2], other.max[2])
        return BBox([min_x, min_y, min_z], [max_x, max_y, max_z])

    def intersect(self, ray):
        tmin = (self.min[0] - ray.origin[0]) / ray.direction[0] if ray.direction[0] != 0 else float('inf')
        tmax = (self.max[0] - ray.origin[0]) / ray.direction[0] if ray.direction[0] != 0 else float('inf')
        if tmin > tmax: tmin, tmax = tmax, tmin
        tmin = max(tmin, (self.min[1] - ray.origin[1]) / ray.direction[1] if ray.direction[1] != 0 else float('inf'))
        tmax = min(tmax, (self.max[1] - ray.origin[1]) / ray.direction[1] if ray.direction[1] != 0 else float('inf'))
        if tmin > tmax: return False
        tmin = max(tmin, (self.min[2] - ray.origin[2]) / ray.direction[2] if ray.direction[2] != 0 else float('inf'))
        tmax = min(tmax, (self.max[2] - ray.origin[2]) / ray.direction[2] if ray.direction[2] != 0 else float('inf'))
        if tmin > tmax: return False
        return True

