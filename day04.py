# string slicing, list basics & list operations in python

# 1. String Slicing in Python
# string[start : end : step]

text = "PythonProgramming"

# result = text[0:6]
# result = text[1:6:2]

# 2. List Basics
numbers = [10,20,30,40,50]

# result = numbers[-1]
# result = numbers[1:3]
# result = numbers[::2]
# result = numbers[0:3:2]

# 3. List Operations

a = [1, 2, 3]
b = [4, 5]

# result = a + b
# result = a * 3
# result = 3 in a
# result = 3 not in a
# result = len(a)

# 4. Important List Methods

nums = [1,2,3]
nums.append(4) # add value at the end 

nums.insert(1,5) # add the value at specific index (index,value)

nums.extend([6,7,8]) # add multiple value at the end

nums.remove(7) # delete an specific value

nums.pop() # delete the last index value

nums.pop(0) # delete the entered index value

nums.clear() # delete all value


# 5. Sorting & Reversing Lists

marks = [45,76,23,18]

# marks.sort() # sort the list and it's origin list

# result = sorted(marks) # sort but without modifing the origin list

marks.reverse()

# 6. Other list methods

set_ofnum = [1,2,3,6,2,7,1,2]

# result = set_ofnum.count(10) # get's the occurrence of the value in the list
# result = set_ofnum.index(2) # find index of the value - the value of first index present in list

# result = set_ofnum.copy()

# Task 1
# Reverse a string using slicing.

value = "PythonProgramming"

result = value[::-1]

# Task 2
# Take a list [5, 10, 15, 20, 25] and print only even numbers using slicing or loop.

num_set = [5, 10, 15, 20, 25]

for num in num_set:
    if num % 2 == 0:
        print(num)

for i in range(len(num_set)):
    if num_set[i] % 2 == 0:
        print(num_set[i])

# Task 3
# Add 100 at index 2 in a list.

num_set.insert(2,100)
