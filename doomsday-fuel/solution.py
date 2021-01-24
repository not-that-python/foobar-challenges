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
    n = np.array(m)
    n = n.astype(float)
    ntmi = [i for i in range(len(n)) if any(j!=0 for j in n[i])]
    tmi = [i for i in range(len(n)) if all(j==0 for j in n[i])]
    ans = []
    denoms = []
    
    for i in tmi:
         n[i, i] = 1
    for i in range(len(n)):
        x = sum(n[i])
        for j in range(len(n[i])):
            n[i, j]/=x
    Q = np.array([[n[i,j] for j in ntmi] for i in ntmi])
    R = np.array([[n[i, j] for j in tmi] for i in ntmi])
    a, b = np.shape(Q)
    I = np.identity(a)
    F = np.linalg.inv(I-Q)
    FR = np.dot(F, R)
    for j in range(len(FR[0])):
        f = Fraction(FR[0, j]).limit_denominator()
        ans.append(f.numerator)
        denoms.append(f.denominator)
    lcd = 1
    for denom in denoms:
        lcd = lcm(lcd, denom)
    for j_in in range(len(FR[0])):
        ans[j_in] *= int(lcd/denoms[j_in])
    ans.append(lcd)
    return ans
