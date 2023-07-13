# Ans 1 
# In object-oriented programming (OOP), a class is a blueprint or a template 
# that defines the characteristics and behaviors of an object
# Example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
result=Dog("sultan",10)
print(result.name)   
print(result.age)   

# Ans 2
# 1 Abstraction.
# 2 Encapsulation.
# 3 Inheritance.
# 4 Polymorphism.



# Ans 3
# The __init__() function is a special method in Python classes that is automatically called when an object is created from the class.
# It is used to initialize the attributes of an object with initial values
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
result=Dog("sultan",10)
print(result.name)   
print(result.age)   

# Ans 4
# The self variable is used to represent the instance
# of the class which is often used in object-oriented programming




# Ans 5
#  1 Single Inheritance:
"""In single inheritance, a subclass inherits from a single superclass. It forms a hierarchical relationship where the subclass inherits all the properties and methods of the superclass.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

my_dog = Dog("Buddy")
print(my_dog.name)  
my_dog.sound()  



# 2  Multiple Inheritance:
"""Multiple inheritance allows a subclass to inherit from multiple superclasses. The subclass can access and use attributes and methods from multiple parent classes.
"""

class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")

my_child = Child()

my_child.method1() 
my_child.method2() 
my_child.method3()  
