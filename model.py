#This is the multi-agent model simulating reactive cleaning robots in a M x N room space

import math
import mesa 
from mesa.discrete_space import OrthogonalMooreGrid


from agent import CleaningRobot


#The environment have to manage the space , the dirt and the robots

# The attributes : 
# width : M
# height : N
# num_agents : number of robots 
# dirty porcentaje : The proportions of dirty cells
# max_steps : Avoid infinite run of the program
# elapsed_space : Step counter 
# clean_time : the time that the robots clear al the space 
# grid : Representation of the room
# data_collector : results and metrics of the simulation


class CleaningModel(mesa.Model):
    def __init__(self , width = 50 , height = 50 , num_agents = 10, dirty_porcentage = 0.9, max_steps = 200, rng = None):
        # Creation of the cleaning simulation
         super.__init__(rng = rng)
         self.width = width
         self.height = height
         self.num_agents = num_agents
         self.dirty_porcentage = dirty_porcentage
         self.max_steps = max_steps

         self.elapsed_steps = 0
         self.time_to_clean = None

         # Closed grid when there is a cleaning robots in one space 
         self.grid = OrthogonalMooreGrid((width, height), capacity=math.inf , random = self.random)

         #Initialization of dirty cells randomly 1 is for the dirt and 0 is clean
         

