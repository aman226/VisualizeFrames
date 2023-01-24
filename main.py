#!/usr/bin/env python3
from frameviz import FrameVisualization
import numpy as np


ft = FrameVisualization([-4,4],[-4,4],[-4,4],0.5)
initial_position = np.array([2.0,2.0,2.0])
basis_vector = np.array([ [1.0 , 0.0, 0.0], 
                          [0.0 , 1.0, 0.0], 
                          [0.0 , 0.0, 1.0] ])
ft.addFrame("Precession", initial_position, basis_vector)

while True:
    for angle in np.linspace(0,2*np.pi,300):
        ft.changeFrame("World")
        # Update in World Frame
        ft.updateFrame("Precession",initial_position, basis_vector)
        ft.applyEulerRotation("Precession",angle,np.pi/6,angle,"ZYZ")

        # Change to Precession Frame
        ft.changeFrame("Precession")

        # Display Frames wrt Precession Frame
        ft.displayAllFrames(0.01)
        