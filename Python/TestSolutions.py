# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:26:35 2018

@author: J
"""

import importlib, time, os



problems = [i[:3] for i in os.listdir() if len(i) == 6]
totaltime = 0.0  # In seconds
for prob in problems:
    module = importlib.import_module(prob)
    starttime = time.time()
    ans = module.run()  # Must return a string
    elapsedtime = time.time() - starttime
    totaltime += elapsedtime
    print(prob, ans)
#		"" if actualans == expectans else "    *** FAIL ***"))
print("Total computation time: {} ms".format(int(round(totaltime * 1000))))