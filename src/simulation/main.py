import model

def startLoad(path):
    farm = model.Farms.Farm.farmFromJson(path)
    return farm

# returns new farm of type 'arid', 'temperate', or 'boreal'
def startNew(reg):
    farm = model.Farms.Farm.makeFarm(reg, "../assets/regions.json")
    return farm

def iterate():
    pass

def plant(newPlant, plot):
    plot.plant = newPlant
 
def pick(plot):
    if plot.plant == None:
        return None
    else:
        plant = plot.plant;
        plot.plant = None
        return plant

def addWater(plot, amtWater):
    plot.water = plot.water + amtWater
    return plot.water

def fertilize(plot):
    pass
