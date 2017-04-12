from vector3 import vec3

class ray:
	def __init__(self, *args):
		if len(args) == 0:
			self.A = vec3(0,0,0)
			self.B = vec3(1,0,0)
		elif len(args) == 2:
			if type(args[0]) != vec3 or type(args[1]) != vec3:
				raise ValueError("Expected two vec3s")
			else:
				self.A = args[0]
				self.B = args[1]
		else:
			raise ValueError("Expected 0 or 2 arguments, got " + len(args))

	def origin(self):
		return self.A
	
	def direction(self):
		return self.B

	def point_at_parameter(self, t):
		return self.A + t*self.B


if __name__ == "__main__":
	r = ray(vec3(3,2,5.5), vec3(1,0,0))
	print(r.point_at_parameter(5.0))

