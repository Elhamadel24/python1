class FirstClass: 
     def setdata(self, value): 
         self.data = value 
     def display(self):
         print(self.data) 
         
         
         
x = FirstClass() 
y = FirstClass() 


print(x)
print(y)
print(isinstance(x, FirstClass))

print("##########################")

class Customer:
     def	__init__(self, name, balance=0):  
         self.name = name
         self.balance = balance
         print("The	init	method was called")
        

cust = Customer("Lara de Silva") 
print(cust.balance)

print("##########################")

class Person(object):

	def __init__(self, name, idnumber):
 		self.name = name
 		self.idnumber = idnumber

def display(self):
 		print(self.name)
 		print(self.idnumber)

class Employee(Person):
 	def __init__(self, name, idnumber, salary, post):
 		self.salary = salary
 		self.post = post

 		Person.__init__(self, name, idnumber)

a = Employee('Rahul', 886012, 200000, "Intern")

a.display()

print("########################################################")

class Person():
    def __init__(self, name, age):
    	self.name = name
    	self.age = age
    
    def display(self):
    	print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
    	self.sName = name
    	self.sAge = age
    	# inheriting the properties of parent class
    	super().__init__("Osama", age)
    
    def displayInfo(self):
    	print(self.sName, self.sAge)

obj = Student("Khalid", 23)
obj.display()
obj.displayInfo()

