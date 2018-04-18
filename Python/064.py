# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import math

def genSeq(S):
    #x=[m,d,a]
    x=[[0, 1, int(math.floor(math.sqrt(S)))]]

    while True:
        temp = [(x[-1][1]*x[-1][2] - x[-1][0])]
        temp.append((S-temp[0]**2)/x[-1][1])
        if temp[1] == 0:
            return 0,0
        temp.append(int(math.floor((x[0][2]+temp[0])/temp[1])))

        if temp not in x:
            x.append(temp)

        else:
            a = []
            for i in x:
                a.append(i[2])
            return a, len(x)-x.index(temp)
def run():

    count = 0
    for i in range(1,10000):
        temp = genSeq(i)
        if temp[1]%2 == 1:
            count +=1
            #print(i,genSeq(i))
    return count


if __name__ == "__main__":
    print(run())

