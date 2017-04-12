from hitable import hitable, hit_record

class hitable_list(hitable):
	def __init__(self, hit_list):
		self.hit_list = hit_list

	def hit(self, r, t_min, t_max, rec):
		temp_rec = hit_record()
		hit_anything = False
		closest_so_far = t_max
		for i in range(len(self.hit_list)):
			hit_obj, temp_rec = self.hit_list[i].hit(r, t_min, closest_so_far, temp_rec)
			if hit_obj:			
				hit_anything = True
				closest_so_far = temp_rec.t
				rec = temp_rec
		return (hit_anything, rec)


