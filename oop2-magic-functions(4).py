

class Customer:
    
    def	__init__(self, name, balance=20):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

    def __sub__(self, other): 
        return Customer("Test_Customer",self.balance - other)

c1 = Customer("Ali") 
print(c1.balance) 
print(str(c1))

c2 = c1 + 30
c3 = c1 - 3
print(c2.balance , c3.balance)

print("###############################################################")
class Employee:

 	def __init__(self , b = 15):
          self.balance = b
          print('Employee created.')

 	def __add__(self , other):
          return Employee(self.balance - other)

 	def __del__(self):
	  	print('Destructor called, Employee deleted.')

obj1 = Employee()
obj2 = obj1 + 10
print(obj2.balance)
del obj2

