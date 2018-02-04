import model

def startLoad(path):
    farm = Farm.farmFromJson(path)
    pass	

# returns new farm of type 'arid', 'temperate', or 'boreal'
def startNew(reg : str):
	return Farm.makeFarm(reg)

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


