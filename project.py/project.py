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

