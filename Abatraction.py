x = 5 
y = "hello" 
a = [1,2,3]
try: 
    print("Test1")
    print(a[3])
    z = x + y 
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")
    
print("####################################################") 

from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	def noofsides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 

	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	def noofsides(self): 
		print("I have 4 sides") 

R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 
 
print("####################################################") 

