# Done all following questions to have $10

#Write Python functions to draw provided shapes based on the input numbers:

#1. Input: n as an edge of isosceles right-angled triangle
# ex: n = 5
# *
# * *
# * * *
# * * * *
# * * * * *
def rightAngTri():
#ASKS USER FOR INPUT TO DETERMINE HOW MANY ROWS THERE WILL BE.
    num = int(input("Enter the number of rows:"))
#FOR LOOP TO PRINT THE TRIANGLE, CREATES LIST
    for i in range(0,num):
#PRINTS SPACES BEFORE "*" BASED ON THE USER INPUT. (left spacing)
#EXAMPLE IF USER PUTS 4 AS INPUT, NUM 1 IS ASSIGNED TO 0 AND WILL BE SUBTRACTED BY 1 TO GO TO 3 IN THE RANGE/LIST 3 WILL BE THE NUMBER OF SPACES FOR THE FIRST "*".(I THINK)
    #    for j in range(0,num-i-1):
    #        print(end="")
#SAME THING AS BEFORE BUT PUTS SPACES AFTER THE "*" AND PUTS THE "*"'S IN THE TRIANGLE. (right spacing)
#FOR THE AMOUNT OF "*" IT ADDS ONE TO THE LIST NUMBER, SO FOR THE FIRST ONE 1 IS ASSIGNED TO 0, AND IT ADDS 1 TO ZERO, MAKING THE AMOUNT OF STARS 1.
       for j in range(0,i+1):
           print("*",end=" ")
       print()
rightAngTri()

# def rightAng():
#     num = int(input('>'))
#     for i in range(1,num + 1):
#         print('* ' * i)

# rightAng()
#2. Input:  n as an edge of isosceles right-angled triangle
# ex: n = 5
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
def rightAngTri():
    num = int(input("Enter the number of rows:"))
    for i in range(0,num):
       for j in range(0,num-i-1):
           print(end="  ")
       for j in range(0,i+1):
           print(" *",end="")
       print()
rightAngTri()

#3. Input: h as the height of the triangle
# ex: n = 5
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
def rightAngTri():
    num = int(input("Enter the number of rows:"))
    for i in range(0,num):
       for j in range(0,num-i-1):
           print(end="  ")
       for j in range(0,2*i+1):
           print(" *",end="")
       print()
rightAngTri()
#4. Input: h as the height of the triangle
# ex: n = 5
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def upsideTriangle():
    num = int(input("Enter the number of rows:"))
#RANGE STARTS FROM GREATEST TO LEAST.
    for i in range(num-1, 0, -1):
        print(end = ("  " * (num - i)))
        print("* " * (2*i-1))
        # for j in range(2*i, 1, -1):
        #     print("*", end=" ")
        # print()
upsideTriangle()
#5. Input: a, b as the edges of the rectangle
#ex: a = 4, b = 5
# * * * * *
# *       *
# *       *
# * * * * *

def rectangle():
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of col: "))
#while loop to print rectangle
    for i in range(0, row):
        for j in range(col):
            if(i == 0 or i == row - 1 or j == 0 or j == col - 1):
#prints stars and top and bottom spacing between the stars by using "end". 
                print(end= "* ")
#spaces the right column away from the left. 
            else:
                print(end = "  ")
        print()
rectangle()


#6. Building a Guessing Game.
# Guess a random provided number between 0 to 20
# Step1: Get a random number between 0-20
# Step2: A loop that asks user to give the guessing answer
# Step3: Check the answers and print the notes
# Step3.1: If the guessing number is smaller than the right answer print('Greater')
# Step3.2: If the guessing number is greater than the right answer print('Smaller')
# Step3.3: If they are match then print('Competed') and finish the game

import random
tries = 0
num = random.randint(0, 5)
while tries < 3:
    tries = tries + 1
    guess = int(input("Enter a number:"))
    if (guess) < (num):
        print("Greater")
    if (guess) > (num):
        print ("Smaller")
    if (guess) == (num):
        print("Done")
        break

else:
    print("You lost")
