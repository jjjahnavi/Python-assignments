class A:
    def __init__(self):
        self.valueA = 10  

    def methodA1(self):
        print("Method A1: Specific to Class A")

    def methodA2(self):
        print("Method A2: Specific to Class A")

    def overridden_method(self):  
        print("Overridden Method in Class A")


# Subclass B (Inherits from A)
class B(A):
    def __init__(self):
        super().__init__()  
        self.valueB = 20

    def methodB1(self):
        print("Method B1: Specific to Class B")

    def methodB2(self):
        print("Method B2: Specific to Class B")

    def overridden_method(self):
        print("Overridden Method in Class B")


# Subclass C (Inherits from B)
class C(B):
    def __init__(self):
        super().__init__()  
        self.valueC = 30  

    def methodC1(self):
        print("Method C1: Specific to Class C")

    def methodC2(self):
        print("Method C2: Specific to Class C")

    def overridden_method(self):
        print("Overridden Method in Class C")


# Main function
def main():
    
    objA = A()
    objB = B()
    objC = C()

    
    print("Calling methods using object of A:")
    objA.methodA1()
    objA.methodA2()
    objA.overridden_method()

    print("\nCalling methods using object of B:")
    objB.methodA1()
    objB.methodA2()
    objB.methodB1()
    objB.methodB2()
    objB.overridden_method()

    print("\nCalling methods using object of C:")
    objC.methodA1()
    objC.methodA2()
    objC.methodB1()
    objC.methodB2()
    objC.methodC1()
    objC.methodC2()
    objC.overridden_method()

   
    print("\nRuntime Polymorphism - Overridden Method Calls:")
    ref1 = B()  
    ref2 = C()
    ref1.overridden_method()  
    ref2.overridden_method()  
    
    print("\nRuntime Polymorphism with Instance Variables:")
    ref1_as_A = A()  
    ref2_as_A = A()  

    print("Value of valueA using ref1 (A -> B):", ref1_as_A.valueA)
    print("Value of valueA using ref2 (A -> C):", ref2_as_A.valueA)

    
    print("Value of valueB using objB:", objB.valueB)
    print("Value of valueC using objC:", objC.valueC)



if __name__ == "__main__":
    main()
