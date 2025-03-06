# function for arithmetic operators(+,-,*,/)
def arithmetic(a, b):
    print("Addition:", a + b)      
    print("Subtraction:", a - b)   
    print("Multiplication:", a * b) 
    print("Division:", a / b)       
n1 = 10
n2 = 5
arithmetic(n1, n2)

# method for increment and decrement operators(++, --)
def incrementdecrement():
    num = 5 
    num += 1  
    print("After Increment:", num)
    num -= 1  
    print("After Decrement:", num)
incrementdecrement()

# program to find the two numbers equal or not.
n1=int(input("enter the number"))
n2=int(input("enter the number"))
if n1==n2:
    print("equal")
else:
    print("not equal")


# Program for relational operators (<,<==, >, >==)
def relational(a,b):
    print("a<b:",a<b)
    print("a>b:",a>b)
    print("a<=b:",a<=b)
    print("a>=b:",a>=b)
n1=int(input("enter a number"))
n2=int(input("enter a number"))
relational(n1,n2)


#. Print the smaller and larger number
def smallerlarger(a, b):
    if a < b:
        print("Smaller number:", a)
        print("Larger number:", b)
    elif a > b:
        print("Smaller number:", b)
        print("Larger number:", a)
    else:
        print("Both numbers are equal.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

smallerlarger(num1, num2)




