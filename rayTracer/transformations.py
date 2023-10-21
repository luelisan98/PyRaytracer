from rayTracer.matrix import Matrix
import math 
class Transformations: 
	@staticmethod
	def translation(x,y,z):
		m = Matrix(4,4).identity()
		m.mat[0][3] = x
		m.mat[1][3] = y
		m.mat[2][3] = z
		return m
	
	@staticmethod
	def scaling(x,y,z):
		m = Matrix(4,4).identity()
		m.mat[0][0] = x
		m.mat[1][1] = y
		m.mat[2][2] = z
		return m
	
	@staticmethod
	def rotation_x(angle):
		#angle_radians = math.radians(angle_degrees)
		cos_r = math.cos(angle)
		sin_r = math.sin(angle)
		m = Matrix(4,4).identity()
		m.mat[1][1] = cos_r
		m.mat[1][2] = -sin_r
		m.mat[2][1] = sin_r
		m.mat[2][2] = cos_r
		return m
	
	@staticmethod
	def rotation_y( angle):
		#angle_radians = math.radians(angle_degrees)
		m = Matrix(4,4).identity()
		cos_r = math.cos(angle)
		sin_r = math.sin(angle)
		m.mat[0][0] = cos_r
		m.mat[0][2] = sin_r
		m.mat[2][0] = -sin_r
		m.mat[2][2] = cos_r
		return m
	
	@staticmethod
	def rotation_z( angle):
		m = Matrix(4,4).identity()
		#angle_radians = math.radians(angle_degrees)
		cos_r = math.cos(angle)
		sin_r = math.sin(angle)
		m.mat[0][0] = cos_r
		m.mat[0][1] = -sin_r
		m.mat[1][0] = sin_r
		m.mat[1][1] = cos_r
		return m
	
	@staticmethod
	def shearing( xy,xz,yx,yz,zx,zy):
		m = Matrix(4,4).identity()
		m.mat[0][1] = xy
		m.mat[0][2] = xz
		m.mat[1][0] = yx
		m.mat[1][2] = yz
		m.mat[2][0] = zx
		m.mat[2][1] = zy
		return m
	
	@staticmethod
	def view_transform(p_from, p_to, p_up):
		pass