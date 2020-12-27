#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Created on 21 Dec 2020
    @Author: Geoff Willis
    @Email: gwillis18@yahoo.com
    @Updated On:
    @Updated On:
    @template: Randomize provided seeds using various statistical models
"""

import numpy as np

#First two generate test data, second two are called by system
def get_random_float_values_uniform_dist_test(low = 9500.0, high = 0.1, size = 500 ):
    return np.random.uniform(low, high, size)

def get_random_float_values_normal_dist(median = 9500., sigma = 1, size = 500):
    return np.random.normal(median, sigma, size)

#These are actually called by API, above can be used to gen data for plots to demonstrate the ranges
def generate_random_float_uniform(value, tolerance):
    half_tol = float(tolerance)/2
    val = float(value)
    return np.random.uniform(val-half_tol, val+half_tol)

def generate_random_float_normal(nom_val, sigma = 0.1):
    return np.random.normal(float(nom_val), float (sigma))

#Insert here if desire a different statistical model to generate random value from seed
def process_parameters(config):
    if(config):
        prob_distribution = config.get("distribution")
        prob_tolerance = config.get("tolerance")
        if(prob_distribution == "NORMAL"):
            return [generate_random_float_normal(element, prob_tolerance) for element in config.get("data")]
        elif(prob_distribution == "UNIFORM"):
            return [generate_random_float_uniform(element, prob_tolerance) for element in config.get("data")]
