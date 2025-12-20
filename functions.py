#1.introduction to functions 
# 2.defining functions
# 3.Calling funtions
# 4.function Parameters
# 5.default parameters 
# 6.Variable-length Arguments
# 7.Return Statemnets

# syntax 
#| def function_name(parameters)
#|    "docstring"
#|# function body 
#|return expression
#---------------------------------
# sample example 1(functions with parameters)
def add(a,b):
    return a+b
result = add(2,4)
print(result)
#---------------------------------
# sample example 2(default parameters)
def greet(name):
    print(f"hello {name} bondhu kemon acho! :) ")
greet("rolex")
#----------------------------------
# sample example 3(variable length argument)
def print_numbers(*args):
    for numbers in args:
        print(numbers)
print_numbers(1,2,3,4,5,6,7,"rolex","Tom & Jerry")
#-----------------------------------------
# sample example 4(keyword arguments)
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(name = "rolex",age="69",country = "INDIA")
#---------------------------------------------
# sample example 5(positional and keyword arguments (args + kwargs))
def print_details(*args,**kwargs):
    for val in args:
        print(f"positional argument :{val}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(1,2,3,"rolex",name="rolex420",age="69",country="INDIA")
#------------------------------------------------