

import numpy as np

# command vector 
command_vector = np.arange(0,1000)

# front leg parameters
frontLegSensorValues = np.zeros(1000)
amplitude_front = np.pi/6
frequency_front = 10/100
phaseOffset_front = 0

# back leg parameters
backLegSensorValues = np.zeros(1000)
amplitude_back = np.pi/4
frequency_back = 5/100
phaseOffset_back = np.pi/6

# number of generations
numberOfGenerations = 10

# parallelHC 
populationSize = 10

# number sensors and motors 
numSensorNeurons = 4
numMotorNeurons = 4

# cap motor range 
motorJointRange = 0.3