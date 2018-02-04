#!/usr/bin/python3

import json
import random
from .Environment import *
from .Plants import Plant

class Cycle:
    def __init__(self, name="", length=0, precipitation=Precipitation(), temperature=Temperature(), daylight=Daylight()):
        self.name = name
        self.length = length
        self.precipitation = precipitation
        self.temperature = temperature
        self.daylight = daylight

    def jsonToCycle(self, data):
    	self.name = data["name"]
    	self.length = data["length"]
    	self.precipitation = Precipitation(**data["p"])
    	self.temperature = Temperature(**data['t'])
    	self.daylight = Daylight(**data['dl'])

class Region:
    def __init__(self, name="", drainage=0, pH=pH(), cycles=[], N=N(), P=P(), K=K()):
        self.name = name
        self.drainage = drainage
        self.pH = pH
        self.cycles = cycles
        self.N = N
        self.P = P
        self.K = K

    def makeRegion(name, path):
    	reg = Region()
    	with open(path, 'r') as f:
    		data = json.load(f)
    		data = data["Regions"]
    	if name == 'arid':
    		data = data[0]
    	elif name == 'temperate':
    		data = data[1]
    	elif name == 'boreal':
    		data = data[2]
    	else:
    		print("error, unknown region specified. (currently) Accepted regions: arid, temperate, boreal.")
    		exit(-1)
    	reg.name = name
    	reg.drainage = Drainage(**data["drainage"])
    	reg.pH = pH(**data["pH"])
    	reg.N = N(**data["N"])
    	reg.P = P(**data["P"])
    	reg.K = K(**data["K"])
    	cycleData = data["cycles"]
    	for curCycle in cycleData:
    		cycle = Cycle()
    		cycle.jsonToCycle(curCycle)
    		reg.cycles.append(cycle)
    	return reg

class Plot:
    def __init__(self, plant=Plant(), water=0, N=0, P=0.0, K=0, pH=0, drainage=0):
        self.plant = None
        self.water = water
        self.N = N
        self.P = P
        self.K = K
        self.pH = pH
        self.drainage = drainage

    def makePlot(region):
        plot = Plot()
        plot.N = random.randint(region.N.min, region.N.max)
        plot.P = round(random.uniform(region.P.min, region.P.max), 2)
        plot.K = random.randint(region.K.min, region.K.max)
        plot.pH = round(random.uniform(region.pH.min, region.pH.max), 2)
        plot.drainage = random.randint(region.drainage.min, region.drainage.max)
        return plot

    def stats(self):
        if (self.plant != None):
            x = {'Plant name':self.plant.species.name,'Plant health':self.plant.curHealth ,'water':self.water,'pH':self.pH, 'N':self.N, 'P':self.P, 'K':self.K, 'Drainage':self.drainage}
        else:
            x = {'water':self.water,'pH':self.pH, 'N':self.N, 'P':self.P, 'K':self.K, 'Drainage':self.drainage}
        return x


    #def waterPlant(self, water):


class Farm:
    def __init__(self):
        self.plots = [None]*300
        self.region = None
        self.curIter = 0;
        self.cycles = [None]
        self.curCycle = self.cycles[0]

    def makeFarm(regionStr, path):
        reg = Region.makeRegion(regionStr, path)
        farm = Farm()
        farm.region = reg
        farm.cycles = reg.cycles
        for i in range(0, 300):
            farm.plots[i] = Plot.makePlot(reg)
        return farm
      
    def farmFromJson(path):
        farm = Farm()
        with open(path, 'r') as f:
            fdata = json.load(f)
        farm.plots = fdata["plots"]
        farm.region = fdata["region"]
        farm.curIter = fdata["curIter"]
        farm.cycles = fdata["cycles"]
        farm.curCycle = fdata["curCycles"]
        return farm





