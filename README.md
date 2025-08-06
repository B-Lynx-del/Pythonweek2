# 📘 Week Two Assignment: Python Basics

This assignment introduces foundational list operations in Python. The goal is to understand how to create and manipulate lists using built-in methods and functions.

## 🛠 Learning Objectives

- Create and manage Python lists
- Use methods like `append()`, `insert()`, `extend()`, and `pop()`
- Sort list elements and find specific item indices
- Practice debugging and interpreting list outputs

## 📄 Code Summary

```python
# Create an empty list
my_list = []

# Add elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list with additional values
my_list.extend([50, 60, 70])

# Remove the last element (value 70)
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of element 30
index_of_30 = my_list.index(30)

