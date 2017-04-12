from hitable import hitable, hit_record
from vector3 import vec3

class sphere(hitable):
	def hit(self, r, t_min, t_max, rec):
		print('Hit occured at: ' + str(t_min))

hr = hit_record(4, vec3(1,1,1), vec3(1,0,0))
x = sphere()
x.hit(5,2,5,hr)
x.grbg()
print(x)
