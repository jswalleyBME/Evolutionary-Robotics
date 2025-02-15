
# hillclimber class

from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:

    def __init__(self):
        
        self.parent = SOLUTION()
        self.parent.Evaluate("GUI")
        self.Evolve()
        
    def Evolve(self):
        
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()
        
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent =  self.child
        else:
            self.parent = self.parent 
          
        
    def Print(self):
        print(f'\nparent fitness = {self.parent.fitness}, child fitness = {self.child.fitness}\n')


    def Show_best(self):
        self.parent.Evaluate("GUI")

