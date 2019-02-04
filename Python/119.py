# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 119

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

try producing all powers of numbers that are less than some number (1e12?) and 
find all the powers which are equal to their digit power sum. ie, find all powers
for which their digit sum is equal to their root.
"""
   
def run():
    A     = []
    b     = 15
    a_max = 10**b
    
    # maximum base is b*9, corresponding to a=99999... (b 9's) which has a 
    # digit sum of 9 + 9 + 9+ ... = b*9
    for base in range(2, 9*b):
        exp = 0
        while base**exp <= a_max:
            digitsum = sum(int(n) for n in str(base**exp))
            if base == digitsum and base**exp >= 10:
                A.append(base**exp)
            exp += 1
            
    A = sorted(A)
    # for i, a in enumerate(A):
    #     print(i+1, a)
    return A[29]
        

if __name__ == "__main__":
    print(run())
