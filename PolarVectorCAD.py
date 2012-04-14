#!/usr/bin/env python3
# polar vector CAD library, Bill Ola Rasmussen

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

	v=[]
	v.append(Edge(1,2))
	v.append(Notch(1,2,3))
	v.append(SmoothNotch(1,2,3,4))
	for i in v:
		print('element ', i)

	e=Edge(1,2)
	print('edge',e)

	n=Notch(1,2,3)
	print('Notch',n)

	edgeVec=[]
	for i in range(7):
		r=16-i # length [16,15,...,10]
		a=i*5 # angle [0,5,...,30]
	edgeVec.append(Edge(r,a))

#	notchVec=[]
#	for i in range(7):
#		r=8*(1-i*.05) # % of length 8 [100,95,...,70]
#		a=8+i*11 # angle [8,19,...,74]
#	notchVec.append(Notch(r,a))

def testPoint():
	"""
	>>> p=Point(1,2)
	>>> print(p)
	1,2
	>>> q=Point(3,4)
	>>> print(p+q)
	4,6
	>>> r=Point(3.3,4.4)
	>>> print(p+r)
	4.3,6.4
	>>> v=Point(1,2,3)
	>>> print(v)
	1,2,3
	>>> w=Point(4,5,6)
	>>> print(w)
	4,5,6
	>>> print(v+w)
	5,7,9
	"""
def testPolarVector():
	"""
	>>> v=PolarVector(5,6)
	>>> print(v)
	r:5 a:6
	>>> p=Point(1,2)
	>>> v.draw(p)
	'! point 1,2, vector r:5 a:6'
	>>> p2=v.move(p)
	>>> print(p2) # doctest:+ELLIPSIS
	5.97260947684...,2.5226423163...
	"""
def testEdge():
	"""
	>>> e=Edge(1,2)
	>>> p=Point(3,4)
	>>> e.draw(p) # doctest:+ELLIPSIS
	'_line 3,4 3.9993908270...,4.0348994967...'
	"""
def testNotch():
	"""
	>>> n=Notch(1,2,3)
	>>> print(n)
	r:1 a:2 c:3
	"""
def testSmoothNotch():
	"""
	>>> s=SmoothNotch(1,2,3,4)
	>>> print(s)
	r:1 a:2 c:3 s:4
	"""
def testBezier():
	"""
	>>> p1=Point(1,2)
	>>> p2=Point(3,4)
	>>> p3=Point(5,6)
	>>> b=Bezier(p1,p2,p3)
	>>> b.draw()
	'_curve 1,2 3,4 5,6 _enter'
	"""

if __name__ == "__main__":
	main()
	import doctest
	doctest.testmod()


