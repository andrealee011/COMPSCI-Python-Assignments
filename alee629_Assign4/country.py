#Assignment 4: Country Classes
#Andrea Lee 250836721

#create class
class Country:

#construct class
    def __init__(self,  name='', pop=0, area=0, continent=''):
        self.name = name
        self.pop = int(pop)
        self.area = float(area)
        self.continent = continent

#getter methods
    def getName(self):
        return self.name

    def getPopulation(self):
        return self.pop

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

#setter methods
    def setPopulation(self, pop):
        self.pop = int(pop)

    def setArea(self, area):
        self.area = float(area)

    def setContinent(self, continent):
        self.continent = continent

    def getPopDensity(self, pop, area):
        return round(float(self.pop/self.area), 2)

#compute string
    def __repr__(self):
        return self.name + ' (pop: ' + str(self.pop) + ', size: ' + str(self.area) + ') in ' + self.continent
