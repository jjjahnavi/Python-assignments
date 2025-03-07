#Creating dictionary
Dict = dict([(1,'Kashish'), (2,'Kritika'), (3,'Aastha'), (4,'Vaishali'), (5,'Muskan')])
print("Dictionary with each item as a pair:",Dict) #printing dictionary

#adding element in dictionary
Dict[6] = 'Nitya'
print("\n Dictionary with new item added:",Dict)

#updating values in dictionary
Dict[3] = 'Navdisha'
print("\n Dictionary with updated values:",Dict)

print("\n Accessing one value in Dictionary:",Dict[1])

#deleting value from drictionary
del Dict[6]
print("\n Delete a value from a Dictionary:",Dict)

#creating a nested dictionary
Dict1 = {1: 'Kashish', 2: 'Kritika',
        3:{'Age' : 18, 'Branch' : 'CSE', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])
