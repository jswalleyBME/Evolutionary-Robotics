
# evolutionary robotics 

from simulation import SIMULATION
import sys
import os

directOrGUI = sys.argv[1]
soluton_ID = sys.argv[2]

simulation = SIMULATION(directOrGUI, soluton_ID)
run = simulation.Run()
simulation.Get_Fitness(soluton_ID)
simulation.__del__()



#os.system("py generate.py")

# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import time
# import numpy as np
# import random as r
# import constants as c

# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())  # location of .urdf
# p.setGravity(0,0,-9.8)                                  # gravity
# planeId = p.loadURDF("plane.urdf")                      # set floor 
# robotId = p.loadURDF("body.urdf")   
# p.loadSDF("world.sdf")                                    


# backLegSensorValues = c.backLegSensorValues
# frontLegSensorValues = c.frontLegSensorValues

# amplitude_front = c.amplitude_front
# frequency_front = c.frequency_front
# phaseOffset_front = c.phaseOffset_front

# amplitude_back = c.amplitude_back
# frequency_back = c.frequency_back
# phaseOffset_back = c.phaseOffset_back

# x = c.command_vector

# #np.savetxt("data/sin_wave", motor_sin)

# count = 0
# pyrosim.Prepare_To_Simulate(robotId)
# for n in range(1000):

#     # step simulation and time delay 
#     p.stepSimulation()
    
#     backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     motor_command_front = amplitude_front*np.sin(frequency_front * n + phaseOffset_front)
#     motor_command_back = amplitude_back*np.sin(frequency_back * n + phaseOffset_back)

#     pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b"Torso_BackLeg", controlMode = p.POSITION_CONTROL,
#     targetPosition = motor_command_back, maxForce = 500)
#     pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b"Torso_FrontLeg", controlMode = p.POSITION_CONTROL,
#     targetPosition = motor_command_front, maxForce = 500)

#     time.sleep(1/160)
#     count+=1

# np.save("data/back_leg_sensor", backLegSensorValues)
# np.save("data/front_leg_sensor", frontLegSensorValues)

# p.disconnect()