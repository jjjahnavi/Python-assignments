# program to print name
n=input("enter your name")
print(n)

# Write a program for a Single line comment and multi-line comments
print("# This is a single-line comment")
print('''"""This is a multi-line comment"""''')

#Defining variables for different Data Types int, Boolean, char, float, double.
a=3
b='TRUE'
c=3.5
d='A'
e=35.6763878
print("integer =",a,"boolean =",b,"float =",c,"character =",d,"double=",e)

#Defining the local and Global variables with the same name and print both variables and understand the scope of the variable
x=10
def number():
    x=60
    print("local variable value:",x)
number()
print("global variable value:",x)
