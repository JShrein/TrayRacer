from tkinter import Tk, Canvas, PhotoImage, mainloop
from vector3 import vec3, unit_vector
from ray import ray
import math
import sys

WIDTH, HEIGHT = 640, 480
MAXFLOAT = sys.float_info[0]

def init():
	window = Tk()
	canvas = Canvas(window, width=WIDTH+2, height=HEIGHT+1, bg="#000000")
	canvas.pack()
	img = PhotoImage(width=WIDTH, height=HEIGHT)
	canvas.create_image((WIDTH/2+4, HEIGHT/2+4), image=img, state="normal")
	return window, img

def color(ray, world):
	rec = hit_record()
	if world.hit(r, 0.0, MAXFLOAT, rec):
		return 0.5*vec3(rec.normal.x()+1, rec.normal.y()+1, rec.normal.z()+1)
	else:
		unit_direction = vec3(unit_vector(r.direction()))
		t = 0.5*(unit_direction.y() + 1.0)
		return (1.0-t)*vec3(1.0,1.0,1.0) + t*vec3(0.5,0.7,1.0)

def render(img):

	lower_left_corner = vec3(-2.0, -1.5, -1.0)
	horizontal = vec3(4, 0.0, 0.0)
	vertical = vec3(0.0, 3, 0.0)
	origin = vec3(0.0, 0.0, 0.0)			

	# Adding objects to render
	list

	for j in range(HEIGHT-1):
		for i in range(WIDTH): 
			u = float(i) / float(WIDTH)
			v = float(HEIGHT-j) / float(HEIGHT)
			r = ray(origin, lower_left_corner + u * horizontal + v * vertical)
			col = color(r)
			ir = int(255.99*col[0])
			ig = int(255.99*col[1])
			ib = int(255.99*col[2])
		
			img.put("#%02x%02x%02x" % (ir,ig,ib), (i,j))

window, img = init()
render(img)
mainloop()
