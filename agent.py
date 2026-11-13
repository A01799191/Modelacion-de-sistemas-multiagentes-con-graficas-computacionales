import numpy as np
import pandas as pd
import seaborn as sns
import math 
import mesa 
from mesa.discrete_space import CellAgent, OrthogonalMooreGrid


# This is a reactive agent that cleans dirty cell or move randomly 
# In this script is the definition and conduct of the reactive cleaning robot 
# Atributes :
# Cell is the current grid that is occupied by the robot
# Movements is the total number os valid cell transition performed 

class CleaningRobot(CellAgent):
    #Inicitialize the agent with a starting cell. 
    def __init__(self, model, cell ):
        super().__init__(model)
        self.cell = cell
        self.movement = 0

def step(self):
    # In this part execute one reactive decision cycle for the robot
    x , y = self.cell.coordinate
    # If the current cell is dirty is represented with 1 then vacuum it and end turn
    if self.model.grid.dirty[x,y] == 1:
        self.model.grid.dirty[x,y] = 0
        return

    # For the other hand take one of the 8 more directions randonmly








