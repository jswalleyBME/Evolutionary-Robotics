
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, link_name):

        self.linkName = link_name
        self.values = np.zeros(1000)
        #print(self.values)

        

    def Get_Value(self,n):
        
       self.values[n] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    

