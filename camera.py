from ray import ray
from vector3 import vec3, unit_vector
import math

class camera:
	def __init__(self, lookfrom, lookat, vup, vfov, aspect):
		u = vec3()
		v = vec3()
		w = vec3()
		theta = vfov*math.pi/180.0
		half_height = math.tan(theta/2)
		half_width = aspect * half_height
		self.origin = lookfrom
		w = unit_vector(lookfrom - lookat)
		u = unit_vector(vup ^ w)
		v = w ^ u
		self.lower_left_corner = vec3(-half_width, -half_height, -1.0)
		self.lower_left_corner = self.origin - half_width*u - half_height*v - w
		self.horizontal = 2*half_width*u
		self.vertical = 2*half_height*v

	def get_ray(self,s,t):
		return ray(self.origin, self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin)

