#This is the multi-agent model simulating reactive cleaning robots in a M x N room space

import math
from mesa import DataCollector, Model
from mesa.discrete_space import OrthogonalMooreGrid

from agent import CleaningRobot



class CleaningModel(Model):
    # Purpose: Configure the closed grid environment, distribute initial dirt randomly, and spawn robots at (0, 0).
    # Parameters:
    #   self: Current instance of the simulation model.
    #   width: Width of the room (M).
    #   height: Height of the room (N).
    #   numAgents: Total number of cleaning robots in the room.
    #   dirtyPercentage: Initial proportion of dirty cells (between 0.0 and 1.0).
    #   maxSteps: Maximum execution steps allowed before stopping the simulation.
    #   rng: Seed value for the random number generator.
    # Return value: None.

    def __init__(
        self,
        width=10,
        height=10,
        num_agents=5,
        dirty_percentage=0.5,
        max_steps=200,
        rng=None,
    ):
        super().__init__(rng=rng)
        self.width = width
        self.height = height
        self.num_agents = num_agents
        self.dirty_percentage = dirty_percentage
        self.max_steps = max_steps

        self.elapsed_steps = 0
        self.time_to_clean = None

        # Closed grid (torus=False) allowing multiple robots per cell
        self.grid = OrthogonalMooreGrid(
            (width, height), capacity=math.inf, random=self.random, torus=False
        )

        # Initialize dirty cells randomly (1 = dirty, 0 = clean)
        self.grid.create_property_layer("dirty", default_value=0)
        total_cells = width * height
        num_dirty = round(total_cells * dirty_percentage)
        all_coords = [(x, y) for x in range(width) for y in range(height)]

        for x, y in self.random.sample(all_coords, num_dirty):
            self.grid.dirty.data[x, y] = 1

        # All agents start at cell [1,1])
        start_cell = self.grid[(0, 0)]
        for _ in range(num_agents):
            CleaningRobot(self, start_cell)

        self.datacollector = DataCollector(
            model_reporters={
                "Clean_Percentage": self.get_clean_percentage,
                "Total_Movements": self.get_total_movements,
                "Elapsed_Steps": lambda m: m.elapsed_steps,
                "Time_To_Clean": lambda m: m.time_to_clean,
            }
        )
        self.datacollector.collect(self)
        self.running = True

        if self.get_clean_percentage() >= 100.0:
            self.time_to_clean = 0
            self.running = False

    # Purpose: Calculate the current percentage of clean cells in the room.
    # Parameters:
    #   self: Current instance of the simulation model.
    # Return value: Float representing the percentage of clean cells (0.0 to 100.0).

    def get_clean_percentage(self):
        total_cells = self.width * self.height
        dirty_cells = int(self.grid.dirty.data.sum())
        return ((total_cells - dirty_cells) / total_cells) * 100.0

    # Purpose: Compute the cumulative number of valid movements performed by all agents.
    # Parameters:
    #   self: Current instance of the simulation model.
    # Return value: Integer representing total movements across all robots.

    def get_total_movements(self):
        return sum(self.agents.get("movement"))

    # Purpose: Advance the simulation by one step, collect metrics, and check termination conditions.
    # Parameters:
    #   self: Current instance of the simulation model.
    # Return value: None.

    def step(self):
        if not self.running:
            return

        self.elapsed_steps += 1
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)

        if self.get_clean_percentage() >= 100.0:
            self.time_to_clean = self.elapsed_steps
            self.running = False
        elif self.elapsed_steps >= self.max_steps:
            self.time_to_clean = self.max_steps
            self.running = False