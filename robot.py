
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time


class ROBOT:

    def __init__(self, soluton_ID):

        self.robotId = p.loadURDF("body.urdf")   
        self.nn = NEURAL_NETWORK(f"brain{soluton_ID}.nndf")

        os.system(f"del brain{soluton_ID}.nndf")
        

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

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle,n)


        # for key in self.motors:
        #     self.motors[key].Set_Value(self.robotId, n)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, soluton_ID):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # write x to file 
        f = open(f"tmp{soluton_ID}.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp"+str(soluton_ID)+".txt" , "fitness"+str(soluton_ID)+".txt")

        # print(xCoordinateOfLinkZero)
        # exit()

