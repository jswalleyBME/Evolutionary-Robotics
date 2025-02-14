
# search.py

import os
import pyrosim.pyrosim as pyrosim
import numpy as np
import random 
import pybullet as p

for num in range(5):
    os.system("py generate.py")
    os.system("py simulate.py")