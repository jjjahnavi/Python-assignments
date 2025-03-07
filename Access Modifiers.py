# Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.Create a sub class and try to access the private fields and methods from sub class.

class MyClass:
    def __init__(self):
        self.__private_field = "This is a private field"  
        self.__private_field2 = "Another private field"  
    def __private_method(self):
        print("This is a private method")
    def main(self):
        print(self.__private_field)
        print(self.__private_field2)
        self.__private_method()
my_object = MyClass()
print("\nCalling main method of MyClass:")
my_object.main()
class SubClass(MyClass):
    def access_private(self):
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field directly from subclass")
        
        try:
            self.__private_method()
        except AttributeError:
            print("Cannot call private method directly from subclass")
print("\nCalling access_private method from SubClass:")
sub_object = SubClass()
sub_object.access_private()

#Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package. Also, Access the PROTECTED fields and methods from child class located in a different package


class MyClass:
    def __init__(self):
        self._protected_field = "This is a protected field"
    def _protected_method(self):
        print("This is a protected method")
    def show(self):
        print(self._protected_field)  
        self._protected_method()      
class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_protected(self):
        print("Accessing protected field in AnotherClass:")
        print(self.obj._protected_field)  
        self.obj._protected_method()      
class SubClass(MyClass):
    def access_protected(self):
        print("\nAccessing protected field in SubClass (different package):")
        print(self._protected_field)  
        self._protected_method()      
class OtherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_protected(self):
        print("\nAccessing protected field in OtherClass (different package):")
        print(self.obj._protected_field) 
        self.obj._protected_method()      
print("Running in the same package:")
another_obj = AnotherClass()
another_obj.access_protected()
print("\nRunning in a subclass from a different package:")
sub_obj = SubClass()
sub_obj.access_protected()
print("\nRunning in a non-subclass from a different package:")
other_obj = OtherClass()
other_obj.access_protected()

#Create a class with PUBLIC fields and methods. Access the public methods and fields from any class in the same package or different package.

class MyClass:
    def __init__(self):
        self.public_field = "This is a public field"  
    def public_method(self):
        print("This is a public method")
    def show(self):
        print(self.public_field)  
        self.public_method()      
class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_public(self):
        print("Accessing public field in AnotherClass:")
        print(self.obj.public_field)  
        self.obj.public_method()      
class SubClass(MyClass):
    def access_public(self):
        print("\nAccessing public field in SubClass (different package):")
        print(self.public_field)  
        self.public_method()      
class OtherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_public(self):
        print("\nAccessing public field in OtherClass (different package):")
        print(self.obj.public_field)  
        self.obj.public_method()      
print("Running in the same package:")
another_obj = AnotherClass()
another_obj.access_public()
print("\nRunning in a subclass from a different package:")
sub_obj = SubClass()
sub_obj.access_public()
print("\nRunning in a non-subclass from a different package:")
other_obj = OtherClass()
other_obj.access_public()


