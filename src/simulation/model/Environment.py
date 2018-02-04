#!/usr/bin/python3

'''
Module name:    Environment
Purpose:        Defines all environmental factors that affect a farm
Classes:        pH, Water, Drainage, Temperature, N, P, K, Precipitation, Daylight
                Each class has 3 attributes: value (realtime value), min and max, which defines
                a limit for whatever object that the class is an attribute of.
'''

class pH:
    def __init__(self, value=7, min=0, max=14):
        self.min = min
        self.max = max

class Water:
    def __init__(self, value=1, min=0, max=100):
        self.min = min
        self.max = max

class Drainage:
    def __init__(self, value=1, min=0, max=100):
        self.min = min
        self.max = max

class Temperature:
    def __init__(self, value=12, min=-273, max=100):
        self.min = min
        self.max = max

class N:
    def __init__(self, value=1, min=0, max=100):
        self.min = min
        self.max = max

class P:
    def __init__(self, value=1, min=0, max=100):
        self.min = min
        self.max = max

class K:
    def __init__(self, value=1, min=0, max=100):
        self.min = min
        self.max = max

class Precipitation:
    def __init__(self, value=25, min=0, max=10000):
        self.min = min
        self.max = max

class Daylight:
    def __init__(self, value=12, min=0, max=24):
        self.min = min
        self.max = max
