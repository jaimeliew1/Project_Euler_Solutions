# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:13:43 2018

@author: J
"""
import os

searchTerm = 'gcd'

problems = [i for i in os.listdir() if len(i) == 6]

for prob in problems:
    f = open(prob)
    content = f.read()
    if searchTerm in content:
        print('\n\n\n', prob)
        print(content)
