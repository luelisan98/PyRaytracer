from rayTracer.intersection import Intersection
from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.bbox import BBox

class BVHNode:
    def __init__(self, bounds, objects, left=None, right=None):
        self.bounds = bounds
        self.objects = objects
        self.left = left
        self.right = right

def build_bvh(objects):
    if not objects:
        return None

    if len(objects) == 1:
        return BVHNode(objects[0].bounds(), objects)

    objects.sort(key=lambda obj: obj.bounds().min.x)
    mid = len(objects) // 2

    left_child = build_bvh(objects[:mid])
    right_child = build_bvh(objects[mid:])

    left_bounds = left_child.bounds if left_child else None
    right_bounds = right_child.bounds if right_child else None

    combined_bounds = combine_bounds(left_bounds, right_bounds)

    return BVHNode(combined_bounds, objects, left_child, right_child)


def combine_bounds(left_bounds, right_bounds):
    if left_bounds is None:
        return right_bounds
    if right_bounds is None:
        return left_bounds

    min_x = min(left_bounds.min.x, right_bounds.min.x)
    min_y = min(left_bounds.min.y, right_bounds.min.y)
    min_z = min(left_bounds.min.z, right_bounds.min.z)
    max_x = max(left_bounds.max.x, right_bounds.max.x)
    max_y = max(left_bounds.max.y, right_bounds.max.y)
    max_z = max(left_bounds.max.z, right_bounds.max.z)

    return BBox(Tuples(min_x, min_y, min_z), Tuples(max_x, max_y, max_z))


def intersect_bvh(ray, node, world, computations):
    if node is None:
        return Colors(0, 0, 0)

    if not node.bounds.intersect(ray):
        return Colors(0, 0, 0)

    intersections = []
    for obj in node.objects:
        intersections.extend(Intersection().intersect(obj, ray))

    if intersections:
        closest_hit = Intersection().hit(intersections)
        if closest_hit:
            computations.prepare_computations(closest_hit, ray, intersections)
            current_color = computations.shade_hit(world, computations)
            return current_color

    left_color = intersect_bvh(ray, node.left, world, computations)
    right_color = intersect_bvh(ray, node.right, world, computations)

    return (left_color + right_color) * 0.5  # Adjust accumulation method if needed
