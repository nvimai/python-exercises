# Finish 1 to 7 to have $7; 8 and 9 to have $8

# 1. Write Python program to check a given list is empty or not. If not then return the length of that list 
# def checkList(aList):
# # a list of number
#     if not aList:
#         print("This list is empty")
#         return 0

# # Checks if the list is empty or not.
#     else: 
#         print("This list is not empty")
#         return len(aList)
# # if the list is not empty this will print^^.


# numList = [1, 2, 3, 4]
# print(checkList(numList))
#Function to check and print how long the list is.

#================== skip =====================
# 2. Write Python program to guess the Ontario school grade structures by a year of birth
# Input: 2010
# Output: Grade 5 in Elementary
# def schoolGrade(yOfB):
    # Check the age from the yOfB

    # 

#================== end skip =====================



# 3. Write Python program to find the longest word and the length of it from the string1
# Input: 
#   string1: "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
# Output (example):
#   Longest word: reprehenderits
#   Length: 14

# string1 = "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
# #finds the longest word from string1
# def findLongestWord(string1):

#     longest = max(string1.split(), key=len)
#     #prints the longest word from string1 and its length
#     print ("The longest word is:", longest)
#     print ("Length:", len(longest))

#     return ({ "word": longest, "length": len(longest)})

# longestWord = findLongestWord(string1)

# print(longestWord)

# 4. Write Python program to replace string2 by "%%" from string1
# Input: 
#   string1: "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
#   string2: given from input. ex:  "ullamco"

# Output: The new string1 after replaced. ex: "Esse cillum quis %% est irure ipsum. Adipisicing ex non %% ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."

# string1 = "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."


# Input string1 (source) and string2 (search string)
# def replaceString(sourceString, searchString, replaceString):
#     # replace all the string2 by "%%" in string1
#     newSourceString = sourceString.replace(searchString, replaceString)
#     # return new string1
#     return newSourceString



# string1 = "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
# string2 = "e"
# string3 = "$"
# print(replaceString(string1, string2, string3))







# 5. Write Python program to return a right Money Format of a given number
# Input: 4235.254
# Output: $4,235.25

# def currencyFormat(amount):   
# #.2 tells the print to only print the first 2 digits after the point.  
#     money = "${:,.2f}".format(amount)
# #prints the input in money format.
    
#     return money

# amount = 4235.254
# money = currencyFormat(amount)
# print(money)

# 6. Write Python program to find the second longest digit of an element from an list.
# Input: ex: [123, 13432, 5452, 125, 67]
# Output: The second longest digit number is '5452', which has 4 digits


# list1 = [123, 13432, 5452, 125, 67]
# #sorts the list from shortest to longest
# list1.sort()
# #prints the second last element of the list
# print("The second longest digit is:", list1[-2])

# 7. Write Python program to convert a given input to KB in binary
# Input: 1MB
# Output: 1024KB

#asks for an number
# MB = int(input("Enter a number:"))
# #turns MB into KB
# KB = MB * 1024
# print(KB)
#Function to turn the output into binary
# binaryNumber = ''
# def numToBinary(KB):
#     if KB >= 1:
#         binaryNumber += (KB % 2)
#         return numToBinary(KB // 2)
#     else:
#         return 0
# numToBinary(KB)
# print(binaryNumber)

# numToBinary(KB)

#^^^^^prints the output in binary

# 7.2. 
#     a. Convert 8039, 371, 10234 to Binary
#     b. Convert 1010101, 1111101 to Decimal
# ex: 8 = 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 0 * 2^0 => 1000
# 2 => 10
# 4 => 100
# 5 => 101
# 1 2 4 8 16 32
# 26 = 16 + 8 + 2 = 1*2^4 + 1*2^3 + 0 * 2^2 + 1 * 2^1 +  0 * 2^0  => 11010



#=======================Converting decimal to Binary====================

# 8039:

#ignore remainders
#8039 / 2 = 4019, 4019 / 2 = 2009, 2009 / 2 = etc.

# 1 for odd, 0 for even

# 8039, 4019, 2009, 1004, 502, 251, 125, 62, 31, 15, 7, 3, 1
# 1    , 1   , 1   , 0   ,  0  , 1,   1,  0,  1,  1,  1, 1, 1

#1110011011111
#FLIP AROUND
#ANSWER IS 1 1 1 1 1 0 1 1 0 0 1 1 1


#371: 

#371, 185, 92, 46, 23, 11, 5, 2 ,1
# 1,   1,   0,  0,  1,  1, 1, 0, 1

#ANSWER IS 1 0 1 1 1 0 0 1 1


# 10234

#10234, 5117, 2558, 1279, 639, 319, 159, 79, 39, 19, 9, 4, 2, 1
#  0,    1,     0,    1,   1,   1,    1,  1,  1,  1, 1, 0, 0, 1

#ANSWER IS 1 0 0 1 1 1 1 1 1 1 1 0 1 0


#====================Converting Binary to Decimal=================


# 1010101

# 1, 2, 4, 8, 16, 32, 64


#  1  0   1  0  1  0  1
# 64, 32, 16, 8, 4, 2, 1
#take the numbers that go under 1 in the binary number
# 64, 16, 4, 1
#add the numbers

#ANSWER IS 85

# 1111101

#1, 2, 4, 8, 16, 32, 64

#64, 32, 16, 8, 4, 2, 1

#64, 32, 16, 8, 4, 1

#ANSWER IS 125








#==========decimal to binary=============
#asks for a number and converts it into an int
# num = int(input("Enter a number:"))
# # #function to turn input into binary
# def numToBinary(num):

#     if num >= 1:
#         numToBinary(num // 2)
#         print (num % 2)

# print(numToBinary)

# numToBinary(num)
#prints the output in binary^^^




#===========binary to decimal============


# #asks for a binary number
# bNum = list(input("Input a binary number:"))
# value = 0

# for i in range (len(bNum)):
#     digit  = bNum.pop()
#     if digit == "1":
#         value = value + pow(2, i)
# print("The decimal value of the number is", value)
# prints a binary number











# =====================
# Raspberry Pi: 
# 8. Based on the lesson 3 and use a press button to change the state when pressing n times:
#   1. Press 1st time to turn on the flowing water light and make the flow running from left to right
#   2. Press 2nd time to change the flow from right to left
#   3. Press 3rd time to turn off the lights

# state  : 0 1 2 3 4 5 6
# state%3:
# if(state % 3 == 0):

# elif(state % 3 == 1):

# elif(state % 3 == 2):
