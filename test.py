class LipBalm:
    def __init__(self, brand, flavor, price):   
        self.brand = brand
        self.flavor = flavor
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Flavor: {self.flavor}, Price: {self.price}"


s1 = LipBalm("Nivea", "Strawberry", "150")

print(s1)


