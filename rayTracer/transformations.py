from rayTracer.matrix import Matrix
import math 
class Transformations: 
	def __init__(self):
		self.transformation = Matrix(4,4)
		self.transformation = self.transformation.identity()


	def translation(self, x,y,z):
		self.transformation.mat[0][3] = x
		self.transformation.mat[1][3] = y
		self.transformation.mat[2][3] = z
		return self.transformation
	
	def scaling(self,x,y,z):
		self.transformation.mat[0][0] = x
		self.transformation.mat[1][1] = y
		self.transformation.mat[2][2] = z
		return self.transformation
	
	def rotation_x(self,angle_degrees):
		angle_radians = math.radians(angle_degrees)
		cos_r = math.cos(angle_radians)
		sin_r = math.sin(angle_radians)

		self.transformation.mat[1][1] = cos_r
		self.transformation.mat[1][2] = -sin_r
		self.transformation.mat[2][1] = sin_r
		self.transformation.mat[2][2] = cos_r

		return self.transformation