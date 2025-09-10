class Demo:
    def __init__(self,a,b,c):
        print("Inside init method")
        print("address of self:",id(self))
        self.attribute1=a
        self.attribute2=b
        self.attribute3=c
        print(self.attribute1)




print("object creation")
obj1=Demo(10,20,30)
print("we are outside of class")
print("address of obj1:", id(obj1))

print(obj1.attribute1)
print(obj1.attribute2)
print(obj1.attribute3)

















