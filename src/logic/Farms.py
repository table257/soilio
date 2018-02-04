#!/usr/bin/python3

import json
from Environment import *
from Plants import Plant

class Cycle:
    def __init__(self, name="", length=0, precipitation=Precipitation(), temperature=Temperature(), daylight=Daylight()):
        self.name = name
        self.length = length
        self.precipitation = precipitation
        self.temperature = temperature
        self.daylight = daylight

class Region:
    def __init__(self, name="", drainage=0, pH=pH(), cycles=[]):
        self.name = name
        self.drainage = drainage
        self.pH = pH
        self.cycles = cyles

class Plot:
    def __init__(self, plant=Plant(), water=Water(), N=N(), P=P(), K=K(), pH=pH(), drainage=Drainage()):
        self.plant = plant
        self.water = water
        self.N = N
        self.P = P
        self.K = K
        self.pH = pH
        self.drainage = drainage

class Farm:
    def __init__(self, plots=[], )
