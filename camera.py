from ray import ray
from vector3 import vec3

class camera:
	def __init__(self):
		self.lower_left_corner = vec3(-2.0, -1.5, -1.0)
		self.horizontal = vec3(4, 0.0, 0.0)
		self.vertical = vec3(0.0, 3.0, 0.0)
		self.origin = vec3(0.0, 0.0, 0.0)

	def get_ray(self,u,v):
		return ray(self.origin, self.lower_left_corner + u*self.horizontal + v*self.vertical - self.origin)

