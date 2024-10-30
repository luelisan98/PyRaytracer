from rayTracer.intersection import Intersection
from rayTracer.colors import Colors


## KD Tree in python 
class KDNode:
	def __init__(self, bounds, objects, left=None, right=None):
		self.bounds = bounds
		self.objects = objects
		self.left = left
		self.right = right 
		
# kdtree.py

def build_kd_tree(objects, depth=0):
	if not objects:
		return None
	
	axis = depth % 3
	objects.sort(key=lambda obj: obj.bounds()[0].x if axis == 0 else (obj.bounds()[0].y if axis == 1 else obj.bounds()[0].z))
	median = len(objects) // 2

	node = KDNode(
		bounds=objects[median].bounds(),
		objects=objects,
		left=build_kd_tree(objects[:median], depth + 1),
		right=build_kd_tree(objects[median + 1:], depth + 1)
	)
	
	return node

def intersect_kd_tree(ray, node, world, computations):
    if node is None:
        return Colors(0, 0, 0)
    
    if not ray.intersects(node.bounds):
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

    left_color = intersect_kd_tree(ray, node.left, world, computations)
    right_color = intersect_kd_tree(ray, node.right, world, computations)
    
    return (left_color + right_color) * 0.5  # Adjust accumulation method if needed
