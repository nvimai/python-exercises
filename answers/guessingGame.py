
# Guessing game
# Step1: Provide a key number based on the range
import random
keyNumber = random.randint(0, 10)
limit = 3
count = 0

# Step2: Limit while loop to ask user for input of answers
while count < limit:
  print(f'This is your {count+1} attempt')
  answer = int(input('Type your guess: '))

  # Step3: When user gives a right number, stop the program
  if(answer == keyNumber):
    print('Congrates')
    break
  else:
    # Step4: If user gave the wrong answer, plusing count
    print('The answer was wrong.')
    count += 1

else:
  # Step5: When count equals to limit then stop
  print('You lost')