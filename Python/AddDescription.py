# -*- coding: utf-8 -*-
"""
Adds the description of the problem at the top of the solutions script

Created on Mon Apr 16 23:48:30 2018

@author: Jaime Liew
"""

import urllib

substitute = {'<p>': '', '</p>': '\n',
              '<var>': '', '</var>': '',
              '<sup>': '^', '</sup>': '',
              '<sub>': '_', '</sub>': '',
              '<i>': '', '</i>': ''}
with urllib.request.urlopen('https://projecteuler.net/problem=19') as response:
   out = response.read().decode()
out = out.split('role="problem">')[1].split('</div><br />')[0]


for key, value in substitute.items():
    out = out.replace(key, value)

print(out)

