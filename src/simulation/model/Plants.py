#!/usr/bin/python3

import json
from Environment import *

class Species:
    def __init__(self, name="", hardiness=0, phases=[], pH=pH()):
        self.name = name
        self.hardiness = hardiness
        self.phases = phases
        self.pH = pH

    def jsonToSpecies(self, data):
        x = json.loads(data)
        self.name = x["name"]
        self.hardiness = x["hardiness"]
        self.phases = x["phases"]
        #self.pH = x["pH"]
        self.pH = pH(**x["pH"])

    def speciesToJSON(self):
        x = {'name':self.name,'hardiness':self.hardiness,'phases':self.phases,'pH':self.pH.__dict__}
        return json.dumps(x, separators=(',',':'), ensure_ascii=False)

class Phase:
    def __init__(self, water=Water(), N=N(), P=P(), K=K(), unicode=""):
        self.water = water
        self.N = N
        self.P = P
        self.K = K
        self.unicode = unicode

class Plant:
    def __init__(self, species=Species(), curPhase=Phase()):
        self.species = species
        self.curPhase = curPhase

corn = Species()
print(corn.pH.value, corn.pH.min, corn.pH.max)
data='{"name":"corn","hardiness":15,"phases":[{"water":{"min":1,"max":4},"N":{"min":4,"max":5},"P":{"min":0.4,"max":0.6},"K":{"min":3,"max":5},"unicode":"ஃ"},{"water":{"min":3,"max":7},"N":{"min":3,"max":5},"P":{"min":0.3,"max":0.5},"K":{"min":2,"max":4},"unicode":"ɾ"},{"water":{"min":5,"max":10},"N":{"min":2,"max":4},"P":{"min":0.4,"max":0.5},"K":{"min":2,"max":4},"unicode":"ʇ"},{"water":{"min":4,"max":12},"N":{"min":2.75,"max":3.75},"P":{"min":0.3,"max":0.5},"K":{"min":1,"max":5},"unicode":"ʬ"}],"pH":{"min":5.8,"max":7  }}'
corn.jsonToSpecies(data)
print(corn.pH.value, corn.pH.min, corn.pH.max)
jsonObj = corn.speciesToJSON()
print(jsonObj)
