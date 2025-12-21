# object oriented programming is a programming paradiagram that uses "object" to design applications and computer programs.
# a class is a blue print for craeting objects attributes methods
class car:
    pass
audi = car()
bmw = car()
print(type(car))
print(audi)
print(bmw)

# instance variabble & methods
class dog:
    ##constructor 
    def __init__(self,name,age):
        self.name = name
        self.age = age
## create objects
dog1 = dog("buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)

dog2 = dog("lucy",4)
print(dog2.name)
print(dog2.age)

# define a class with instance method
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says WOOOFFF")

dog1 = dog("buddy",3)
dog1.bark()
dog2 = dog("lucy",6)
dog2.bark()

# EXAMPLE :- modelling a bank account
# define a class for bank account
class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"{amount} is deposited.new balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn.newbalance is {self.balance}")
    def get_balance(self):
        return self.balance

# craete an object
account = Bankaccount("rolex",5000)
print(account.balance)
# call instance method 
account.deposite(100)
account.withdraw(300)
print(account.get_balance)
