import numpy as np
import math
import matplotlib.pyplot as plt
import time
from scipy import interpolate
from scipy.optimize import root
import pymc
import obspy
import random

class Model(object):

    '''  '''

    def __init__(self, params_dict):

        self.no_layers = random.randint(params_dict['min_layers'],params_dict['max_layers']) # generate number of layers
        self.layers = generate_layer_dictionary(self.no_layers) # generate dictionary of layer names
        self.interfaces = generate_interfaces(self.no_layers, params_dict)
        for x in np.arange(self.no_layers):
            setattr(self, self.layers[x]['layer_name'], Layer(params_dict, self.interfaces, x+1))

class Layer(object):

    ''' Initializes layer values - all but depth which must be generated in model to attain correct order '''

    def __init__(self, params_dict, interface_depths, layer_no):

        self.number = layer_no
        self.density = random.uniform(params_dict['min_rho'], params_dict['max_rho'])
        self.velocity = random.uniform(params_dict['min_vel'], params_dict['min_vel'])
        self.mu = 1
        self.upper_interface = interface_depths[layer_no - 1]
        self.lower_interface = interface_depths[layer_no]

def calc_misfit(data, synthetic):

    ''' where data is an obspy trace object '''

    sum_of_squared_diffs = 0

    for point in np.arange(data.stats.npts):
        sum_of_squared_diffs += (data[point] - synthetic[point])**2

    return sum_of_squared_diffs

def generate_layer_dictionary(no_layers):
    layer_dict = []
    for x in np.arange(no_layers):
        layer_dict.append({'layer_name':'layer_'+str(x+1)})
    return layer_dict

def generate_interfaces(no_layers, params_dict):
    depth_vec = [0]
    for x in np.arange(no_layers-1):
        depth_vec.append(random.randint(params_dict['min_depth'],params_dict['max_depth']))
    depth_vec.append(params_dict['max_depth'])
    depth_vec = sorted(depth_vec)
    return depth_vec
