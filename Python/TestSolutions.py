"""
Created on Sun Mar 25 18:26:35 2018

@author: J
"""

import importlib
import time
from pathlib import Path


this_dir = Path(__file__).parent

for prob in this_dir.glob("*.py"):
    try:
        prob_mod = prob.stem
        int(prob_mod)
    except:
        continue

    module = importlib.import_module(prob_mod)
    starttime = time.time()
    ans = module.run()
    elapsedtime = time.time() - starttime
    print(f"{prob} answer: {ans} ({elapsedtime:2.8f}s)")
