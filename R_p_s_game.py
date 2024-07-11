#rock paper sissor game
import random

def check(computer,user):
    if ( computer == user):
        return 0
    if(computer == 0 and user == 2):
        return -1
    if(computer == 1 and user == 0):
        return -1
    if(computer == 2 and user == 1):
        return -1
    return 1

# while(True):
computer = random.randint(0,2) 
while(True):
  user = int(input("enter 0 for rock, 1 for paper, 2 for sissor and 9 for exit:\n"))
  if (user == 9):
    break
  score = check(computer,user)
  if(score == 0):
    print("it's a draw")
  elif(score == -1):
    print("You are a loser") 
  else:
    print("you won")
           
  