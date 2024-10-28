from rayTracer.intersection import Intersection
from rayTracer.colors import Colors


## KD Tree in python 
class KDNode:
    def __init__(self, bounds, objects, left=None, right=None):
        self.bounds = bounds
        self.objects = objects
        self.left = left
        self.right = right 
        
def build_kd_tree(objects, depth=0): 
    if not objects:
        return None

    # Choose axis based on depth
    axis = depth % 3

    # Sort objects by the chosen axis
    objects.sort(key=lambda obj: obj.bounds[axis])

    # Find the median object
    median = len(objects) // 2

    # Create the node
    node = KDNode(
        bounds=objects[median].bounds,
        objects=objects,
        left=build_kd_tree(objects[:median], depth + 1),
        right=build_kd_tree(objects[median + 1:], depth + 1)
    )

    return node

def intersect_kd_tree(ray, node, world, computations):
    if node is None:
        return []

    # Check if the ray intersects the node's bounding box
    if not ray.intersects(node.bounds):
        return []

    # Test objects in the node
    intersections = []
    for obj in node.objects:
        intersections.extend(Intersection().intersect(obj, ray))

    # Recursively check children nodes
    intersections += intersect_kd_tree(ray, node.left, world, computations)
    intersections += intersect_kd_tree(ray, node.right, world, computations)

    if intersections:
        # Assuming the first intersection is the closest hit
        closest_hit = Intersection().hit(intersections)
        computations.prepare_computations(closest_hit, ray, intersections)
        color = computations.shade_hit(world, computations)
        return color

    return Colors(0, 0,0)