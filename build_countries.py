#Ziming Dong
#Student ID: 260951177

#import copy module
from copy import*
#make Country class
class Country:
    '''
    Represents a country
    Instance attributes: iso_code (str), name (str), continents (list),
                         co2_emissions (dict), population (dict)
    Class attributes: min_year_recorded (int), max_year_recorded (int)
    '''
    #make minimum and maximum year recorded as 9999 and 0
    min_year_recorded = 9999
    max_year_recorded = 0
    def __init__(self,iso_code,name,continents,year,co2_emissions,population):
        ''' (Country,str,str,list,int,float,int) -> Country
        creat a Country object
        
        >>> c1 = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> c1.name
        'China'
        
        >>> c2 = Country('CHN', 'China', ['ASIA'], 1997, -1, 1261996032)
        >>> c2.co2_emissions
        {}
        
        >>> c2 = Country('CHINA', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        Traceback (most recent call last):
        AssertionError
        '''
        #check special cases
        if len(iso_code) > 3 and iso_code != 'OWID_KOS':
            raise AssertionError
        #use deepcopy
        new_continents = deepcopy(continents)
        self.iso_code = iso_code
        self.name = name
        self.continents = new_continents
        #check special cases for co2_emissions and population
        if co2_emissions != -1:
            self.co2_emissions = {year : co2_emissions}
        else:
            self.co2_emissions = {}
        if population != -1:    
            self.population = {year : population}
        else:
            self.population = {}
            
    def __str__(self):
        ''' Country -> str
        returns a string representation of a country containing the name, the continents,
        and a string representation of both the co2_emissions dictionary and the population dictionary.
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> str(c)
        'China\\tASIA\\t{1997: 3414.549}\\t{1997: 1261996032}'
        
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> str(p)
        'Poland\\tEUROPE\\t{2009: 315.341}\\t{2009: 38352000}'
        '''
        #return string for Country
        return self.name + '\t' + ','.join(self.continents) + '\t' + str(self.co2_emissions) + '\t' + str(self.population)
    
    def add_yearly_data(self,string):
        ''' (Country,str) -> None
        This method updates the appropriate attributes of the country.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True
        >>> a.population == {1949: 7663783, 2018: 37122000}
        True
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> c.add_yearly_data('1822\\t0\\t385567456')
        >>> c.population
        {1997: 1261996032, 1822: 385567456}
        
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> p.add_yearly_data('1826\\t1.22\\t10920617')
        >>> p.co2_emissions
        {2009: 315.341, 1826: 1.22}
        '''
        #get str_list and year
        str_list = string.split('\t')
        year = int(str_list[0])
        #check special cases for co2_emissions and population
        if str_list[1] != '' and str_list[1] != -1:
            co2_emissions = float(str_list[1])
            self.co2_emissions[year] = co2_emissions
        if str_list[2] != '' and str_list[2] != -1:
            population = int(str_list[2])
            self.population[year] = population
        #update minimum and maximum year if possible
        if year > self.max_year_recorded:
            self.max_year_recorded = year
        if year < self.min_year_recorded:
            self.min_year_recorded = year    
    
    def get_co2_emissions_by_year(self,year):
        ''' (Country,int) -> float
        It returns the co2 emission of the country in the specified year if available.
        It returns 0.0 otherwise.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015
        >>> a.get_co2_emissions_by_year(2000)
        0.0
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> c.add_yearly_data('1822\\t0\\t385567456')
        >>> c.get_co2_emissions_by_year(1997)
        3414.549
        
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> p.add_yearly_data('1826\\t1.22\\t10920617')
        >>> p.get_co2_emissions_by_year(1826)
        1.22
        '''
        #use try block to get result
        try:
            return self.co2_emissions[year]
        except KeyError:
            return 0.0
    
    def get_co2_per_capita_by_year(self,year):
        ''' (Country,int) -> float
        It return the co2 emission per capita in tonnes for the specified year if available.
        If either the co2 emissions or the population of the country are not available for the specified year,
        the method returns None.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427
        >>> print(a.get_co2_per_capita_by_year(1949))
        None
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> c.add_yearly_data('1822\\t0\\t385567456')
        >>> round(c.get_co2_per_capita_by_year(1997), 5)
        2.70567
        
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> p.add_yearly_data('1826\\t1.22\\t10920617')
        >>> round(p.get_co2_per_capita_by_year(1826), 5)
        0.11172
        '''
        #use try block to get result and check special cases
        try:
            result = self.co2_emissions[year] * 1000000 / self.population[year]
        except KeyError:
            return None
        if result <= 0:
            return None
        #return result
        return result
    
    def get_historical_co2(self,year):
        ''' (Country,int) -> float
        It return the historical (total) co2 emission in millions of tonnes
        that the country has produced for all years up to and including the specified year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277
        >>> q.get_historical_co2(2007)
        108.176
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> c.add_yearly_data('1822\\t0\\t385567456')
        >>> c.get_historical_co2(1997)
        3414.549
        
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> p.add_yearly_data('1826\\t1.22\\t10920617')
        >>> p.get_historical_co2(1826)
        1.22
        '''
        #make result equal to 0.0
        result = 0.0
        #use for loop to add corresponding value to result
        for key in self.co2_emissions:
            if key <= year:
                if self.get_co2_emissions_by_year(key) == 0.0:
                    continue
                result += self.get_co2_emissions_by_year(key)
        #return result
        return result
    
    @classmethod
    def get_country_from_data(cls,string):
        ''' (type,str) -> Country
        The method should return a new Country object created from the data in the input string.
        
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{1991: 4.283}\\t{1991: 3280000}'
        
        >>> c = Country.get_country_from_data('CHN\\tChina\\tASIA\\t1997\\t3414.549\\t1261996032')
        >>> c.name
        'China'
        
        >>> p = Country.get_country_from_data('POL\\tPoland\\tEUROPE\\t2009\\t315.341\\t38352000')
        >>> p.population
        {2009: 38352000}
        '''
        #get str_list, iso_code, name, continents and year
        str_list = string.split('\t')
        iso_code = str_list[0]
        name = str_list[1]
        continents = str_list[2].split(',')
        year = int(str_list[3])
        #check special cases
        if str_list[4] == '':
            co2_emissions = -1
        else:
            co2_emissions = float(str_list[4])
        #use try block and check special cases
        try:
            if str_list[5] == '':
                population = -1
            else:
                population = int(str_list[5])
        except IndexError:
            population = -1
        #return Country with elements below
        return Country(iso_code,name,continents,year,co2_emissions,population)
    
    @staticmethod        
    def get_countries_by_continent(countries):
        ''' (list) -> dict
        The method returns a dictionary mapping a string representing a continent to a list of countries
        which all belong to that continent.
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> d = Country.get_countries_by_continent([c,a,r])
        >>> len(d['ASIA'])
        3
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> d = Country.get_countries_by_continent([c,a,r,p])
        >>> len(d['EUROPE'])
        2
        '''
        #make dict_continent with the continents in alphabetical order
        dict_continent = {'AFRICA':[],'ASIA':[],'EUROPE':[],'NORTH AMERICA':[],'OCEANIA':[],'SOUTH AMERICA':[]}
        #use for loop
        for country in countries:
            #use for loop to check each Country.continents
            for continent in country.continents:
                dict_continent[continent].append(country)
        #return dict_continent
        return dict_continent
    
    @staticmethod
    def get_total_historical_co2_emissions(countries,year):
        ''' (list,int) -> float
        The method returns a float representing the total co2 emissions
        produced by all the countries in the input list for all years up to and including the specified year.
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> Country.get_total_historical_co2_emissions([c,r],2007)
        5019.327
        >>> Country.get_total_historical_co2_emissions([c,p],2009)
        3729.89
        >>> Country.get_total_historical_co2_emissions([c,a],1997)
        3414.564
        '''
        #make result equal to 0.0
        result = 0.0
        #use for loop to add value to result
        for country in countries:
            result += country.get_historical_co2(year)
        #return result
        return result
    
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(countries,year):
        ''' (list,int) -> float
        The method returns the co2 emissions per capita in tonnes
        produced by the countries in the given list in the specified year.
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([c,r],2007),5)
        112.4897
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([c,p],2009),5)
        8.22228
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([c,a],1997),5)
        2.70567
        '''
        #make result_co2_emissions and result_population equals to 0.0
        result_co2_emissions = 0.0
        result_population = 0
        #use for loop to check each Country in list
        for country in countries:
            #use try block to avoid KerError and continue
            try:
                #check special cases 
                if country.co2_emissions[year] == 0.0 or country.population[year] == 0:
                    continue 
                result_co2_emissions += country.co2_emissions[year]
                result_population += country.population[year]
            except KeyError:
                continue
        #use try block to avoid ZeroDivisionError 
        try:
            #return result
            return result_co2_emissions * 1000000 / result_population
        except ZeroDivisionError:
            return 0.0
        
    @staticmethod
    def get_co2_emissions_per_capita_by_year(countries,year):
        ''' (list,int) -> dict
        The method returns a dictionary mapping objects of type Country to floats representing
        co2 emissions per capita in tonnes.
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> d1 = Country.get_co2_emissions_per_capita_by_year([c,r],2007)
        >>> round(d1[r],4)
        112.4897
        >>> d2 = Country.get_co2_emissions_per_capita_by_year([c,p],2009)
        >>> round(d2[p],5)
        8.22228
        >>> d3 = Country.get_co2_emissions_per_capita_by_year([c,a],1997)
        >>> round(d3[c],5)
        2.70567
        '''
        #make dict_co2 as an empty dictionary
        dict_co2 = {}
        #use for loop to make value to corresponding key in dict_co2
        for country in countries:
            dict_co2[country] = country.get_co2_per_capita_by_year(year)
        #return the dictionary
        return dict_co2

    @staticmethod
    def get_historical_co2_emissions(countries,year):
        ''' (list,int) -> dict
        The method returns a dictionary mapping objects of type Country to floats representing
        the total co2 emission for all years up to the input year.
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1997, 3414.549, 1261996032)
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> p = Country('POL', 'Poland', ['EUROPE'], 2009, 315.341, 38352000)
        >>> d1 = Country.get_historical_co2_emissions([c,r],2007)
        >>> d1[r]
        1604.778
        >>> d2 = Country.get_historical_co2_emissions([c,p],2009)
        >>> d2[p]
        315.341
        >>> d3 = Country.get_historical_co2_emissions([c,a],1997)
        >>> d3[c]
        3414.549
        '''
        #make an empty dictionary
        dict_historical_co2 = {}
        #use for loop to make value to corresponding key in dict_historical_co2
        for country in countries:
            dict_historical_co2[country] = country.get_historical_co2(year)
        #return the dictionary
        return dict_historical_co2
    
    @staticmethod
    def get_top_n(dict_countries,n):
        ''' (dict,int) -> list
        The mathod returns a list of tuples containing the iso code of a country and the number
        to which the country is mapped in the input dictionary.
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t1 = Country.get_top_n(d, 10)
        >>> t1[:5]
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        >>> t1[5:]
        [('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]
        >>> t2 = Country.get_top_n(d,3)
        >>> t2
        [('BOL', 10), ('IRL', 9), ('NZL', 8)]
        >>> t3 = Country.get_top_n(d,5)
        >>> t3
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        '''
        #make lists and dictionaries as follow
        top_list = []
        dict_new = {}
        list_new = []
        dict_name = {}
        #use for loop to get dict_name
        for key in dict_countries:
            dict_name[key.name] = key.iso_code
            #if value meet requirement then do as follow
            if dict_countries[key] in dict_new and key.iso_code not in dict_new[dict_countries[key]]:
                dict_new[dict_countries[key]].append(key.name)
                dict_new[dict_countries[key]].sort()
                continue
            #append value to top_list
            top_list.append(dict_countries[key])
            dict_new[dict_countries[key]] = [key.name]
        #use sort and get new_top_list
        top_list.sort()
        new_top_list = top_list[::-1]
        #use nest for loop to get list_new and return it if possible
        for num in new_top_list:
            for country in dict_new[num]:
                list_new.append((dict_name[country],num))
                if len(list_new) == n:
                    return list_new
        #return list_new
        return list_new   
                
def get_countries_from_file(filename):
    ''' (str) -> dict
    creates and returns a dictionary mapping ISO codes in file to objects of Country
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    
    >>> d2 = get_countries_from_file('small_data.tsv') #small_data is a file which I get from add_continents_to_data('small_clean_text.tsv', "iso_codes_by_continent.tsv","small_data.tsv")
    >>> len(d2)
    3
    
    >>> d3 = get_countries_from_file('large_data.tsv') #large_data is a file which I get from add_continents_to_data('large_clean_text.tsv', "iso_codes_by_continent.tsv","large_data.tsv")
    >>> len(d3)
    30
    '''
    #make an empty dictionary and open file
    dict_countries = {}
    fobj = open(filename,'r',encoding = 'utf-8')
    #use for loop to check each line in file
    for line in fobj:
        line = line.strip('\n')
        line_list = line.split('\t')
        #use if else to get correct Country(value) to corresponding key
        if line_list[0] in dict_countries:
            dict_countries[line_list[0]].add_yearly_data('\t'.join([line_list[3],line_list[4],line_list[5]]))
        else:
            dict_countries[line_list[0]] = Country.get_country_from_data(line)
    #close file
    fobj.close()
    #return the dictionary
    return dict_countries
#end