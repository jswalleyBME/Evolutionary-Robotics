
import pyrosim.pyrosim as pyrosim
import numpy as np

x = 0
y = 0
z = 0

def Create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-2,2,z+0.5] , size=[1,1,1])
    pyrosim.End()

def Create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,1+0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_front_leg" , parent= "Torso" , child = "front_leg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="front_leg", pos=[0.5,0,-0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_back_leg" , parent= "Torso" , child = "back_leg" , type = "revolute", position = [-0.5,0,1])
    pyrosim.Send_Cube(name="back_leg", pos=[-0.5,0,-0.5] , size=[1,1,1])

    

    pyrosim.End()

Create_world()
Create_robot()

