# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 

# def evenOrOdd(x):
#     if x % 2 == 0:
#         print ("This number is an even number")
#     else:
#         print("This number is an odd number")

# x = int(input ("Type a number: "))

# evenOrOdd(x)

# aString = "Today is a nice day"

# print("Nice" not in aString)

# Write a ternary operator: if someone's age is higher than 18 then he can buy alcohol else he cannot buy one

age = int(input("What is your age?: "))
age = 18
if age > 18:
    print ("Can buy alcohol")
else:
    print("Cannot buy alcohol")

age = 18
if age > 18:
    print ("Can buy alcohol")
elif age == 18:
    print ("Show the id")
else:
    print("Cannot buy alcohol")

able = "Can buy alcohol" if age > 18 else "Cannot buy alcohol"

# <variable> = <Result1> if <statement> else <Result2>
print(able)


