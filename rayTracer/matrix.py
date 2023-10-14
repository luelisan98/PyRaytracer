from rayTracer.tuples import Tuples
import math 

EPSILON = 0.00001

class Matrix():
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.mat = [[0 for _ in range(cols)] for _ in range(rows)]

	def equal(self, a, b):
		return abs(a - b) < EPSILON

	def __eq__(self, other):
		if self.rows != other.rows or self.cols != other.cols:
			return False

		for row in range(self.rows):
			for col in range(self.cols):
				if not self.equal(self.mat[row][col], other.mat[row][col]):
					return False

		return True
	
	def __mul__(self, other):
		if isinstance(other, Matrix):
			if self.cols != other.rows:
				return None

			result = Matrix(self.rows, other.cols)

			for row in range(self.rows):
				for col in range(self.cols):
					for k in range(other.rows):
						result.mat[row][col] += (self.mat[row][k] * other.mat[k][col])	
					result.mat[row][col] = round(result.mat[row][col])

			return result
		elif isinstance(other, Tuples):
			result = Tuples(
				self.mat[0][0] * other.x + self.mat[0][1] * other.y + self.mat[0][2] * other.z + self.mat[0][3] * other.w,
				self.mat[1][0] * other.x + self.mat[1][1] * other.y + self.mat[1][2] * other.z + self.mat[1][3] * other.w,
				self.mat[2][0] * other.x + self.mat[2][1] * other.y + self.mat[2][2] * other.z + self.mat[2][3] * other.w,
				self.mat[3][0] * other.x + self.mat[3][1] * other.y + self.mat[3][2] * other.z + self.mat[3][3] * other.w
			)
			return result

	def identity(self):
		identity = Matrix(self.rows, self.cols)
		
		# Construct the identity matrix 
		for rows in range(self.rows):
			identity.mat[rows][rows] = 1

		return identity
	
	def transposing(self):
		# Create a new matrix with swapped rows and columns
		transposed = Matrix(self.cols, self.rows)

		# Populate the new matrix with elements from the original matrix
		for row in range(self.rows):
			for col in range(self.cols):
				transposed.mat[col][row] = self.mat[row][col]

		return transposed
	
	def determinant(self):
		if self.rows == 2:
			det = self.mat[0][0] * self.mat[1][1] - self.mat[0][1] * self.mat[1][0]
		else:
			det = 0
			for col in range(self.cols):
				cofactor_row_col = self.cofactor(0, col)
				det += self.mat[0][col] * cofactor_row_col

		return det
	
	def submatrix(self, row_sub, col_sub):
		submatrix = Matrix(self.rows - 1, self.cols - 1)

		sub_row = 0
		for row in range(self.rows):
			if row == row_sub:
				continue  # Skip the specified row
			sub_col = 0
			for col in range(self.cols):
				if col == col_sub:
					continue  # Skip the specified column
				submatrix.mat[sub_row][sub_col] = self.mat[row][col]
				sub_col += 1
			sub_row += 1
		
		return submatrix

	def minor(self, row_sub, col_sub):
		# Calculate the minor by computing the determinant of the submatrix
		submatrix = self.submatrix(row_sub, col_sub)
		minor_value = submatrix.determinant()

		return minor_value
	
	def cofactor(self, row_sub, col_sub):
		minor_value = self.minor(row_sub, col_sub)
		sign = -1 if (row_sub + col_sub) % 2 != 0 else 1
		cofactor_value = sign * minor_value

		return cofactor_value

	def is_invertible(self):
		if self.determinant() == 0:
			return False
		else:
			return True
		
	def inverse(self):
		if not self.is_invertible():
			return None
		
		det = self.determinant()
		M2 = Matrix(self.rows, self.cols)
		for row in range(self.rows):
			for col in range(self.cols):
				cof = self.cofactor(row, col)
				#M2.mat[col][row] = round(cof / det, 5) 
				M2.mat[col][row] = cof / det 
			
		return M2 
