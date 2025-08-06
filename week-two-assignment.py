# Week Two Assignment: Python Basics
# empty list creation
my_list =[]
# adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# printing the list
print("The list is:", my_list)

# insert an element at the second position
my_list.insert(1, 15)

# printing the updated list
print("The updated list is:", my_list)

# extend the list with another list
my_list.extend([50, 60, 70])

# printing the extended list
print("The extended list is:", my_list)

# remove last element from the list
my_list.pop()

# printing the list after removing the last element
print("The list after removing the last element is:", my_list)

# sort the list in ascending order
my_list.sort()

# printing the sorted list
print("The sorted list is:", my_list)

# find the index of element 30
index_of_30 = my_list.index(30)

# printing the index of element 30
print("The index of element 30 is:", index_of_30)


