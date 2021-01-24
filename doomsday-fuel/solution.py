import numpy as np
from fractions import Fraction

def lcm(x, y): # Function for finding the lowest common factor between two numbers
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def solution(m):
    if len(m) < 2:
        return [1,1]
    # If The length of m is less than 2, the probability is 100%.
    n = np.array(m)
    n = n.astype(float)
    ntmi = [i for i in range(len(n)) if any(j!=0 for j in n[i])] # Every non-terminal state
    tmi = [i for i in range(len(n)) if all(j==0 for j in n[i])] # Every terminal state
    ans = []
    denoms = [] # Denominators for probability of each non - terminal state
    
    for i in tmi:
         n[i, i] = 1 # Gives each terminal state a 100% chance of becoming itself in the next stage.
    for i in range(len(n)):
        x = sum(n[i])
        for j in range(len(n[i])):
            n[i, j]/=x
    Q = np.array([[n[i, j] for j in ntmi] for i in ntmi]) # The chances of a non-terminal state becoming a non-terminal state
    R = np.array([[n[i, j] for j in tmi] for i in ntmi]) # The chances of a non-terminal state becoming a terminal state
    a, b = np.shape(Q)
    I = np.identity(a) # The chances of a terminal state becoming a terminal state
    F = np.linalg.inv(I-Q)
    FR = np.dot(F, R) # The final possibilities of a non-terminal state becoming a terminal state
    for j in range(len(FR[0])):
        f = Fraction(FR[0, j]).limit_denominator() # Turns each item in FR into a fraction (kind of)
        ans.append(f.numerator)
        denoms.append(f.denominator)
    lcd = 1
    for denom in denoms:
        lcd = lcm(lcd, denom)
    # Finds lowest common denominator out of the denominators of every posibility fraction
    for j_in in range(len(FR[0])):
        ans[j_in] *= int(lcd/denoms[j_in])
    # Changes all the numerators to fit the new common denominator
    ans.append(lcd) # Appends the lowest common denominator
    return ans
# I found this quite confusing myself just to edit, so don't worry if you get confused.
# To make better sense of this, I recommend going here: https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
