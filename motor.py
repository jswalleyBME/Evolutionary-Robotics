
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c



class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName

        self.amplitude = c.amplitude_front
        self.frequency = c.frequency_front
        self.phaseOffset = c.phaseOffset_front  ## chnage constants file eventually 
        print(self.jointName)
        
        #print(self.values)


    def Prepare_to_act(self, n):

        amplitude = c.amplitude_front
        frequency = (1/2)*c.frequency_front
        phaseOffset = c.phaseOffset_front

        if self.jointName ==  b'Torso_BackLeg':
            self.motorValues = amplitude*np.sin(frequency * n + phaseOffset)
        else:
            self.motorValues = self.amplitude*np.sin(self.frequency * n + self.phaseOffset)



    def Set_Value(self, robotID, n):

        self.Prepare_to_act(n)

        pyrosim.Set_Motor_For_Joint( bodyIndex = robotID, jointName = self.jointName, controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues, maxForce = 500)
    
