# Tuples, Sets & Dict in python

# Tuples

person = ("Nitin", 28, "Developer", "Nitin", ["1",2,3])

# print(person[4])

# Why use tuple?
# 1. Data should not change
# 2. Faster than lists
# 3. Used for fixed records (coordinates, DB rows)


# Set

number = {1,2,3,4,5,6}

# print(number)

a = {1,2,3}
b = {3,4,5,6}

# print( a | b) # Union
# print( a & b) # Intersection
# print( a - b) # Difference

# Why use set?
# 1. Remove duplicates
# 2. Membership testing is very fast
# 3. Mathematical operations

# Dictionary (Dict)

user = {
    "name": "Nitin",
    "age": 27,
    "role": "Web Developer"
}

user["age"] = 28         # Update
user["city"] = "Mumbai"  # Add

# print(user)

print(user.keys())
print(user.values())
print(user.items())

# Why use dict?
# 1. Structured data
# 2. Fast lookup using keys
# 3. Widely used in APIs & JSON