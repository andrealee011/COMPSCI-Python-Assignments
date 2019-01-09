#Assignment 4: Country Classes
#Andrea Lee 250836721

#import country module to get base class
import country

#create derived class
class CountryCatalogue(country.Country):
    def __init__(self, data_file, continent_file): #construct class

        super().__init__(self) #call base class constructor

        data_file = open(data_file) #open file
        continent_file = open(continent_file)

        data_list = data_file.readlines() #read file and create list of countries
        continent_list = continent_file.readlines()

        country_data = []
        country_continent = []
        countryCat = {}
        cDictionary = {}

        for country_name in data_list[1:]: #split each country's data in list of countries and get rid of header
            country_list = country_name.strip().split('|')
            country_data.append(country_list)

        for country_name in continent_list[1:]: #split each (country, continent) in list of countries and get rid of header
            country_list = country_name.strip().split(',')
            country_continent.append(country_list)

        for country_name in country_continent: #fill Dictionary
            cDictionary[country_name[0]] = country_name[1]

        for country_name in country_data: #fill Catalogue
            country_object = country.Country(country_name)
            pop = country_object.setPopulation(int(country_name[1].replace(',', '')))
            area = country_object.setArea(float(country_name[2].replace(',', '')))
            continent = country_object.setContinent(cDictionary[country_name[0]])
            countryCat[country_name[0]] = {'Population': country_object.getPopulation(), 'Area': country_object.getArea(), 'Continent': country_object.getContinent()}

        self.countryCat = countryCat
        self.cDictionary = cDictionary

    def findCountry(self, country_name): #function to look up country
        if country_name in self.countryCat:
            country_object = country.Country(country_name)
            country_object.setPopulation(self.countryCat[country_name]['Population'])
            country_object.setArea(self.countryCat[country_name]['Area'])
            country_object.setContinent(self.countryCat[country_name]['Continent'])
            return country_object #return the string representation of the country object
        else: #return null if country not in catalogue
            return None

    def setPopulationOfCountry(self, country_name, pop): #function to set population
        if country_name in self.countryCat:
            country_object = country.Country(country_name)
            country_object.setPopulation(int(pop))
            self.countryCat[country_name]['Population'] = country_object.getPopulation()
            return True
        else: #return false if country not in catalogue
            return False

    def setAreaOfCountry(self, country_name, area): #function to set area
        if country_name in self.countryCat:
            country_object = country.Country(country_name)
            country_object.setArea(float(area))
            self.countryCat[country_name]['Area'] = country_object.getArea()
            return True
        else: #return false if country not in catalogue
            return False

    def addCountry(self, country_name, pop, area, continent): #function to add country to dictionary and catalogue
        if country_name in self.countryCat and self.cDictionary: #return false if country already in dictionary and catalogue
            return False
        else:
            if country_name not in self.countryCat:
                country_object = country.Country(country_name)
                country_object.setPopulation(int(pop))
                country_object.setArea(float(area))
                country_object.setContinent(continent)
                self.countryCat[country_name] = {'Population': country_object.getPopulation(), 'Area': country_object.getArea(), 'Continent': country_object.getContinent()}
            if country_name not in self.cDictionary:
                self.cDictionary[country_name] = continent
            return True

    def deleteCountry(self, country_name): #function to delete country from dictionary and catalogue
        if country_name in self.countryCat:
            del self.countryCat[country_name]
        if country_name in self.cDictionary:
            del self.cDictionary[country_name]

    def printCountryCatalogue(self): #function to print catalogue
        for country_name in self.countryCat:
            country_object = country.Country(country_name)
            country_object.setPopulation(self.countryCat[country_name]['Population'])
            country_object.setArea(self.countryCat[country_name]['Area'])
            country_object.setContinent(self.countryCat[country_name]['Continent'])
            print(country_object) #print string representation for each country's objects

    def getCountriesByContinent(self, continent): #function to return a list of countries in a continent
        list = []
        for country_name in self.countryCat:
            if self.cDictionary[country_name] == continent:
                country_object = country.Country(country_name)
                list.append(country_object.getName())
        return list

    def getCountriesByPopulation(self, continent=''): #function to return a list of countries with its population in a continent
        def getKey(item):
            return item[1]
        list = []
        if continent == '': #return list of all countries if continent name is empty string
            for country_name in self.countryCat:
                country_object = country.Country(country_name)
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                list.append((country_object.getName(), country_object.getPopulation()))
            return sorted(list, reverse=True, key=getKey)
        elif continent in self.cDictionary.values():
            for country_name in self.countryCat:
                if self.cDictionary[country_name] == continent:
                    country_object = country.Country(country_name)
                    pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                    list.append((country_object.getName(), country_object.getPopulation()))
            return sorted(list, reverse=True, key=getKey)
        else: #return blank list if continent does not exist and is not empty
            return list

    def getCountriesByArea(self, continent=''): #function to return a list of countries with its area in a continent
        def getKey(item):
            return item[1]
        list = []
        if continent == '': #return list of all countries if continent name is empty string
            for country_name in self.countryCat:
                country_object = country.Country(country_name)
                area = country_object.setArea(self.countryCat[country_name]['Area'])
                list.append((country_object.getName(), country_object.getArea()))
            return sorted(list, reverse=True, key=getKey)
        elif continent in self.cDictionary.values():
            for country_name in self.countryCat:
                if self.cDictionary[country_name] == continent:
                    country_object = country.Country(country_name)
                    area = country_object.setArea(self.countryCat[country_name]['Area'])
                    list.append((country_object.getName(), country_object.getArea()))
            return sorted(list, reverse=True, key=getKey)
        else: #return blank list if continent does not exist and is not empty
            return list

    def findMostPopulousContinent(self): #function to return the name and population of the continent with the most people living in it
        africa_list = []
        asia_list = []
        europe_list = []
        north_america_list = []
        south_america_list = []
        for country_name in self.countryCat: #create list of country populations for each continent
            country_object = country.Country(country_name)
            if self.cDictionary[country_name] == 'Africa':
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                africa_list.append(country_object.getPopulation())
            if self.cDictionary[country_name] == 'Asia':
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                asia_list.append(country_object.getPopulation())
            if self.cDictionary[country_name] == 'Europe':
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                europe_list.append(country_object.getPopulation())
            if self.cDictionary[country_name] == 'North America':
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                north_america_list.append(country_object.getPopulation())
            if self.cDictionary[country_name] == 'South America':
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                south_america_list.append(country_object.getPopulation())
        africa = ('Africa', sum(africa_list)) #sum country populations for each continent
        asia = ('Asia', sum(asia_list))
        europe = ('Europe', sum(europe_list))
        north_america = ('North America', sum(north_america_list))
        south_america = ('South America', sum(south_america_list))
        list = [africa, asia, europe, north_america, south_america]
        def getKey(item):
            return item[1]
        return max(list, key=getKey) #return continent with highest population

    def filterCountriesByPopDensity(self, lower, upper): #function to return list of populationi densities within range
        list = []
        for country_name in self.countryCat: #calculate pop density for each country
            country_object = country.Country(country_name)
            pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
            area = country_object.setArea(self.countryCat[country_name]['Area'])
            pop_density = country_object.getPopDensity(pop, area)
            if lower < pop_density < upper: #create list of pop densities in range
                list.append((country_name, pop_density))
        def getKey(item):
            return item[1]
        return sorted(list, reverse=True, key=getKey) #return sorted list

    def saveCountryCatalogue(self, output_file): #fuction to save catalogue information to a file
        try:
            output_file = open(output_file, 'w') #open file to write
            output_file.write('Name|Continent|Population|Area|Population Density\n')
            for country_name in sorted(self.countryCat): #sort countries alphabetically and write information for each country to file
                country_object = country.Country(country_name)
                continent = country_object.setContinent(self.countryCat[country_name]['Continent'])
                pop = country_object.setPopulation(self.countryCat[country_name]['Population'])
                area = country_object.setArea(self.countryCat[country_name]['Area'])
                pop_density = country_object.getPopDensity(pop, area)
                output_file.write('%s|%s|%d|%.2f|%.2f\n' % (country_name, country_object.getContinent(), country_object.getPopulation(), country_object.getArea(), pop_density))
            output_file.close()
            return len(self.countryCat) #return number of items written
        except:
            return -1 #return -1 if operation unsuccessful
