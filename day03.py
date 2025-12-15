#for loops, while loops, break & continue in Python

#for i in range(1, 7):
#    print(i)

# pets = ['dog', 'cat', 'parrot']

#for i in pets:
#    print(i)

#i = 1
#while i <= 5:
#    print(i)
#    i += 1

#for i in range(1,6):
#    if i == 4:
#        break
#    print(i)


# for i in pets:
#     if i == 'dog':
#         continue
#     print(i)


#Task 1

# for i in range(1, 21):
#     if i % 2 != 0:
#         continue
#     print(i)

#Task 2

# i = 1
# user_input = int(input("Enter a Number: "))
# while i <= 10:
#     print( user_input, " X ", i, " = ", i * user_input)
#     i += 1

#Task 3

# for i in range(1,20):
#     user_data = input("Enter script! ")
#     if user_data.lower() == "exit":
#         break

    #correction
while True:
    user_data = input("Enter script! ")
    if user_data.lower() == "exit":
        break