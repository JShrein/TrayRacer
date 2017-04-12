from hitable import hitable, hit_record
import math

class sphere(hitable):
	def __init__(self, *args):
		if len(args) == 3:
			self.center = args[0]
			self.radius = args[1]
			self.material = args[2]

	def hit(self, r, t_min, t_max, rec):	
		oc = r.origin() - self.center
		a = r.direction() * r.direction()
		b = oc * r.direction()
		c = (oc*oc) - self.radius*self.radius
		discriminant = b*b - a*c
		if discriminant > 0:
			disc_root = math.sqrt(discriminant)
			temp = (-b - disc_root)/a
			if temp < t_max and temp > t_min:
				rec.t = temp
				rec.p = r.point_at_parameter(rec.t)
				rec.normal = (rec.p - self.center) / self.radius
				rec.material = self.material
				return (True, rec)
			temp = (-b + disc_root)/a
			if temp < t_max and temp > t_min: 
				rec.t = temp
				rec.p = r.point_at_parameter(rec.t)
				rec.normal = (rec.p - self.center) / self.radius
				rec.material = self.material
				return (True, rec)
		return (False, rec)
	
		
