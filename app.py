# Simulation visualitazion

from mesa.visualization import (SolaraViz, SpaceRenderer)
from mesa.visualization.components import (AgentPortrayalStyle, PropertyLayerStyle)

from model import CleaningModel


# Visualitation of the cleaning robots ( you can changed if you want)
def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color ="blue", 
        marker = "o", 
        size = 20, 
        zorder = 2, 
        alpha = 0.8,
        edgecolor = "black", 
        linewidths= 1.5,
    )

def property_layer_portrayal(layer):
    if layer.name == "dirty":
        return PropertyLayerStyle(
            color = "brown", 
            alpha = 0.5,
            colorbar = False,
            vmin = 0, 
            vmax =1,  
        )
    return None

model_params = {
    "num_agents": {
        "type":"SliderInt", 
        "value": 5, 
        "label": "Number of agents", 
        "min": 1, 
        "max" : 30, 
        "step": 1, 
    },

    "width": {
        "type":"SliderInt", 
        "value": 10,
        "label": "M",
        "min": 5, 
        "max": 30,
        "step": 1, 
    }, 

    "height": {
        "type":"SliderInt", 
        "value": 10,
        "label": "N",
        "min": 5, 
        "max":30,
        "step":1, 
    }, 


    "dirty_porcentage":  {
        "type":"SliderFloat", 
        "value": 0.5,
        "label": "Initial dirty",
        "min": 0.1, 
        "max":1,
        "step":0.05, 
    }, 

    "max_steps": {
        "type":"SliderInt", 
        "value": 200,
        "label": "Max Steps",
        "min": 50, 
        "max":1000,
        "step":50, 
    }, 

}

initial_model = CleaningModel()

renderer = (
    SpaceRenderer(model = initial_model, backend = "matplotlib")
    .setup_propertylayer(propertylayer_portrayal)
    .setup_agents(agent_portrayal)
)
renderer.render()

#  This is the part of statistics












