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

def iterate(farm : Farm):
    farm.curIter += 1
    for counter,cycle in farm.cycles:
        counter += cycle.length
        if farm.curIter >= counter:
            farm.curCycle = next(cycle)
            break
    # generate precipitation, temperature, daylight
    precipitation = Precipitation(round(random.uniform(farm.curCycle.precipitation.min, farm.curCycle.precipitation.max)),2)
    plot.water += precipitation
    temperature = Temperature(round(random.uniform(farm.curCycle.temperature.min, farm.curCycle.temperature.max)),2)
    daylight = Daylight(round(random.uniform(farm.curCycle.daylight.min, farm.curCycle.daylight.max)),2)
    for plot in farm.plots:
        #calculate health n shit
        b = plot.plant.curHealth
        if plot.plant.species.temperature.min <= temperature <= plot.plant.species.temperature.max:
            b *= 0.95
        if plot.plant.curPhase.N.min <= plot.N <= plot.plant.curPhase.N.max:
            b *= 0.99
        if plot.plant.curPhase.P.min <= plot.P <= plot.plant.curPhase.P.max:
            b *= 0.97
        if plot.plant.curPhase.K.min <= plot.K <= plot.plant.curPhase.K.max:
            b *= 0.98
        if plot.plant.curPhase.Water.min <= plot.water*plot.drainage <= plot.plant.curPhase.Water.max:
            b *= 0.80
        h = plot.plant.species.hardiness
        if b < 0.5*h:
            plot.plant = None
        if 1.03*h <= b <= 1.05*h:
            plot.plant.curPhase = plot.plant.species.phases[0]
        elif 1.05*h < b < 1.5*h:
            plot.plant.curPhase = plot.plant.species.phases[1]
        elif 1.5*h <= b:
            plot.plant.curPhase = plot.plant.species.phases[2]
