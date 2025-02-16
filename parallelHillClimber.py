

# hillclimber class

from solution import SOLUTION
import constants as c
import copy
import os
import time

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")

        self.parents = {}
        self.nextAvailableID = 0

        for num in range(0, c.populationSize):
            self.parents[num] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        #self.parent.Evaluate("GUI")
        self.Evolve()

        self.Show_best()
        

    def Evolve(self):
        
        self.Evaluate(self.parents)
            
        for currentGeneration in range(0,c.populationSize):
            self.Evolve_For_One_Generation()
            

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        
        
    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.Set_ID(self.children[key])


    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()
            

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] =  self.children[key]
            else:
                self.parents[key] = self.parents[key]
          
        
    def Print(self):
        for key in self.parents.keys():
            print(f'\nparent fitness = {self.parents[key].fitness}, child fitness = {self.children[key].fitness}\n')


    def Show_best(self):
        fitness_dict = {}
        
        for key in self.parents.keys():
            fitness_dict[key] = self.parents[key].fitness

        min_key = min(fitness_dict, key=fitness_dict.get)
        self.parents[min_key].Start_Simulation("GUI")

    def Set_ID(self, child):
        child.myID = self.nextAvailableID
        self.nextAvailableID += 1
    
    def Evaluate(self,solutions):

        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")
        
        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()



