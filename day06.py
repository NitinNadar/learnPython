# Functions - arguments / return / lambda in python

# What is a Function in Python?

def get_data(value):
    print('this is data:', value)

# get_data("hello")

# Types of Arguments
# 1. Positional Arguments

def add(a, b):
    print(a + b)

# add(2,4)

# 2. Keyword Arguments

# add(b = 3, a = 7)

# 3. Default Arguments

def print_name(name = "Nitin"):
    print("Hello!!", name)

# print_name()
# print_name("Nivedha")


# 4. Variable-Length Arguments

def total(*numbers):
    print(sum(numbers))

# total(1,2,3)

def details(**data):
    print(data)

# details(name="Nitin", age=25)

# Return Statement

def add_num(a,b):
    return a + b

result = add_num(5,3)

# print(result)

# Multiple Return Values

def calc(a,b):
    return a + b, a - b

one, two = calc(5,6)
# print(one, two)