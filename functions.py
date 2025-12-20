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
# function examples
# example -1 Temparature conversion [function converts temparature between cellsius and farenheit]
def converts_temparature(temp,unit):
    if unit == 'c':
        return temp * 9/5 + 32  #celcius to farenheit
    elif unit == 'F':
        return (temp-32)*5/9
    else:
        return None
    
print(converts_temparature(25,'c'))
print(converts_temparature(77,'F'))
# ----------------------------------------------------
# example 2 password strength checker 
def is_strong_password(password):
    '''this function checks if the passwd is strong or not '''
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()-+' for char in password):
        return False
    return True
print(is_strong_password("weakpasswd"))
print(is_strong_password("passwrd20"))
print(is_strong_password("sp213"))
print(is_strong_password("IDUHIU3iuwq234$#"))
print(is_strong_password("345678"))
print(is_strong_password("LSFJIEADE"))
# --------------------------------------------
# validate Email Address
import re
# Email validation function 
def is_valid_email(email):
    """this funciton checks if  the Email is valid"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None
#calling funtion
print(is_valid_email("test@example.com"))
print(is_valid_email("invalid_Email"))
# --------------------------------------

    
