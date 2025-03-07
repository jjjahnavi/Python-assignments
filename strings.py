#1. Different ways of creating an string.

s="Hi"
print(s)
s1='Hello'
print(s1)
s2='''Welcome'''
print(s2)

#2. Concatnate two strings.

s1='Hi'
s2='Hello'
print(s1+s2)

#3. Finding length of a string

s=input('Enter a string:')
c=0
for i in s:
    c+=1
print(c)


#4. Extract a string using substring.

s='Hello World'
sb=s[6:12]
print(sb)

#5. Searching a string using index.

s=input('Enter a string:')
m=int(input('Enter index:'))
print(s[m])

#6. Matching a String using matches().

import re
s1 =input('Enter first string')  
s2 =input('Enter second string')
matches =re.findall(s1,s2)
if matches:
    print("Matches found:", matches)
else:
    print("No matches found.")

#7. Comparing two strings.

s1=input('Enter first string:')
s2=input('Enter second string:')
if s1==s2:
    print('Same strings')
else:
    print('Different strings')

#8. startsWith(), endsWith() and compareTo()
s=input('Enter a string:')
print(s.startswith('j'),s.endswith('i'))
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if str1 == str2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")
#9. Trimming strings with strip()
str7 = 'Hello World hi'
print(str7.strip("hi"))
print()

#10.Replacing with a character.

s=input('Enter a string:')
m=input('Enter a character to replace:')
n=input('Enter a new character:')
k=s.replace(m,n)
print(k)

#11.Splitting strings with split()
str9 = 'basic programs python'
print(str9.split("-"))
print()

#12.Converting integer objects to Strings
numb = 10
numb1 = str(numb)
print(numb1)
print(type(numb1))

#13.Converting to uppercase and lowercase
string = 'python'
string1 = 'JAVA'
print(string.upper())
print(string1.lower())




















