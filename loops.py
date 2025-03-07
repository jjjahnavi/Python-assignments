#program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

#program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i)
    i += 1
#Program to equal operator and not equal operators
a = 5
b = 10
print(a == b)  
print(a != b)

#program to print the odd and even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
#program to print largest number among three numbers       
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

#program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


#program to print 1 to 10 using the do-while loop statement. 
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

#program to find prime number or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


#program to find Armstrong number or not
a=int(input())
t=a
s=0
while(a!=0):
    r=a%10
    s=s+r*r*r
    a=a//10
if (s==t):
    print("given number is armstrong")
else:
    print("given number is not armstrong")
    
    
    


#program to palindrome or not
num = input("Enter a number: ")
rev = ""

for i in range(len(num) - 1, -1, -1):
    rev += num[i]

if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Program to check whether a number is EVEN or ODD using switch
num = int(input("Enter a number: "))
switch = {0: "Even", 1: "Odd"}
print(switch[num % 2])

#Printing gender (Male/Female) program according to given M/F using switch
gender = input("Enter M or F: ").upper()
switch = {"M": "Male", "F": "Female"}
print(switch.get(gender, "Invalid Input"))













