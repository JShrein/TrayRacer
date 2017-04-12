import random
from vector3 import vec3

def random_in_unit_sphere():
	p = vec3()
	p = 2.0*vec3(random.random(), random.random(), random.random()) - vec3(1,1,1)
	while p.squared_length() >= 1.0:
		p = 2.0*vec3(random.random(), random.random(), random.random()) - vec3(1,1,1)
	return p

def reflect(v, n):
	return v - 2*(v*n)*n

