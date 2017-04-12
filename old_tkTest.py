from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin

WIDTH, HEIGHT = 640, 480

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2+3, HEIGHT/2+3), image=img, state="normal")

red = 0
green = 150
blue = 0
for x in range(WIDTH):
	for y in range(HEIGHT):
		img.put("#ff0000", (x,y))
		#img.put("#%02x%02x%02x" % (int(255.99*(red+x)/WIDTH),green,int(255.99*(blue+y)/HEIGHT)),(x,y))	

#for x in range(4 * WIDTH):
#    y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
#    img.put("#ffffff", (x//4,y))

mainloop()
