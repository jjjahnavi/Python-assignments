#Write two methods with the same name but different number of parameters of same type and call the methods
class MyClass:
    def my_method(self, arg1):
        """Method with one parameter."""
        print(f"Method with one parameter called: {arg1}")

    def my_method(self, arg1, arg2):
        """Method with two parameters."""
        print(f"Method with two parameters called: {arg1}, {arg2}")

# Create an instance of the class
obj = MyClass()

# Call the method with two parameters
obj.my_method("Hello", "World")

# Calling with only one parameter will raise a TypeError.
try:
    obj.my_method("Only one argument")
except TypeError as e:
    print(f"Error: {e}")

# Demonstration of how python handles this.
print(MyClass.my_method) # This shows that the second definition overwrites the first.
#Write two methods with the same name but different number of parameters of different data type and call the methods
class MyClass:
    def greet(self, *args):
        if len(args) == 2:
            name, age = args
            print(f"Hello, {name}! You are {age} years old.")
        elif len(args) == 1:
            print(f"Hello, {args[0]}!")
        elif len(args) == 0:
            print("Hello!")
        else:
            print("Invalid number of arguments!")

# Create an object of MyClass
obj = MyClass()

# Calling the method with different numbers of parameters
obj.greet("Alice", 30)    # Output: Hello, Alice! You are 30 years old.
obj.greet("Bob")          # Output: Hello, Bob!
obj.greet()               # Output: Hello!
obj.greet("Charlie", 25, "extra")  # Output: Invalid number of arguments!
#Write two methods with the same name and same number of parameters of same type
class MyClass:
    def my_method(self, arg1):
        """First method with one parameter (string)."""
        print(f"First method called: {arg1}")

    def my_method(self, arg1):
        """Second method with one parameter (string)."""
        print(f"Second method called: {arg1}")

# Create an instance of the class
obj = MyClass()

# Call the method
obj.my_method("Hello")

#Demonstration of how python handles this.
print(MyClass.my_method) #This shows that the second definition overwrites the first.
