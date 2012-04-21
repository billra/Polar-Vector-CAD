#!/usr/bin/env python3
# Polar Vector CAD library
# Bill Ola Rasmussen
# version 2.0

from math import sin, cos, radians
from copy import deepcopy

# ---- Cartesian Space ----

class Point(object):
	'point coordinates, any dimension'
	def __init__(self,*f):
		self.f=f
	def __str__(self):
		return ','.join(map(str,self.f))
	def move(self,*m):
		'move a point by a list of numbers'
		self.f=[x+y for x,y in zip(self.f,m)]
		return self

class Bezier(object):
	'Points defining a Bezier curve (start Point, 1-n control Points, end Point)'
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
	def move(self,p):
		'point + vector -> point'
		return p.move(self.r*cos(radians(self.a)),self.r*sin(radians(self.a)))
	def mirror(self,a):
		'mirror vector across angle'
		self.a=2*a-self.a
		return self
	def draw(self,p):
		'base PolarVector "draws" a comment and updates Point location'
		return '! start('+str(p)+'), vector '+str(self)+', end('+str(self.move(p))+')'

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
	def draw(self,p):
		'draw notch in cartesian space, evaluates to two Edges'
		return Edge(self.r,self.a+90-self.c/2.).draw(p)+'\n'+ \
		       Edge(self.r,self.a-90+self.c/2.).draw(p)

class SmoothNotch(Notch):
	'notch with smooth transition'
	def __init__(self,r,a,c,s):
		super().__init__(r,a,c)
		self.s=s # smooth blending >0, <=1
	def __str__(self):
		return super().__str__()+' s:'+str(self.s) 
	# todo: SmoothNotch evaluates to two QuadraticBeziers when drawing

if __name__ == "__main__":
	import doctest
	doctest.testfile('tests.txt')
	doctest.testfile('testSless1c.txt')


