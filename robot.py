
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c


class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")   

    
    def prepare_to_sense(self):
        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    

    def Sense(self,n):

        for key in self.sensors:
            self.sensors[key].Get_Value(n)


    def Prepare_to_act(self):

        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, n):

        for key in self.motors:
            self.motors[key].Set_Value(self.robotId, n)
