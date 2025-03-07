from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method_1(self):
        return "AbstractClass: Non-abstract method 1"

    def non_abstract_method_2(self):
        return "AbstractClass: Non-abstract method 2"

class ChildClass(AbstractClass):

    def abstract_method(self):
        return "ChildClass: Implementation of abstract_method"

    def call_non_abstract_methods(self):
        return self.non_abstract_method_1(), self.non_abstract_method_2()

# Create an instance of the child class
child_instance = ChildClass()

# Call the method that calls the non-abstract methods
result1, result2 = child_instance.call_non_abstract_methods()

# Print the results
print(result1)
print(result2)
