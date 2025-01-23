
# evolutionary robotics HW1
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())  # location of .urdf
p.setGravity(0,0,-9.8)                                  # gravity
planeId = p.loadURDF("plane.urdf")                      # set floor 
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")                                    


count = 0
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)
for n in range(1000):

    # step simulation and time delay 
    p.stepSimulation()
    
    backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    time.sleep(1/60)
    count+=1
np.save("data/back_leg_sensor", backLegSensorValues)
np.save("data/front_leg_sensor", frontLegSensorValues)

p.disconnect()