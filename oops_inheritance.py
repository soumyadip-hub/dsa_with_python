# inheritance: inheritance is a fundamental concept in object-oriented programming(oop) that allows 
# a class to inherit attribute and methods from another class


# single inheritance
class car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def drive(self):
        print(f"the Prison will drive the {self.enginetype} car")
    
car1=car(4,5,"petrol")
car1.drive()

class tesla(car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving=is_selfdriving
    def selfdriving(self):
        print(f"Tesla supports self driving:{self.is_selfdriving}")

tesla1 = tesla(4,5,"electric",True)
tesla1.selfdriving()
tesla1.drive()

# multiple inheritance (when a class inherits from more than one)
# base class 1
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("subclass must implement this method")

# base class 2
class Pet:
    def __init__(self,owner):
        self.owner=owner

# derived class
class dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    def speak(self):
        return f"{self.name} say woof! ! !"
        
#create an Object
dog = dog("buddy","krish")
print(dog.speak())
print(f"owner:{dog.owner}")


