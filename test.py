# Function
def greet(name):
    print(f"Hello, {name}!")

# Method
class Person:
    def __init__(self, name): # Constructor , it add properties
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

# Usage
greet("John")  # Function call
person = Person("Jane")
person.greet()  # Method call



