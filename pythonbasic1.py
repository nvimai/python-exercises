# Bython Basic 1


# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# print ("Twinkle, twinkle, little star,\n    How I wonder what you are!\n        Up above the world so high,\n       Like a diamond in the sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are")

# 2. Write a Python program to get the Python version you are using. 
# import platform
# print (platform.python_version())

#3. Write a Python program to display the current date and time.

# import datetime
# now=datetime.datetime.now()
# print ("current date and time: ")
# print (now.strftime('%Y-%m-%d %I:%M %p'))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# import math
# radiusString = input("Type in the radius:")
# radius = int(radiusString)
# def circleArea(radius):
#     return math.pi * radius**2

# area = circleArea(radius)

# print("r = {0}\n area = {1}".format(radius, area))


# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 

# fullName = input ("What is your name?:")
# print (fullName[::-1])

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
y = int(input("Input the year:"))
m = int(input("Input the month:"))
print(calendar.month(y,m))

# 8. Write a Python program to display the first and last colors (First and last elements) from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

# 113. Write a Python function to input a number, if it is not a number generate an error message, or is positive, negative or zero. 

# 48. Write a Python function to parse a string to Float or Integer. Name the function as "string2Float" and "string2Int"

# 34. Write a Python function to sum of two given (input) integers. However, if the sum is between 15 to 20 it will return 20. 

# 65. Write a Python function to convert seconds to day, hour, minutes and seconds. Function name "seconds2Datetime"

# 91. Write a Python function to swap two variables. Function name "swap2Vars"

# 138. Write a Python function to convert true to 1 and false to 0. 

##### Bonus:
# 58. Write a python function to find the sum of the first n positive integers. 

# 99. Write a Python function to clear the screen or terminal. 
