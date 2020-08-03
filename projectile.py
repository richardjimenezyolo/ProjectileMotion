import math

class Node:
	def __init__(self):
		self.Left = None
		self.Val = 0
		self.Right = None
		self.sinA = None
		self.sorted = []

	def Insert(self,v,A):
		if self.Val == 0:
			self.Val = v
			self.sinA = A
			return

		# Left
		if v < self.Val:
			if self.Left == None:
				self.Left = Node()
				self.Left.Val = v
				self.Left.sinA = A
				return
			self.Left.Insert(v,A)

		# Right
		if v > self.Val:
			if self.Right == None:
				self.Right = Node()
				self.Right.Val = v
				return
			self.Right.Insert(v, A)

	def GetMin(self):
		if self.Left == None:
			print(self.sinA)
			return self.Val
		return self.Left.GetMin()


def quadratic(a, b, c):
	sqrt=0
	try:
		sqrt=math.sqrt((b**2) - 4*a*c)
	except Exception as e:
		pass
	
	plus= (-b + sqrt)/(2*a)
	minus= (-b - sqrt)/(2*a)

	if plus > 0:
		return plus

	if minus > 0:
		return minus


def solve_triangle(velocity, sinA, h):
	c=velocity
	a=c*math.sin(math.radians(sinA)) # NO NEED TO DEVICE BY SIN(90) BECAUSE SIN(90) == 1
	b=math.sqrt((c**2) - (a**2))

	t=quadratic(-4.9, a, h)
	d=b*t

	return d

def find_angle(velocity, distance, h):
	tree=Node()
	for sinA in range(1,90):
		yolo=solve_triangle(velocity, sinA, h)-distance
		if yolo > 0:
			tree.Insert(yolo, sinA)

	print(tree.GetMin())


def find_distance(velocity, angle, h):
	return solve_triangle(velocity, angle, h)

print(find_distance(8.5, 30, 100))
