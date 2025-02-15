
# solution class
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:

    def __init__(self):
        self.weights = 2*np.random.rand(3,2) - 1
        #print(self.weights)
        self.Evaluate()
    
    def Evaluate(self, directOrGUI = "DIRECT"):
        x = 0
        y = 0
        z = 0

        def Create_world():
            pyrosim.Start_SDF("world.sdf")
            pyrosim.Send_Cube(name="Box", pos=[-2,2,z+0.5] , size=[1,1,1])
            pyrosim.End()

        def Create_body():
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=[x,y,1+0.5] , size=[1,1,1])
            pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
            pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
            pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
            pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])

            pyrosim.End()

        def Create_brain():

            pyrosim.Start_NeuralNetwork("brain.nndf")    

            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

            pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
            pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

            # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
            # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1.0 )
            
            # fully connected NN
            sensor_names = [0, 1, 2]
            motor_names = [0, 1]

            for currentRow in sensor_names:
                for currentColumn in motor_names:
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )


            # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 0.5 )
            # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )
            
            pyrosim.End()

        Create_world()
        Create_body()
        Create_brain()

        # run simulation 
        os.system(f"py simulate.py {directOrGUI}")

        # read from fitness file and store value 
        fitness = open("fitness.txt", "r")
        self.fitness = float(fitness.read())
        fitness.close()

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weights[row,col] = random.random()*2 -1



    




