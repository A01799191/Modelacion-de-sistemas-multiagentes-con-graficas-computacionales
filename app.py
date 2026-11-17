# Description: Interactive Solara visualization dashboard for the reactive cleaning robots simulation.
# Author(s):
# Rodrigo Castillo Francisco - A01799191
# Ian Morgado Villaseñor - A01754495
# Creation Date: 11/16/2026

from mesa.visualization import SolaraViz, SpaceRenderer, make_plot_component
from mesa.visualization.components import (
    AgentPortrayalStyle,
    PropertyLayerStyle,
)

from model import CleaningModel

# Purpose: Define the visual styling for each cleaning robot on the grid.
# Parameters:
# agent: Instance of CleaningRobot to be rendered.
# Return value: AgentPortrayalStyle object containing visual properties for the agent.

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="dodgerblue",
        marker="o",
        size=220,
        zorder=5,
        alpha=1.0,
        edgecolors="black",
        linewidths=1.5,
    )


# Purpose: Define the visual styling for the dirt property layer on the grid.
# Parameters:
# layer: PropertyLayer object representing cell attributes.
# Return value: PropertyLayerStyle object for the dirty layer, or None if not applicable.

def property_layer_portrayal(layer):
    """Define visual style for the dirty cells layer."""
    if layer.name == "dirty":
        return PropertyLayerStyle(
            color="saddlebrown",
            alpha=0.6,
            colorbar=False,
            vmin=0,
            vmax=1,
        )
    return None


model_params = {
    "num_agents": {
        "type": "SliderInt",
        "value": 5,
        "label": "Number of Agents",
        "min": 1,
        "max": 30,
        "step": 1,
    },
    "width": {
        "type": "SliderInt",
        "value": 10,
        "label": "Room Width (M)",
        "min": 5,
        "max": 30,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 10,
        "label": "Room Height (N)",
        "min": 5,
        "max": 30,
        "step": 1,
    },
    "dirty_percentage": {
        "type": "SliderFloat",
        "value": 0.5,
        "label": "Initial Dirty Ratio",
        "min": 0.1,
        "max": 1.0,
        "step": 0.05,
    },
    "max_steps": {
        "type": "SliderInt",
        "value": 200,
        "label": "Max Steps",
        "min": 50,
        "max": 1000,
        "step": 50,
    },
}

initial_model = CleaningModel()

renderer = (
    SpaceRenderer(model=initial_model, backend="matplotlib")
    .setup_structure(lw=1, ls="solid", color="gray", alpha=0.3)
    .setup_propertylayer(property_layer_portrayal)
    .setup_agents(agent_portrayal)
)
renderer.render()

clean_plot = make_plot_component("Clean_Percentage")
movements_plot = make_plot_component("Total_Movements")

page = SolaraViz(
    initial_model,
    renderer,
    components=[clean_plot, movements_plot],
    model_params=model_params,
    name="Reactive Cleaning Robots Simulation",
)


