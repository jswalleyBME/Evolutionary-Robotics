
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np

from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self):

        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())      # location of .urdf
        p.setGravity(0,0,-9.8)                                      # gravity
        
        self.robot = ROBOT()
        self.world = WORLD()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.prepare_to_sense()
        self.robot.Prepare_to_act()

    def __del__(self):

        p.disconnect()


    def Run(self):

        for n in range(1000):

            p.stepSimulation()
            self.robot.Sense(n)
            self.robot.Think()
            self.robot.Act(n)
            time.sleep(1/100)
            #print(n)

        keys = self.robot.sensors.keys()

        # for key in keys:
        #     print(self.robot.sensors[key].values)



            
    