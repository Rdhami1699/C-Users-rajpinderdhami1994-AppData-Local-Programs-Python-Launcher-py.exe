import random
def computerguess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
      computerguess = random.randint(low,high)
      feedback = input(f" Is this the {computerguess} too high(h), too low(l)or correct(c)????")
      if feedback == 'h':
          high = computerguess - 1
      elif feedback == 'l':
          low = computerguess + 1
          
    print(f"yay! you got it")
computerguess(10)



    
    
    
