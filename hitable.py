import ray
from vector3 import vec3
from abc import ABCMeta, abstractmethod
from material import metal,lambertian

class hit_record:
	def __init__(self, *args):
		if len(args) == 0:
			self.t = 0
			self.p = vec3(0,0,0)
			self.normal = vec3(1,0,0)
			self.material = lambertian(vec3(0.6,0.6,0.6))
		else:
			self.t = args[0]
			self.p = args[1]
			self.normal = args[2]
			self.material = args[3]

class hitable(metaclass=ABCMeta):
	@abstractmethod
	def hit(self, r, t_min, t_max, rec):
		pass
