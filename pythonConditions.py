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
def schoolGrade(yOfB):
    # Check the age from the yOfB

    # 

#================== end skip =====================



# 3. Write Python program to find the longest word and the length of it from the string1
# Input: 
#   string1: "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
# Output (example):
#   Longest word: reprehenderits
#   Length: 14





# 4. Write Python program to replace string2 by "%%" from string1
# Input: 
#   string1: "Esse cillum quis ullamco est irure ipsum. Adipisicing ex non ullamco ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."
#   string2: given from input. ex:  "ullamco"

# Output: The new string1 after replaced. ex: "Esse cillum quis %% est irure ipsum. Adipisicing ex non %% ipsum reprehenderits consequat sint irure proident nisi et adipisicing ut proident."

# 5. Write Python program to return a right Money Format of a given number
# Input: 4235.254
# Output: $4,235.25

# 6. Write Python program to find the second longest digit of an element from an list.
# Input: ex: [123, 13432, 5452, 125, 67]
# Output: The second longest digit number is '5452', which has 4 digits

# 7. Write Python program to convert a given input to KB in binary
# Input: 1MB
# Output: 1024KB

# 7.2. 
#     a. Convert 8039, 371, 10234 to Binary
#     b. Convert 1010101, 1111101 to Decimal
# ex: 8 = 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 0 * 2^0 => 1000






# =====================
# Raspberry Pi: 
# 8. Based on the lesson 3 and use a press button to change the state when pressing n times:
#   1. Press 1st time to turn on the flowing water light and make the flow running from left to right
#   2. Press 2nd time to change the flow from right to left
#   3. Press 3rd time to turn off the lights

state  : 0 1 2 3 4 5 6
state%3:
if(state % 3 == 0):

elif(state % 3 == 1):

elif(state % 3 == 2):

# 9. Do the Lesson 5: RGBLED