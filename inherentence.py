class Base1(object):
 	def __init__(self):
 		self.str1 = "Geek1"
 		print("Base1")


class Base2(object):
 	def __init__(self):
 		self.str2 = "Geek2"
 		print("Base2")


class Derived(Base1, Base2):
 	def __init__(self):

 	  def printStrs(self):
 	    	print(self.str1, self.str2)

ob = Derived()
ob.printStrs()

print("#######################################")

class Student: 	
 	_name = None
 	_roll = None
 	_branch = None
 	def __init__(self, name, roll, branch): 
 		self._name = name
 		self._roll = roll
 		self._branch = branch 	
 	def _displayRollAndBranch(self):
 		print("Roll: ", self._roll)
 		print("Branch: ", self._branch)

class Geek(Student):

 	def __init__(self, name, roll, branch): 
          Student.__init__(self, name, roll, branch) 
 		
 	def displayDetails(self):
          # accessing protected data members of super class 
          print("Name: ", self._name) 
 		 # accessing protected member functions of super class 
          self._displayRollAndBranch()

obj = Geek("Ali", 1706256, "Information Technology") 
obj.displayDetails() 

print("#######################################")

class Geek:
	
	__name = None
	__roll = None
	__branch = None

	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	def __displayDetails(self):
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	def accessPrivateFunction(self):
		self.__displayDetails() 

	def get_name(self):
		self.__name 
        
	def set_name(self , name):
		self.__name = name 

	def get_roll(self):
		self.__roll
        
	def set_roll(self , roll):
		self.__roll = roll 

	def get_branch(self):
		self.__branch
        
	def set_branch(self , branch):
		self.__branch = branch 

             
obj = Geek("Osama", 1706256, "Information Technology")

obj.accessPrivateFunction()

