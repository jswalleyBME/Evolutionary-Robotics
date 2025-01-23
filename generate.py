
import pyrosim.pyrosim as pyrosim
import numpy as np

x = 0
y = 0
z = 0

pyrosim.Start_SDF("box.sdf")

size = [1,1,1]
for x_ in range(0,5):
    for y_ in range(0,5):
        count = 0
        pyrosim.Send_Cube(name="Box", pos=[x+x_,y+y_,z+0.5] , size=[1,1,1])
        count = 1
        for z_ in range(1,10):
            multiplier = 0.9**z_
            pyrosim.Send_Cube(name="Box", pos=[x+x_,y+y_,z+z_+0.5] , size = np.array(size)*multiplier)
    
pyrosim.End()