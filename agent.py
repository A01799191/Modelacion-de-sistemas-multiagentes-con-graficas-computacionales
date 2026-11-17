# Description: Reactive cleaning robot agent definition in a discrete grid environment.
# Author(s):
# Rodrigo Castillo Francisco - A01799191
# Ian Morgado Villaseñor - A01754495
# Creation Date: 11/16/2026

from mesa.discrete_space import CellAgent

class CleaningRobot(CellAgent):
    DIRECTIONS = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1),
    ]

    # Purpose: Initialize a cleaning robot at its starting cell and set its movement counter to zero.
    # Parameters:
    #   self: Current instance of the robot agent.
    #   model: Reference to the simulation model managing the environment.
    #   cell: Initial grid cell where the robot is placed.
    # Return value: None.

    def __init__(self, model, cell):
        """Initialize the agent with a starting cell."""
        super().__init__(model)
        self.cell = cell
        self.movement = 0

    # Purpose: Execute one reactive perception-action cycle (vacuum dirty cell or move randomly).
    # Parameters:
    #   self: Current instance of the robot agent.
    # Return value: None.

    def step(self):
        """Execute one reactive decision cycle for the robot."""
        x, y = self.cell.coordinate

        if self.model.grid.dirty.data[x, y] == 1:
            self.model.grid.dirty.data[x, y] = 0
            return

        dx, dy = self.random.choice(self.DIRECTIONS)
        next_x = x + dx
        next_y = y + dy

        if 0 <= next_x < self.model.width and 0 <= next_y < self.model.height:
            self.cell = self.model.grid[(next_x, next_y)]
            self.movement += 1






