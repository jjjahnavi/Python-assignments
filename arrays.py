# 1)Function to add integer values of an array
def add(n):
    a = []
    s = 0
    for i in range(n):
        k = int(input("Enter a number: "))
        a.append(k)
    for i in a:
        s = s + i
    return s
n = int(input("Enter the number of elements for sum: "))
print("Sum of elements:", add(n))

# 2)Function to calculate the average value of an array of integers
def avg(n):
    a = []
    s = 0
    for i in range(n):
        k = int(input("Enter a number: "))
        a.append(k)
    for i in a:
        s = s + i
    return s // n
n = int(input())
print("Average value:", avg(n))

#3) Program to find the index of an array element
def find_index(n):
    a = []
    for i in range(n):
        k = int(input("Enter a number: "))
        a.append(k)
    m = int(input("Enter the element to find: "))
    if m in a:
        print("Element found at index:", a.index(m))
    else:
        print("Not in array")
n = int(input("Enter the number of elements to find index: "))
find_index(n)

# 4)Function to test if array contains a specific value
def test(n):
    a = []
    for i in range(n):
        k = int(input("Enter a number: "))
        a.append(k)
    m = int(input("Enter the number to test: "))
    if m in a:
        return True
    else:
        return False
n = int(input("Enter the number of elements for test: "))
print("Is element present:", test(n))

# 5)Function to remove a specific element from an array
def remove_element(arr, elem):
    return [x for x in arr if x != elem]
arr = [1, 2, 3, 4, 5]
print("Array after removing 3:", remove_element(arr, 3))

# 6)Function to copy an array to another array
def copy_array(arr):
    return arr.copy()
arr = [1, 2, 3, 4, 5]
new_arr = copy_array(arr)
print("Copied array:", new_arr)

# 7)Function to insert an element at a specific position in the array
def insert_element(arr, elem, pos):
    arr.insert(pos, elem)
    return arr
arr = [1, 2, 3, 4, 5]
print("Array after inserting 10 at index 2:", insert_element(arr, 10, 2))

# 8)Function to find the minimum and maximum value of an array
def find_min_max(arr):
    return min(arr), max(arr)
arr = [1, 2, 3, 4, 5]
min_val, max_val = find_min_max(arr)
print("Minimum value:", min_val, "Maximum value:", max_val)

#9) Function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]
arr = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(arr))


#10) Function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
arr = [1, 2, 3, 4, 5, 2, 3]
print("Duplicate values:", find_duplicates(arr))

#11) Function to find the common values between two arrays
def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print("Common elements:", find_common_elements(arr1, arr2))

#12) Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 3, 4, 5, 5, 4]
print("Array after removing duplicates:", remove_duplicates(arr))

# 13)Write a method to find the second largest number in an array
def find_second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

arr = [1, 2, 3, 4, 5]
print("Second largest number:", find_second_largest(arr))

#14) Write a method to find number of even numbers and odd numbers in an array
def count_even_odd(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

arr = [1, 2, 3, 4, 5]
even, odd = count_even_odd(arr)
print("Even count:", even, "Odd count:", odd)

# 15)Write a function to get the difference of largest and smallest value
def difference_of_largest_and_smallest(arr):
    return max(arr) - min(arr)

arr = [1, 2, 3, 4, 5]
print("Difference between largest and smallest:", difference_of_largest_and_smallest(arr))

#16) Write a method to verify if the array contains two specified elements(12,23)
def contains_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

arr = [12, 23, 34, 45]
print("Contains 12 and 23:", contains_elements(arr, 12, 23))

# 17)Write a program to remove the duplicate elements and return the new array
def remove_duplicates_and_return(arr):
    return list(set(arr))
arr = [12, 12, 34, 45, 45, 67]
print("Array after removing duplicates:", remove_duplicates_and_return(arr))

#18)Write a function to reverse an array of integer values

# Function to reverse an array
def reverse_array(arr):
    return arr[::-1]

# Example usage:
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)
