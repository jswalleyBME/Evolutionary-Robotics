
# evolutionary robotics HW1
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import random as r

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())  # location of .urdf
p.setGravity(0,0,-9.8)                                  # gravity
planeId = p.loadURDF("plane.urdf")                      # set floor 
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")                                    


count = 0
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

amplitude_front = np.pi/6
frequency_front = 10/100
phaseOffset_front = 0

amplitude_back = np.pi/4
frequency_back = 5/100
phaseOffset_back = np.pi/6

x = np.arange(0,1000)

#np.savetxt("data/sin_wave", motor_sin)

pyrosim.Prepare_To_Simulate(robotId)
for n in range(1000):

    # step simulation and time delay 
    p.stepSimulation()
    
    backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    motor_command_front = amplitude_front*np.sin(frequency_front * n + phaseOffset_front)
    motor_command_back = amplitude_back*np.sin(frequency_back * n + phaseOffset_back)

    pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b"Torso_BackLeg", controlMode = p.POSITION_CONTROL,
    targetPosition = motor_command_back, maxForce = 500)
    pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b"Torso_FrontLeg", controlMode = p.POSITION_CONTROL,
    targetPosition = motor_command_front, maxForce = 500)

    time.sleep(1/160)
    count+=1

np.save("data/back_leg_sensor", backLegSensorValues)
np.save("data/front_leg_sensor", frontLegSensorValues)

p.disconnect()