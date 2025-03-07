# 1. Generate Arithmetic Exception without exception handling
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    n = a % b  
    print(n)
except Exception as e:
    print(f"Error: {e}")  

# 2. Handle the Arithmetic exception using try-except block
try:
    p = int(input("Enter the numerator: "))
    q = int(input("Enter the denominator: "))
    r = p % q
    print(r)
except ZeroDivisionError:
    print("Can't be divided by 0")
except ValueError:
    print("Please enter valid integers.")
          
# 4. Program with multiple catch blocks
def divide(m, n):
    return m / n
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = divide(num1, num2)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 5. Throw exception with your own message
def check_age(ag):
    if ag < 18:
        raise ValueError("Age must be 18 or above to proceed!")
    else:
        print("Access granted.")

try:
    user_ag = int(input("Enter your age: "))
    check_age(user_ag)
except ValueError as e:
    print(f"Error: {e}")

# 6. Create your own exception
class AgeTooLowError(Exception):
    def __init__(self, message="Age must be 18 or above to proceed!"):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise AgeTooLowError()  
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except AgeTooLowError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")

# 7. Program with finally block
def divide(u, v):
    try:
        res = u / v
        print("Result:", res)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Execution completed.")

n1 = int(input("Enter numerator: "))
n2 = int(input("Enter denominator: "))
divide(n1, n2)

# 8. Generate Arithmetic Exception
def generate_arithmetic_exception():
    result = 10 / 0  

try:
    generate_arithmetic_exception()
except ZeroDivisionError as e:
    print(f"Arithmetic Exception Occurred: {e}")

# 9. Generate FileNotFoundError
try:
    t = open('text1.txt', 'r')  
    print(t.read())
except FileNotFoundError as e:  
    print(f'Error: {e}')

# 10. Generate ModuleNotFoundError
try:
    import nonexistent_module  
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundException Occurred: {e}")

# 11. Generate IOError (File I/O Error)
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except OSError as e:  
    print(f"IOException Occurred: {e}")

# 12. Generate AttributeError (NoSuchFieldException in Java equivalent)
class MyClass:
    def __init__(self):  
        self.name = "Shivani"

try:
    obj = MyClass()
    print(obj.non_existent_field)  
except AttributeError as e:
    print(f"NoSuchFieldException Occurred: {e}")


# 3. Write a method which throws an exception, call that method in main class without try block
class MyClass:
    def risky_method(self):
        raise ValueError("Something went wrong!")

def main():
    obj = MyClass()
    obj.risky_method()  

if __name__ == "__main__":
    main()

