class LipBalm:
    def __init__(self, brand, flavor, price):   
        self.brand = brand
        self.flavor = flavor
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Flavor: {self.flavor}, Price: {self.price}"


s1 = LipBalm("Nivea", "Strawberry", "150")

print(s1)


#oop
#class
# class is collection of attribute and methods
# it is like plan/blueprint to create obj
# it is logical entity
# memory is not required

object
#it is physical entity
# it is an instance (obj) of class
#memory is required for execution

#refernce variable
#it is a variable which is poiting to obj.
# we can access data members (attributes)and methods of that obj var.refvar.methodname().

#constructor
#it is one special of method
#it is automatically get invoked(call) when object in to memory
# it is used to initialize the attributes of the class
# job of constructor is to initialize object into memory
# means initialize attributes into memory

#few type of constructors
# default constructor
# parameterized constructor
# copy constructor
#  constructor exicutes only once per object

#types of variable in py
#what is variable
#it is like a container which may or not store data
#it is named memory location

#types of variable in py oop 
#3 types of variable in oop 
#instance variable 
#class variable (static )
#local variable

#instance variable 
#The variable which are written with self keyword is called instance variable 
#individual copy is created for every object
#these variables are initialized byusing constructor 
#those are accessed by using self and ref var

 #2.class variable (static )
 #class variable are the variable which are created outside constructor and inside class body
 #single copy is created and shared among all objects 
 #we can change ,update class variable and update value is shared with all objects
 #class variable can be accessed by ref variable as well as class name
 

#what is method
#it is function which is written inside class.
#def key word is used 
#it is like subprogram/bunch of /group of statements which processing some data (attributes/variable
#its a functionality of that object or its a feture of that object

#types of method /functions
#instance method
#class method
#static method

#instance method
#to process instance variable we need instance method
#first argument if instance method is self 
           #def methodname(self):
              #processing of instance variable \

            #class student:
             #def_init_(self,r,n,m,sub):

class Player:
    def __init__(self, jersey_no, name, runs, wickets, team_name):
        self._jersey_no = jersey_no
        self._name = name
        self._runs = runs
        self._wickets = wickets
        self._team_name = team_name

    # Getter and Setter for jersey_no
    def get_jersey_no(self):
        return self._jersey_no
    
    def set_jersey_no(self, jersey_no):
        self._jersey_no = jersey_no

    # Getter and Setter for name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    # Getter and Setter for runs
    def get_runs(self):
        return self._runs
    
    def set_runs(self, runs):
        self._runs = runs

    # Getter and Setter for wickets
    def get_wickets(self):
        return self._wickets
    
    def set_wickets(self, wickets):
        self._wickets = wickets

    # Getter and Setter for team_name
    def get_team_name(self):
        return self._team_name
    
    def set_team_name(self, team_name):
        self._team_name = team_name



p1 = Player(18, "rohit sharma", 800, 4, "India")

print("Name:", p1.get_name())
print("Runs:", p1.get_runs())
print("Team:", p1.get_team_name())


p1.set_runs(800)
p1.set_team_name("mumbai indians")

print("Updated Runs:", p1.get_runs())
print("Updated Team:", p1.get_team_name())

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call 🚀")
        result = func(*args, **kwargs)
        print("After function call ✅")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Samruddhi")

class Car:
    # Class variable
    wheels = 4

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

    # Instance method → works with object (self)
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Wheels: {Car.wheels}"

    # Class method → works with class (cls)
    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number
        print(f"Updated wheels for all cars: {cls.wheels}")

    # Static method → utility function, independent of class/object
    @staticmethod
    def car_sound():
        return "Vroom Vroom 🚗💨"



car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")

print(car1.display_info())  
print(car2.display_info())

Car.change_wheels(6)         

print(car1.display_info())  
print(car2.display_info())

print(Car.car_sound()) 


#print the fibonacci series 
0,1,2,3,5,8,13.
n1=0
n2=1
n3=0
print(n1,"",n2)
for  i in range(2,10):
    n3=n1+n2
    print("",n3)
    n1=n2
    n2=n3

n1=152
arm=(1*1*1)+(5*5*5)+(3*3*3)  
1+125+27
153

n2=1634
arm=(1*1*1*1)+(6*6*6*6)+(3*3*3*3)+(4*4*4*4)
1+1296+81+256
1634

#define a function to check number is armstrong number or not
def is_armstrong(num):
    digits = str(num)
    power = len(digits)  
    total = sum(int(digit) ** power for digit in digits)
    return num == total



print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True
print(is_armstrong(128))   # False


#define a function to calculate power of number
def power(base,exp):
    result=1
    for i in range(exp):
        result=result*base
        return result
    
#print the following series
# 1 2 4 8 16 32 64 128
# 2 4 6 8 10 12 14 16
# 1 3 5 7 9 11 13 15
# 2 6 12 20 30 42 56 72
# 1 4 9 16 25 36 49 64
# 1 8 27 64 125 216 343 512  


# 1) Powers of 2
print("Series 1:")
for i in range(8):
    print(2**i, end=" ")
print("\n")

# 2) Even numbers
print("Series 2:")
for i in range(2, 18, 2):
    print(i, end=" ")
print("\n")

# 3) Odd numbers
print("Series 3:")
for i in range(1, 17, 2):
    print(i, end=" ")
print("\n")

# 4) n * (n+1)
print("Series 4:")
for n in range(1, 9):
    print(n * (n+1), end=" ")
print("\n")

# 5) Squares
print("Series 5:")
for n in range(1, 9):
    print(n**2, end=" ")
print("\n")

# 6) Cubes
print("Series 6:")
for n in range(1, 9):
    print(n**3, end=" ")
print()

# 1 -2 3 -4 5 -6
for i in range(1, 7):
    if i % 2 == 0:
        print(-i, end=" ")
    else:
        print(i, end=" ")
print()

#-1 2 -3 4 -5 6
for i in range (1,7):
    if i%2==0:
        print(i,end=" ")
    else:
        print(-i,end="")
        print()

#prime number series
# 2 3 5 7 11 13 17 19
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True





























             

           

 
 