#assuming maze is an array of hypothetical squares
#interprets maze as binary tree, where wall/black square equates to no value. If path leads to block surrounded by walls
#then that path is discarded
#to combat loop, always choose left direction if it exists, keep track of already traced paths
#treats first square like root of binary tree, trying to find a path that never returns false
mazAr=[]#list of di-tuples
class Maze(object): # an array of squares, with coordinates and colors. 
#How to describe and treat Maze as both an array and binary tree?
	def __init__(self):
		self.root = None
	def insert (self, insertX, insertY, insertColor):
		if self.root:
			self.root.insert(insertX, insertY, insertColor)
		else:
			self.root = Square(insertColor, inset)
#Each square has coordinate, x and y. Each square has color value. 

class Square(object):
	def __init__(self, color, xCo, yCo):
		self.colorValue = color
		self.x = xCo
		self.y = yCo
		mazeAr.add[self.x,self.y]
	def insert(self, insertX, insertY, insertColor):
		if insertX >self.x:
			if insertY>self.Y:
				if self.right:
					self.right.insert(insertSquareOfColor)
			else:
				self.right = Square(insertSquareOfColor)
		else:
			if insertY>self.Y:
				if self.left:
					self.left.insert(insertXSquareOfColor)
			else:
				self.left = Square(insertSquareOfColor)
		mazeAr.add[insertX,insertY]
	def solve(self): #if square returns white/true and does not have to black square borders
		"""repeats solve on square to right (if exists) and left (if exists)
		figure way to track and discard entire paths that included black square<<<<<--------!!!!! and to descard at particular sqaure"""

		current = self
		while current is not None:
			if current.colorValue == white:
				if current.x+1 in mazeAr[][]:
					current = solve(current.self.x+1, current.self.y)
				if current.y+1 in mazeAr[][]:
					current = solve(current.self.x, current.self.y+1)
				if current.x-1 in mazeAr[][]:
					current = solve(current.self.x, current.self.y-1)
				return True
			else:
				return False

	