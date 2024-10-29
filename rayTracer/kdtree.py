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
		return  Colors(0, 0,0)

	# Check if the ray intersects the node's bounding box
	if not ray.intersects(node.bounds):
		return  Colors(0, 0,0)

	# Test objects in the node
	intersections = []
	for obj in node.objects:
		intersections.extend(Intersection().intersect(obj, ray))
	


	# Recursively check children nodes
	left_color = intersect_kd_tree(ray, node.left, world, computations)
	right_color = intersect_kd_tree(ray, node.right, world, computations)

	if intersections:
		# Assuming the first intersection is the closest hit
		closest_hit = Intersection().hit(intersections)
		computations.prepare_computations(closest_hit, ray, intersections)
		color = computations.shade_hit(world, computations)
		return color

	return Colors(0, 0,0)