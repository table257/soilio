#!/usr/bin/python3

import json
from .Environment import *
import os

class Phase:
    def __init__(self, water=Water(), N=N(), P=P(), K=K(), unicode=""):
        self.Water = water
        self.N = N
        self.P = P
        self.K = K
        self.unicode = unicode
    
    def jsonToPhase(self, data):
    	self.Water = Water(**data["water"])
    	self.N = N(**data["N"])
    	self.P = P(**data["P"])
    	self.K = K(**data["K"])
    	self.unicode = data["unicode"]

class Species:
    def __init__(self, name="", hardiness=0, phases=[], pH=pH(), temperature=Temperature()):
        self.name = name
        self.hardiness = hardiness
        self.phases = phases
        self.pH = pH
        self.temperature = Temperature

    def makeSpeciesFromJSON(name):
        file = "../assets/plants/" + name + ".json"
        with open(file, 'r') as f:
        	x = json.load(f)
       	spec = Species()
        spec.name = x["name"]
        spec.hardiness = x["hardiness"]
        spec.pH = pH(**x["pH"]) 
        spec.temperature = Temperature(**x["t"])
        phasesData = x["phases"]
        for data in phasesData:
        	phase = Phase()
        	phase.jsonToPhase(data)
        	spec.phases.append(phase)
       	return spec

    def speciesToDict(self):
        x = {'name':self.name,'hardiness':self.hardiness,'phases':self.phases,'pH':self.pH.__dict__}
        return x
        #return json.dumps(x, separators=(',',':'), ensure_ascii=False)
    
    def getSpeciesList():
        specList = []
        for file in os.listdir("../assets/plants/"):
            if file.endswith(".json"):
            	spec = Species.makeSpeciesFromJSON((file[0:(len(file)-5)]))
            	specList.append(spec)
        return specList


class Plant:
    def __init__(self, species=Species(), curPhase = Phase()):
        self.species = species
        self.curHealth = species.hardiness
        self.curPhase = len(species.phases)

#corn = Species()
#data='{"name":"corn","hardiness":15,"phases":[{"water":{"min":1,"max":4},"N":{"min":4,"max":5},"P":{"min":0.4,"max":0.6},"K":{"min":3,"max":5},"unicode":"ஃ"},{"water":{"min":3,"max":7},"N":{"min":3,"max":5},"P":{"min":0.3,"max":0.5},"K":{"min":2,"max":4},"unicode":"ɾ"},{"water":{"min":5,"max":10},"N":{"min":2,"max":4},"P":{"min":0.4,"max":0.5},"K":{"min":2,"max":4},"unicode":"ʇ"},{"water":{"min":4,"max":12},"N":{"min":2.75,"max":3.75},"P":{"min":0.3,"max":0.5},"K":{"min":1,"max":5},"unicode":"ʬ"}],"pH":{"min":5.8,"max":7  }}'
#corn.jsonToSpecies("corn")
#print(corn.pH.min, corn.pH.max)
#print(corn.hardiness)
#print(corn.phases[1].N.min, corn.temperature.max)
#print(corn.phases[0].Water.min, corn.phases[0].Water.max)
#print(corn.phases[0])
#p1 = Plant(corn)
#print(p1.curHealth)
#print(p1.curPhase.unicode)
#print(p1.curPhase.Water.min) # 4
