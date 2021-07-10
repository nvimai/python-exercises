# Bython Basic 2 40k

# 1. Write a Python function which accepts the user's first and last name and print them in reverse order with a space between them. 
# def printName(fullName):
#     try:
#         firstLastName = fullName.split(" ")
#         firstName = firstLastName[0]
#         lastName = firstLastName[-1]
#         firstLastName.reverse()
#         print(f'Your name is {lastName} {firstName}')
#         print(f'Your name is {" ".join(firstLastName)}')
#     except Exception as e:
#         print(e)

# def inputName():
#     try:
#         print('Hi there')
#         printName(input('Type your first name and last name: '))
#         print('Bye')
#     except Exception as e:
#         print("Something went wrong")
#         print(e)

# inputName()
# 2. Write a Python function to input a number, if it is not a number generate an error message, or is positive, negative or zero. 
# def num(number):

#     if number > 0:
#         print('Positive number')
#     elif number < 0:
#         print('Negative number')
#     else:
#         print('Zero')

# try:
#     num(float(input('Type a number: ')))
# except Exception as e:
#     print("Something went wrong")
# # 3. Write a Python function to parse a string to Float or Integer. Name the function as "string2Float" and "string2Int"
# def parse(string2Float, string2Int):
#     print(int(string2Float))
#     print(string2Int)


# print(parse(4124.132, -1))
# 4. Write a Python function to sum of two given (input) integers. However, if the sum is between 15 to 20 it will return 20. 
# def sum(x, y):

#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
# try:
#     print(sum(int(input('x: ')), int(input('y: '))))
#     print(sum(int(input('x: ')), int(input('y: '))))
#     print(sum(int(input('x: ')), int(input('y: '))))
#     print(sum(int(input('x: ')), int(input('y: '))))
# except Exception as e:
#     print("Something went wrong")
#  5. Write a Python function to convert seconds to day, hour, minutes. Function name "seconds2Datetime"
# def seconds2Datetime(seconds):

#     secondsInDay = 60 * 60 * 24
#     secondsInHour = 60 * 60
#     secondsInMinute = 60
#     _seconds = seconds - secondsInDay
#     days = seconds // secondsInDay
#     hours = (seconds - (days * secondsInDay)) // secondsInHour
#     minutes = (seconds - (days * secondsInDay) - (hours * secondsInHour)) // secondsInMinute
#     _seconds = (seconds - (days * secondsInDay) - (hours * secondsInHour)) - (minutes * secondsInMinute) // _seconds
#     print(f"D:H:M:S -> {days}:{hours}:{minutes}:{_seconds}")

# try:
#     seconds2Datetime(int(input("Type time in seconds: ")))
# except Exception as e:
#     print("Something went wrong")
# 6. Write a Python function to swap two variables. Function name "swap2Vars"
a = 5
b = 6
a, b = b, a
print(a)
# def swap2Vars(num1, num2):
#      print('Value of num1 before swapping: ', num1)
#      print('Value of num2 before swapping: ', num2)
#      print(f'Value of num1 after swapping: {num2}')
#      print(f'Value of num2 after swapping: {num1}')
# try:
#     swap2Vars(int(input('Type first number: ')), int(input('Type second number: ')))  
# except Exception as e:
#     print("Something went wrong")  
# 7. Write a Python function to convert true to 1 and false to 0. 
# def trueOrFalse(x):
 
#     if x.lower() == 'true':
#         print(1)
#     else:
#         print(0)
# try:
#     trueOrFalse(input('true or false: '))
# except Exception as e:
#     print("Something went wrong")
# # 8. Write a Python function to clear the screen or terminal.
# import os
# import time
# def clear():
#     os.system("ls")
#     time.sleep(0)
#     os.system('clear')

# clear()

# 9. Write a Python function to return the appearance of a specified element in an array
# def appearance(numberCount, array):

#     count = array.count(numberCount)
#     s = 's' if count > 1 else ''
#     print(f'This number appears {count} time{s}')
# try:
#     appearance(int(input('Type number you want to count: ')), [5, 3, 2, 5, 4, 6, 3, 3, 3])
# except Exception as e:
#     print('Some thing went wrong')
# # 10. Write a Python function to sort a dictionary on value 
# def sort(dictionary):

#     allValues = dictionary.values()
#     sort = sorted(allValues)
#     return sort
    
# sort({1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50})
# # 11. Write a Python function to sum all the items' value from a dictionary
# def total(dictionary):

#     allValue = dictionary.values()
#     total = sum(allValue)
#     return total
    
# total({1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50})
# # 12. Write a Python function to get the maximum and minimum value in a dictionary
# def maxAndMin(dictionary):

#     allValue = dictionary.values()
#     print(max(allValue))
#     print(min(allValue))

# maxAndMin(dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50})
# 13. Write a Python function to merge 2 dictionaries
# def merge(d1,d2):

#     d1.update(d2)
#     return d1
# merge({'a': 100, 'b': 200}, {'x': 300, 'y': 200})
# 14. Write a Python function to multiply all the items' value with 2 in a dictionary
# def multiplyBy2(dictionary, numberToMultiply):

#     allValue = dictionary.values()
#     for item in allValue:
#         print(item * numberToMultiply)

# multiplyBy2({1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}, 2)