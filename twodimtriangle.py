"""
Triangle Project:
This triangle script will find the Area, Perimeter, Barycenter, 
LongestSide, and determine if it IsRightTriangle.
Here we have the class triangle that has the methods of each parameter mentioned.
The class takes in the 3 coordinates of a two dimensional triangle
"""
import math
class Triangle:
	def __init__(self, Ax,Ay,Bx,By,Cx,Cy):
		self.Ax = Ax
		self.Ay = Ay
		self.Bx = Bx
		self.By = By
		self.Cx = Cx
		self.Cy = Cy

	def __str__(self):
		return "Triangle((%d,%d),(%d,%d),(%d,%d))" % (self.Ax,self.Ay,self.Bx,self.By,self.Cx,self.Cy)

	def Area(self):
		return (1/2)*abs(self.Ax*(self.By-self.Cy)+self.Bx*(self.Cy-self.Ay)+self.Cx*(self.Ay-self.By))

	def Perimeter(self):
		return math.sqrt(((self.Ax-self.Bx)**2)+(self.Ay-self.By)**2)+math.sqrt(((self.Ax-self.Cx)**2)+(self.Ay-self.Cy)**2)+math.sqrt(((self.Bx-self.Cx)**2)+(self.By-self.Cy)**2)

	def Barycenter(self):
		xcoordinate = (self.Ax+self.Bx+self.Cx)/3
		ycoordinate = (self.Ay+self.By+self.Cy)/3
		return "(%f,%f)" % (xcoordinate,ycoordinate)

	def LongestSide(self):
		side1 = math.sqrt(((self.Ax-self.Bx)**2)+(self.Ay-self.By)**2)
		side2 = math.sqrt(((self.Ax-self.Cx)**2)+(self.Ay-self.Cy)**2)
		side3 = math.sqrt(((self.Bx-self.Cx)**2)+(self.By-self.Cy)**2)
		if side1>side2 and side1>side3:
			return side1
		elif side2>side1 and side2>side3:
			return side2
		else:
			return side3

	def IsRightTriangle(self):
		side1 = math.sqrt(((self.Ax-self.Bx)**2)+(self.Ay-self.By)**2)
		side2 = math.sqrt(((self.Ax-self.Cx)**2)+(self.Ay-self.Cy)**2)
		side3 = math.sqrt(((self.Bx-self.Cx)**2)+(self.By-self.Cy)**2)
		if (side1**2 + side2**2) == (side3**2):
			return True
		elif (side2**2 + side3**2) == (side1**2):
			return True
		elif (side1**2 + side3**2) == (side2**2):
			return True
		else:
			return False

def main():
	T = Triangle(0,0,1,0,1,0)
	print(T)
	print(T.Area())
	print(T.Perimeter())
	print(T.Barycenter())
	print(T.LongestSide())
	print(T.IsRightTriangle())

main()
