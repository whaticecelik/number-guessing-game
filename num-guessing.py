# number guessing game
import random
print("Welcome to the number guessing game.")
print("please select the level! ")
level = str(input("'e' for easy, 'm' for middle, 'h' for hard: "))
num = int(input("enter a number between 1 to 10: "))

level = level.lower()
if level == 'e':
  random_num = random.randint(1, 10)
  if num == random_num:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You won!")
  else:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You lose")
elif level == 'm':
  random_num = random.randint(1, 30)
  if num == random_num:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You won!")
  else:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You lose")
elif  level == 'h':
  random_num = random.randint(1, 50)
  if num == random_num:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You won!")
  else:
    print("computer choose "+ str(random_num)+ " you chose "+ str(num)+ " .You lose")

  


