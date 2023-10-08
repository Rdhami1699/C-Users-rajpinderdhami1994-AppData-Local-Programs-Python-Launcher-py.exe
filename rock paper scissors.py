import random

def play():

    user = input(f"'r' for rock, 'p' for paper, 's' for scissors,What would you choose??\n")

    computer = random.choice(['r','p','s'])
    while user != computer:
       
      if iswin(user, computer):
        return "you won"
      return "you lost!Good luck next time"
    return "it's a tie"
def iswin(player, opponent):

   if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
       return True
    
print(play())
