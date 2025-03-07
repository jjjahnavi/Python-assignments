#a class with a default constructor, one argument constructor and two argument contructors.Instantiate the class to call all the constructors of that class from a main class

class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called.")
        elif arg2 is None:
            print(f"One argument constructor called with arg1: {arg1}")
            self.arg1 = arg1
        else:
            print(f"Two argument constructor called with arg1: {arg1} and arg2: {arg2}")
            self.arg1 = arg1
            self.arg2 = arg2

class MainClass:
     def __init__(self):
        self.default_instance = MyClass()
        self.one_arg_instance = MyClass("Hello")
        self.two_arg_instance = MyClass("Hello", 123)

# Instantiate the MainClass to call the constructors
main_instance = MainClass()

#Call the constructors(both default and argument constructors) of super class from a child class
class SuperClass:
    def __init__(self, arg=None):
        if arg is None:
            print("SuperClass: Default constructor called.")
        else:
            print(f"SuperClass: Argument constructor called with arg: {arg}")
            self.arg = arg

class ChildClass(SuperClass):
    def __init__(self, child_arg=None, super_arg=None):

        if super_arg is None:
            super().__init__()  # Call superclass default constructor
        else:
            super().__init__(super_arg)  # Call superclass argument constructor

        if child_arg is None:
            print("ChildClass: Default constructor called.")
        else:
            print(f"ChildClass: Argument constructor called with child_arg: {child_arg}")
            self.child_arg = child_arg

# Example usage:

# Call superclass default constructor from child class
child1 = ChildClass()

# Call superclass argument constructor from child class
child2 = ChildClass(child_arg="Child Value", super_arg="Super Value")

#Call child class argument constructor, but super class default constructor.
child3 = ChildClass(child_arg="Child value only")
#Apply private, public, protected and default access modifiers to the constructor
class MyClass:
    def __init__(self, public_arg, protected_arg, private_arg):
        """Constructor with public, protected, and private attributes."""
        self.public_attribute = public_arg  # Public attribute
        self._protected_attribute = protected_arg  # Protected attribute
        self.__private_attribute = private_arg  # Private attribute
        print("Constructor called.")

    def public_method(self):
        print(f"Public method called. Public attribute: {self.public_attribute}")

    def _protected_method(self):
        print(f"Protected method called. Protected attribute: {self._protected_attribute}")

    def __private_method(self):
        print(f"Private method called. Private attribute: {self.__private_attribute}")

# Create an instance of the class
obj = MyClass("Public Value", "Protected Value", "Private Value")

# Access public members
obj.public_method()
print(f"Public attribute: {obj.public_attribute}")

# Access protected members (not recommended outside the class/subclasses)
obj._protected_method()
print(f"Protected attribute: {obj._protected_attribute}")

# Access private members (using name mangling)
obj._MyClass__private_method()
print(f"Private attribute: {obj._MyClass__private_attribute}")

# Attempting to access private members directly will raise an AttributeError:
# obj.__private_method()
# print(obj.__private_attribute)

# Example Subclass demonstrating protected access.
class SubClass(MyClass):
    def __init__(self, public_arg, protected_arg, private_arg, subclass_arg):
        super().__init__(public_arg, protected_arg, private_arg)
        self.subclass_arg = subclass_arg

    def access_protected(self):
        print(f"Subclass Protected attribute: {self._protected_attribute}")
        self._protected_method()

sub_obj = SubClass("Public Value", "Protected Value", "Private Value", "Subclass Value")
sub_obj.access_protected()
#Write a program which illustrates the concept of attributes of a constructor.
class Car:

    def __init__(self, make, model, year, color="unknown"):
        self.make = make  # Attribute: Make of the car
        self.model = model  # Attribute: Model of the car
        self.year = year  # Attribute: Year of the car
        self.color = color  # Attribute: Color of the car

        print(f"A {self.color} {self.year} {self.make} {self.model} has been created.")

    def display_car_info(self):
        print(f"Car Information:")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year: {self.year}")
        print(f"  Color: {self.color}")

# Example Usage:

# Creating Car objects using the constructor
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Civic", 2021)  # Color defaults to "unknown"
car3 = Car("Tesla", "Model S", 2023, "Red")

# Accessing attributes directly
print(f"\nCar1 Make: {car1.make}")
print(f"Car2 Year: {car2.year}")
print(f"Car3 Color: {car3.color}")

# Calling a method that uses attributes
print("\n")
car1.display_car_info()
print("\n")
car2.display_car_info()
print("\n")
car3.display_car_info()

#Demonstrating that attributes are instance specific.
car1.color = "Silver"
print("\nCar1 color changed.")
car1.display_car_info()
print("\nCar2 display info, to show no change.")
car2.display_car_info()
