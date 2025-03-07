#Define a static variable and access that through a class
class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value 
print(MyClass.static_var)
obj = MyClass("Instance Value")
print(obj.static_var) 
MyClass.static_var = "New static value"
print(obj.static_var) 
obj.static_var = "Changed from instance"
print(obj.static_var)  
print(MyClass.static_var)  
#Define a static variable and access that through a instance
class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value  
obj = MyClass("Instance Value")
print(obj.static_var)  
#Define a static variable and change within the instance
class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value  
    def modify_static(self, new_value):
        MyClass.static_var = new_value
obj1 = MyClass("Instance 1")
obj1.modify_static("Changed from instance")
obj2 = MyClass("Instance 2")
print(obj1.static_var)  
print(obj2.static_var)  
print(MyClass.static_var)  
#Define a static variable and change within the class
class MyClass:
    static_var = "I am a static variable"
    @classmethod
    def modify_static(cls, new_value):
        cls.static_var = new_value
print(MyClass.static_var)  
MyClass.modify_static("Changed within class")
print(MyClass.static_var)
obj1 = MyClass()
obj2 = MyClass()
print(obj1.static_var)  
print(obj2.static_var)
