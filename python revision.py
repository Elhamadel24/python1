def loop():
     for x in range(10): 
         print (x)
         if x == 3:
             return
        
loop();
("###############################################################################")
def twice(y , x):
     return y(y(x))    

def mul(x):
     return x**2   
out = twice(mul , 2)
print(out)


("###############################################################################")

##define function inside another

def function1(x):
     def function2(y):
        return y + 2
     return 3 * function2(x)
    
a = function1(2)
print (a)

# b = function2(2.5) # error
# print (b)

print("###############################################################################")

x = 1
def add_one (x):
     x = x + 1
     # add one to the local x
     return x

y = add_one (x)
print(x)
print(y)
 
print("###############################################################################")

def f1():
     global x
     x = x + 1
     return x

def f2():
     return x

def f3():
     x = 5
     return x+1


x = 0
print(f1()) #global
print(f2()) #global
print(f3()) #local
 


