# Bython Basic 2 40k

# 1. Write a Python function which accepts the user's first and last name and print them in reverse order with a space between them. 
# def Name():
#     fullName = input('Type your first name and last name: ')
#     firstLastName = fullName.split(" ")
#     firstName = firstLastName[0]
#     lastName = firstLastName[1]
#     print(f'Your name is {lastName} {firstName}')

# print('Hi there')
# Name()
# print('Bye')

# 2. Write a Python function to input a number, if it is not a number generate an error message, or is positive, negative or zero. 
# def num():
#     number = float(input('Type a number: '))
#     if number > 0:
#         print('Positive number')
#     elif number < 0:
#         print('Negative number')
#     else:
#         print('Zero')

# num()

# 3. Write a Python function to parse a string to Float or Integer. Name the function as "string2Float" and "string2Int"
def parse(string2Float, string2Int):
    print(int(string2Float))
    print(string2Int)


print(parse(4124.132, 114.31))
# 4. Write a Python function to sum of two given (input) integers. However, if the sum is between 15 to 20 it will return 20. 
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(int(input('x: ')), int(input('y: '))))
# print(sum(int(input('x: ')), int(input('y: '))))
# print(sum(int(input('x: ')), int(input('y: '))))
# print(sum(int(input('x: ')), int(input('y: '))))
# 5. Write a Python function to convert seconds to day, hour, minutes. Function name "seconds2Datetime"
seconds = 86401
secondsInDay = 60 * 60 * 24
secondsInHour = 60 * 60
secondsInMinute = 60

days = seconds // secondsInDay
hours = (seconds - (days * secondsInDay)) // secondsInHour
minutes = (seconds - (days * secondsInDay) - (hours * secondsInHour)) // secondsInMinute
print(f'{days}: {hours}: {minutes}')
# 6. Write a Python function to swap two variables. Function name "swap2Vars"

# 7. Write a Python function to convert true to 1 and false to 0. 

# 8. Write a Python function to clear the screen or terminal.

# 9. Write a Python function to return the appearance of a specified element in an array

# 10. Write a Python function to sort a dictionary on value
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}


# 11. Write a Python function to sum all the items' value from a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}

# 12. Write a Python function to get the maximum and minimum value in a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}

# 13. Write a Python function to merge 2 dictionaries
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}

# 14. Write a Python function to multiply all the items' value with 2 in a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}