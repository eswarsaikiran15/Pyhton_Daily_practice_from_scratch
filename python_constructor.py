#creating a constructor
"""
1.constructor invokes whenever the object is created
2.constructor always assigns values to variables
3.constructor is a method ,so we dine that with def keyword

we acutally seen function in previous files ,in oops we want to call that as methods
The clean rule (no ambiguity)
Function → defined outside a class
Method → defined inside a class
"""
from copyreg import constructor


class Constructor:
    def __init__(self,name,id):  # name and id are parameters and self is just a convention, not a keyword. You can replace it with any valid variable name
        self.name=name   # this self.name and self.id are the class attributes
        self.id=id

    def get_name(self):    #normal method
        return self.name
    def add(self,a,b):
        return a+b
s1=Constructor("kiran",1)
print(s1.name,s1.id)

print(s1.get_name())
print(s1.add(3,4))

s2=Constructor("ravi",40)
print(s2.name,s2.id)






"""
Types of methods (this is where precision matters)

Inside a class, you get 3 kinds:

1. Instance Method (most common)
def show(self):
    pass
Works on object
Uses self

2. Class Method
@classmethod
def create(cls):
    pass
Works on class
Uses cls

3. Static Method
@staticmethod
def helper():
    pass
No self, no cls


But still a method, not a function
Because it's inside a class
"""