#if / elif / else, comparison operators in Python

a = 10
b = 10

print(a == b)       #Equal to
print(a != b)       #Not equal to
print(a > b)        #Greater than
print(a < b)        #Less than
print(a >= b)       #Greater than or equal to
print(a <= b)       #Less than or equal to

if(a > b):
    print("A is Greater")
elif(a == b):
    print("A is equal to B")
else:
    print("B is Greater")


#Practice Session

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

user_password = "1234"
password = input("Enter your password: ")

if user_password == password:
    print("Login Successfull")
else:
    print("Login Failed")

#Operatoer and, or & not

user_id = input("Enter user id: ")
user_password = input("Enter user password: ")

if user_id == "admin" and user_password == "1234":
    print("validation pass")
elif user_id == "admin" or user_password == "1234":
    print("Entered user id or password is wrong")
else:
    print("validation failed")

mark = int(input("Enter your total mark: "))

if mark > 90:
    print("A Grade")
elif mark >= 60 and mark <= 90:
    print("B Grade")
else:
    print("C Grade")


#Task 1

age = int(input("Enter your age: "))
country = input("Enter your country: ").lower()

if age >= 18 and country == "india":
    print("Eligible")
else:
    print("Not Eligible")


#Task 2

user_input = int(input("Enter your number: "))

if user_input % 3 == 0 or user_input % 5 == 0:
    print("Divisible by 3 or 5")
else:
    print("Not Divisible by 3 or 5")