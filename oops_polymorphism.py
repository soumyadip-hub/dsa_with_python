# polymorphism is a core concept in object-oriented-programming that allows
# objects of different classes to be traeted as objects of  a common superclass.it
# provides a way to perform a single action in different form

# base class 
class Animal:
    def speak(self):
        return "sound of the Animal"
    
# derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
# derived class 
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
# fUnction that demostrate polymorphism
def animal_speak(animal):
    print(animal_speak())

               
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

# ----------------------------------------------------------------

### Polymorphism with function & methods
## Base class

class shape:
    def area(self):
        return "The area of the figure"
    
## Derived class 2

class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    
## derived class 2
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    
## Function that derived polymorphism
def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle = Rectangle(4,5)
circle =circle(3)
print_area(rectangle)
print_area(circle)

        
