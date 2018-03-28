# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 19

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from datetime import date, timedelta

def run():
#how many sundays fell on the first of the month between 1 jan 1901 and 31 dec 2000?

    WEEK = timedelta(weeks = 1)
    d = date(1901,1,6)

    numSundays = 0
    while d <= date(2000,12,31):
        if d.day == 1:
            numSundays += 1
        d = d + WEEK
    return numSundays


if __name__ == "__main__":
	print(run())

