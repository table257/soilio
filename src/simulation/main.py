import model

def startLoad(path):
    farm = model.Farms.Farm.farmFromJson(path)
    return farm

# returns new farm of type 'arid', 'temperate', or 'boreal'
def startNew(reg : str):
    farm = model.Farms.Farm.makeFarm(reg, "../assets/regions.json")
    return farm

def iterate():
    pass

def plant(plant, plot):
    pass
 
def pick(plot):
    pass

def water(plot):
    pass

def fertilize(plot):
    pass

farmy = startNew('arid')
print(farmy.region)
