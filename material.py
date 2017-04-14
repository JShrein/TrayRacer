import random
from abc import ABCMeta, abstractmethod
from vector3 import vec3, unit_vector
from util import random_in_unit_sphere, reflect, refract, schlick
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
	def __init__(self, a, fuzz):
		if type(a) != vec3:
			raise ValueError('Albedo should be a vec3 value')
		self.albedo = a
		self.fuzz = fuzz
	
	def scatter(self, r_in, rec):
		reflected = reflect(unit_vector(r_in.direction()), rec.normal)
		scattered = ray(rec.p, reflected + self.fuzz*random_in_unit_sphere())
		attenuation = self.albedo
		return ((scattered.direction()*rec.normal > 0), attenuation, scattered)

class dielectric(material):
	def __init__(self, ri):
		self.ref_idx = ri
		# attenuation is always 1 for dielectric material
		self.attenuation = vec3(1.0, 1.0, 1.0)

	def scatter(self, r_in, rec):
		outward_normal = vec3()
		reflected = reflect(r_in.direction(), rec.normal)
		ni_over_nt = 0.0
		refracted = vec3()
		reflect_prob = 0
		cosine = 0

		if r_in.direction() * rec.normal > 0:
			outward_normal = -rec.normal
			ni_over_nt = self.ref_idx
			cosine = self.ref_idx * (r_in.direction() * rec.normal) / r_in.direction().length()
		else:
			outward_normal = rec.normal
			ni_over_nt = 1.0 / self.ref_idx
			cosine = -(r_in.direction()*rec.normal) / r_in.direction().length()
		
		did_refract, refracted = refract(r_in.direction(), outward_normal, ni_over_nt, refracted)		
		if did_refract:
			reflect_prob = schlick(cosine, self.ref_idx)
		else:
			reflect_prob = 1.0
		if random.random() < reflect_prob:
			scattered = ray(rec.p, reflected)
		else:
			scattered = ray(rec.p, refracted)
		return (True, self.attenuation, scattered)
