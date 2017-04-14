import random
import math
from vector3 import vec3, unit_vector

def random_in_unit_sphere():
	p = vec3()
	p = 2.0*vec3(random.random(), random.random(), random.random()) - vec3(1,1,1)
	while p.squared_length() >= 1.0:
		p = 2.0*vec3(random.random(), random.random(), random.random()) - vec3(1,1,1)
	return p

def reflect(v, n):
	return v - 2*(v*n)*n

def refract(v, n, ni_over_nt, refracted):
	uv = unit_vector(v)
	dt = uv * n
	discriminant = 1.0 - ni_over_nt*ni_over_nt*(1-dt*dt)
	if discriminant > 0:
		refracted = ni_over_nt*(uv - n*dt) - n*math.sqrt(discriminant)
		return (True, refracted)
	else:
		return (False, None)

def schlick(cosine, ref_idx):
	r0 = (1-ref_idx) / (1+ref_idx)
	r0 = r0*r0
	return r0 + (1-r0)*math.pow((1-cosine),5)

