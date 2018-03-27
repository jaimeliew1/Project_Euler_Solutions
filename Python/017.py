# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 17

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

#finds sum of length of word lengths of numbers from 1 to 1000 inclusive
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','TEN','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


def run():
    Sum = 0

    for i in range(0,10):
        if i == 0:
            for j in tens:
                if j == 'TEN':
                    for k in teens:
                        #print(k)
                        Sum+=len(k)
                else:
                    #print(j)
                    Sum+=len(j)
                    for k in ones:
                        #print(j+k)
                        Sum+=len(j+k)

        else:
            for j in tens:
                if j == 'TEN':
                    for k in teens:
                        #print(ones[i-1] + 'hundredand'+k)
                        Sum+=len(ones[i-1] + 'hundredand'+k)
                else:
                    if j == '':
                        #print(ones[i-1] + 'hundred')
                        Sum+=len(ones[i-1] + 'hundred')
                    else:
                        #print(ones[i-1] + 'hundredand'+j)
                        Sum+=len(ones[i-1] + 'hundredand'+j)
                    for k in ones:
                        #print(ones[i-1] + 'hundredand'+j+k)
                        Sum+=len(ones[i-1] + 'hundredand'+j+k)
    #print('onethouseand')
    Sum+= len('onethousand')

    return Sum


if __name__ == "__main__":
	print(run())

