from abc import ABCMeta, abstractmethod
from vector3 import vec3, unit_vector
from util import random_in_unit_sphere, reflect
from ray import ray

class material(metaclass=ABCMeta):
	@abstractmethod
	def scatter(self, r_in, rec):
		pass

class lambertian(material):
	def __init__(self, a):
		if type(a) != vec3:
			raise ValueError('Albedo should be a vec3 value')
		self.albedo = a
	
	def scatter(self, r_in, rec):
		target = rec.p + rec.normal + random_in_unit_sphere()
		scattered = ray(rec.p, target - rec.p)
		attenuation = self.albedo
		return (True, attenuation, scattered)

class metal(material):
	def __init__(self, a):
		if type(a) != vec3:
			raise ValueError('Albedo should be a vec3 value')
		self.albedo = a
	
	def scatter(self, r_in, rec):
		reflected = reflect(unit_vector(r_in.direction()), rec.normal)
		scattered = ray(rec.p, reflected)
		attenuation = self.albedo
		return ((scattered.direction()*rec.normal > 0), attenuation, scattered)


