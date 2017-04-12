from tkinter import Tk, Canvas, PhotoImage, mainloop
from vector3 import vec3, unit_vector
from camera import camera
from ray import ray
from sphere import sphere
from hitable import hitable, hit_record
from hitable_list import hitable_list
from material import metal, lambertian
from util import random_in_unit_sphere
import math
import sys
import random


WIDTH, HEIGHT = 400, 300
NS = 100
MAXFLOAT = sys.float_info[0]

def init():
	window = Tk()
	window.title("Tray Racer")
	canvas = Canvas(window, width=WIDTH+2, height=HEIGHT+1, bg="#000000")
	canvas.pack()
	img = PhotoImage(width=WIDTH, height=HEIGHT)
	canvas.create_image((WIDTH/2+2, HEIGHT/2+2), image=img, state="normal")
	return window, img

def color(r, world, depth):
	rec = hit_record()
	hit_obj, rec = world.hit(r, 0.001, MAXFLOAT, rec)
	if hit_obj:
		did_scatter, attenuation, scattered = rec.material.scatter(r,rec)
		if depth < 50 and did_scatter:
			# Apply attenuation by element-wise multiplication
			return attenuation**color(scattered,world,depth+1)
		else:
			return vec3(0,0,0)
	else:
		unit_direction = unit_vector(r.direction())
		t = 0.5*(unit_direction.y() + 1.0)
		return (1.0-t)*vec3(1.0,1.0,1.0) + t*vec3(0.5,0.7,1.0)


def render(img):

	cam = camera()	

	# Adding objects to render
	hitables = list()
	hitables.append(sphere(vec3(0,0,-1), .5, lambertian(vec3(0.8, 0.3, 0.3))))
	hitables.append(sphere(vec3(0,-100.5,-1), 100, lambertian(vec3(0.8, 0.8, 0.0))))
	hitables.append(sphere(vec3(1,0,-1), .5, metal(vec3(0.8, 0.6, 0.2))))
	hitables.append(sphere(vec3(-1,0,-1), .5, metal(vec3(0.8, 0.8, 0.8))))
	world = hitable_list(hitables)

	prcnt_done = 0.0
	new_prcnt_done = 0.0
	for j in range(HEIGHT-1):
		for i in range(WIDTH):
			col = vec3(0,0,0)
			for s in range(NS):	 
				u = float(i+random.random()) / float(WIDTH)
				v = float((HEIGHT-j)+random.random()) / float(HEIGHT)
				r = cam.get_ray(u,v)
	
				p = r.point_at_parameter(2.0)
				col += color(r,world,0)
			col /= float(NS)
			col = vec3(math.sqrt(col[0]), math.sqrt(col[1]), math.sqrt(col[2]))
			ir = int(255.99*col[0])
			ig = int(255.99*col[1])
			ib = int(255.99*col[2])
		
			img.put("#%02x%02x%02x" % (ir,ig,ib), (i,j))
		new_prcnt_done = round(100*(j*WIDTH+i)/float(HEIGHT*WIDTH),2)
		if new_prcnt_done != prcnt_done:
			prcnt_done = new_prcnt_done
			print(prcnt_done)

window, img = init()
render(img)
mainloop()
