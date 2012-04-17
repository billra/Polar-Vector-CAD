#!/usr/bin/env python3
# Polar Vector CAD library, Bill Ola Rasmussen

from math import sin, cos, radians

# ---- Cartesian Space ----

class Point(object):
	'point coordinates, any dimension'
	def __init__(self,*f):
		self.f=f
	def __str__(self):
		return ','.join(map(str,self.f))
	def __add__(self,rhs):
		return Point( *map(sum,zip(self.f,rhs.f)) )
	# todo: draw function

class Bezier(object):
	'Points defining a Bezier curve (start point, 1-n control points, end point)'
	def __init__(self,*p):
		self.p=p
	def __str__(self):
		return ' '.join(map(str,self.p))
	def draw(self):
		return '_curve '+str(self)+' _enter'

# ---- Polar Space ----

class PolarVector(object):
	'v=(r,a): vector described by length and angle'
	def __init__(self,r,a):
		self.r=r # length
		self.a=a # angle (in degrees)
	def __str__(self):
		return 'r:'+str(self.r)+' a:'+str(self.a)
	def draw(self,p):
		'draw vector in cartesian space starting from point p'
		return '! point '+str(p)+', vector r:'+str(self.r)+' a:'+str(self.a) # output a comment
	def move(self,p):
		'point + vector -> point'
		return p+Point(self.r*cos(radians(self.a)),self.r*sin(radians(self.a)))

class Edge(PolarVector):
	def draw(self,p):
		'draw vector in cartesian space starting from point p'
		return '_line '+str(p)+' '+str(self.move(p))

class Notch(PolarVector):
	'vector with two walls and an opening angle'
	def __init__(self,r,a,c):
		'parameters: wall length, face angle, central notch angle'
		super().__init__(r,a)
		self.c=c # central angle of notch
	def __str__(self):
		return super().__str__()+' c:'+str(self.c)
	# todo: notch evaluates to two Edges when drawing


class SmoothNotch(Notch):
	'notch with smooth transition'
	def __init__(self,r,a,c,s):
		super().__init__(r,a,c)
		self.s=s # smooth blending >0, <=1
	def __str__(self):
		return super().__str__()+' s:'+str(self.s)
	# todo: SmoothNotch evaluates to two QuadraticBeziers when drawing

# ---- end library ----

def main():

	# sless 1c reference design

	# 14 LE bridle points, 2 TE bridle points (in same bridle) -> 13 LE segments: 1 center, 6 per side
	# stack 7 segments (array command)
	# clip off at an angle to create shorter segments toward tips, length range: [16-10] lr
	# choose a segment incidence angle to create LE curve: [5°] ia
	# rotate segments into their final angle: grab 6, rotate by ia, grab 5 rotate, etc.

	edgeVec=[]
	for i in range(7):
		r=16-i # length [16,15,...,10]
		a=i*5 # angle [0,5,...,30]
	edgeVec.append(Edge(r,a))

	# choose a notch wall length: [8] nw
	# choose a notch angle: [8°] na (greater or equal to segment incidence angle ia)
	# make 7 notches total (array command) 
	# scale notches so smaller toward end, range: [100%-70%] -> 100, 95, 90, 85, 80, 75, 70% sn
	# choose mid and tip notch rotation angle: [8°,74°] sr, er 
	#   (should follow tension vector from bridle point, see wrinkle in canopy)
	# (74-8)/6=11 nr, so rotate each notch 11° using the same segment grab and rotate strategy

	notchVec=[]
	for i in range(7):
		r=8*(1-i*.05) # % of length 8 [100,95,...,70]
		a=8+i*11 # angle [8,19,...,74]
	notchVec.append(Notch(r,a,8))

	# choose a tip width, tw, probably less than last segment length: [8]


if __name__ == "__main__":
	main()
	import doctest
	doctest.testfile('tests.txt')


