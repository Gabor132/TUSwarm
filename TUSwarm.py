import math
from enum import Enum
import numpy as np


class FunctionType(Enum):
    ROSENBROCK = 1
    GRIEWANK = 2
    RASTRIGIN = 3


def calc_function(x,y, function_type):
    if function_type == FunctionType.ROSENBROCK:
        return ((1 - x) ** 2) + (100 * ((y - x ** 2) ** 2))
    elif function_type == FunctionType.GRIEWANK:
        return (x**2)/4000 + (y**2)/4000 - (math.cos(x)*math.cos(y/math.sqrt(2))) + 1
    elif function_type == FunctionType.RASTRIGIN:
        return 20 + (x**2 - 10*math.cos(2*math.pi*x)) + (y**2 - 10*math.cos(2*math.pi*y))


def calc_function_np(x, y, function_type):
    if function_type == FunctionType.ROSENBROCK:
        return ((1 - x) ** 2) + (100 * ((y - x ** 2) ** 2))
    elif function_type == FunctionType.GRIEWANK:
        return (x**2)/4000 + (y**2)/4000 - (np.cos(x)*np.cos(y/np.sqrt(2))) + 1
    elif function_type == FunctionType.RASTRIGIN:
        return 20 + (x**2 - 10*np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y))


def get_max_and_min(function_type):
    if function_type == FunctionType.ROSENBROCK:
        return (-3, 3, -3, 3, 0.5)
    elif function_type == FunctionType.GRIEWANK:
        return (-600, 600, -600, 600, 50)
    elif function_type == FunctionType.RASTRIGIN:
        return (-5.12, 5.12, -5.12, 5.12, 0.5)

