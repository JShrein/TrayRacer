import math
import numpy as np

class vec3:
	def __init__(self, *args):
		if(len(args) == 0):
			self.e = np.array([0,0,0], dtype='float32')
		elif(len(args) == 1):
			self.e = args[0]
		elif len(args) == 3:
			self.e = np.array(args, dtype='float32');
		else:
			raise ValueError("Expected 3D vector or no arguments")

	def x(self):
		return self.e[0]

	def y(self):
		return self.e[1]

	def z(self):
		return self.e[2]

	def r(self):
		return self.e[0]

	def g(self):
		return self.e[1]

	def b(self):
		return self.e[2]

	def __setitem__(self,key,value):
		self.e[key] = value	
	
	def __getitem__(self,key):
		return self.e[key]

	# Arithmetic & Assignment operators
	def __iadd__(self, v):
		self.e = np.add(self.e, v.e)
		return self

	def __isub__(self, v):
		self.e = np.subtract(self.e, v.e)
		return self

	def __imul__(self, v):
		self.e = np.multiply(self.e, v.e)
		return self

	def __itruediv__(self, v):
		if type(v) == vec3:
			self.e = np.divide(self.e, v.e)
		else:
			self.e = np.divide(self.e, v)
		return self

	def __pos__(self):
		return vec3(self.e)

	def __neg__(self):
		return vec3(-self.e)
	
	def __add__(self, v):
		return vec3(np.add(self.e,v.e))

	def __sub__(self, v):
		return vec3(np.subtract(self.e,v.e))

	# ** operator, element-wise multiply
	def __pow__(self, v):
		return vec3(np.multiply(self.e,v.e))
	
	# * operator, dot product or scale, depending on type
	def __mul__(self, elem):
		if type(elem) == vec3:
			return np.dot(self.e, elem.e)
		if type(elem) == float or type(elem) == int or type(elem) == np.float32:
			return vec3(np.multiply(elem,self.e))
		
		raise ValueError("Expected float or vec3, got " + str(type(elem)))

	def __rmul__(self, elem):
		if type(elem) == float or type(elem) == int or type(elem) == np.float32:
			return vec3(np.multiply(elem,self.e))
		raise ValueError("Expected numeric argument, got " + str(type(elem)))

	def __truediv__(self, elem):
		if type(elem) == vec3:
			return vec3(np.divide(self.e,elem.e))
	
		if type(elem) == float or type(elem) == int or type(elem) == np.float32:
			return vec3(np.divide(self.e,elem))
		
		raise ValueError("Expected float or vec3, got " + str(type(elem)))

	# ^ operator, cross product 
	def __xor__(self, v):
		return vec3(np.cross(self.e,v.e))

	def length(self):
		return np.linalg.norm(self.e)

	# For now, using dot product
	def squared_length(self):
		return np.dot(self.e,self.e)

	def make_unit_vector(self):
		v_length = self.length()
		self.e = np.divide(self.e, v_length)

	def normalize(self):
		v_length = self.length()
		return vec3(np.divide(self.e,v_length))

	def __str__(self):
		return '('+str(self.e[0])+', '+str(self.e[1])+', '+str(self.e[2])+')'

def unit_vector(v):
	return v / v.length()	

if __name__ == '__main__':
	v1 = vec3(1,2,3)
	v2 = vec3(4,5,6)

	v3 = v1*v2
	print(v3)
	v4 = v3*2.213
	v5 = 2.213*v3
	print(v4)
	print(v5)
