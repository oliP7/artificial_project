import pygame
import numpy as np
import random as rndm

MAX_WANDER_ROTATION = 15    #degrees
MAXIMUM_SEEK_DISTANCE  = 65 #pixels
MINIMUM_AVOID_DISTANCE = 200 #pixels


def seek(agent, target_position, time_passed_seconds):
    """
    Kinematic Seek Behavior
    Calculate a vector from the agent to the target_position.  (Towards target.)
    """

    seek_vector = target_position - agent.position
    normalized_seek_vector = seek_vector / np.sqrt(np.dot(seek_vector, seek_vector))
    agent.update(normalized_seek_vector, time_passed_seconds)

def arrive(agent, target_position, time_passed_seconds):
    """
    Kinematic Arrive Behavior
    Seek only if my target is too far from me (as defined by maximum_seek_behavior).
    """
  
    arrive_vector = target_position - agent.position
    distance_to_target = np.sqrt(np.dot(arrive_vector, arrive_vector))
    normalized_seek_vector = arrive_vector / distance_to_target
    
    if distance_to_target > MAXIMUM_SEEK_DISTANCE:
        agent.update(normalized_seek_vector, time_passed_seconds)
    

def rotateVectorCounterclockwise(vector, angle_in_degrees):
    angle_in_radians = (angle_in_degrees / 180) * np.pi
    
    sine_of_angle   = np.sin(angle_in_radians)
    cosine_of_angle = np.cos(angle_in_radians)
    
    transformation_matrix = np.array([
                                      [cosine_of_angle, -sine_of_angle],
                                      [sine_of_angle,  cosine_of_angle]
                                     ])

    
    rotated_vector = np.linalg.solve(transformation_matrix, vector)
    
    return rotated_vector
    

def randomBinomial():
    return rndm.random() - rndm.random()




