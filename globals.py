import numpy as np 
SCREEN_SIZE = (1200, 800)

def to_math_coords(point): 
    x = point[0] - (SCREEN_SIZE[0] // 2)
    y = (SCREEN_SIZE[1] // 2) - point[1]
    return np.array([x,y])


def to_screen_coords(point): 
    x = (SCREEN_SIZE[0] // 2) + point[0]
    y = (SCREEN_SIZE[1] // 2) - point[1]
    return np.array([x,y])
    