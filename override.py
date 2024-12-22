class Parent(): 
	
	def __init__(self): 
		self.value = "Inside Parent"
		
	def show(self): 
		print(self.value) 
		
class Child(Parent): 
	
	def __init__(self): 
		self.value = "Inside Child"
		
	def show(self): 
		print(self.value) 
		
		
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 

print('################################################')
 
def product(a, b):
	p = a * b
	print(p)

def product(a, b, c):
	p = a * b*c
	print(p)
product(4, 5, 5)


print('####################################################')


