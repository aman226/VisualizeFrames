#!/usr/bin/env python3
from frameviz import FrameVisualization
import numpy as np

ft = FrameVisualization([-4,4],[-4,4],[0,8])
initial_position = np.array([0,0,0])
basis_vector = np.array([ [1.0 , 0.0, 0.0], 
                          [0.0 , 1.0, 0.0], 
                          [0.0 , 0.0, 1.0]])
ft.addFrame("Ground", initial_position, basis_vector,0.2)
ft.addFrame("Precession", initial_position, basis_vector)
while True:
    for angle in np.linspace(0,2*np.pi,300):
        ft.updateFrame("Precession",initial_position, basis_vector)
        ft.applyEulerRotation("Precession",angle,np.pi/6,angle,"ZYZ")
        ft.displayAllFrames(0.01)
