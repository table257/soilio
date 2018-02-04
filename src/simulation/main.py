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
        plant = plot.plant
        plot.plant = None
        return plant

# input: plot object & amount of water to add
# returns amount of water in the plot now
def addWater(plot, amtWater):
    plot.water = plot.water + amtWater
    return plot.water

def fertilize(plot, n, p, k):
    plot.N = plot.N + n
    plot.P = plot.P + p
    plot.K = plot.K + k
