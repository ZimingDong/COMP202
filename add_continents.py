#Ziming Dong
#Student ID: 260951177

def get_iso_codes_by_continent(filename):
    ''' (str) -> dict
    The function returns a dictionary mapping continents'names to a list of ISO codes of countries
    that belongs to that continent.
    
    >>> d1 = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> len(d1['ASIA'])
    50
    >>> len(d1['NORTH AMERICA'])
    23
    >>> d1['AFRICA'][0]
    'NGA'
    >>> d1['EUROPE'][2]
    'BLR'
    
    >>> d2 = get_iso_codes_by_continent('text_1.tsv') #text_1 is a file which I created, it contain 13 ASIA countries and first one is CHN
    >>> len(d2['ASIA']
    13
    >>> d2['ASIA'][0]
    'CHN'
    
    >>> d3 = get_iso_codes_by_continent('text_2.tsv') #text_1 is a file which I created, it contain 30 EUROPE countries and second one is BLR
    >>> len(d3['EUROPE'])
    30
    >>> d3['EUROPE'][1]
    'BLR'
    '''
    #make dict_continent
    dict_continent = {'ASIA':[],'EUROPE':[],'AFRICA':[],'NORTH AMERICA':[],'OCEANIA':[],'SOUTH AMERICA':[]}
    #open file
    fobj = open(filename,'r',encoding = 'utf-8')
    #use for loop and append corresponding value to list
    for line in fobj:
        line = line.upper()
        line = line.strip()
        line_list = line.split('\t')
        dict_continent[line_list[1]].append(line_list[0])
    #close file
    fobj.close()
    #return dict_continent
    return dict_continent
    
def add_continents_to_data(input_filename,continents_filename,output_filename):
    ''' (str,str,str) -> int
    The function will read the input_filename,
    make changes to each of the lines and write the new version to output_filename.
    
    >>> add_continents_to_data("small_clean_co2_data.tsv", "iso_codes_by_continent.tsv","small_co2_data.tsv")
    10
    >>> add_continents_to_data('small_clean_text.tsv', "iso_codes_by_continent.tsv","small_data.tsv") #small_clean_text is a file I get from clean_one('small_tab_sep_text.tsv', 'small_clean_text.tsv')
    5
    >>> add_continents_to_data('large_clean_text.tsv', "iso_codes_by_continent.tsv","large_data.tsv") #large_clean_text is a file I get from clean_one('large_tab_sep_text.tsv', 'large_clean_text.tsv')
    50
    '''
    #open files
    fobj_1 = open(input_filename,'r',encoding = 'utf-8')
    fobj_2 = open(output_filename,'w',encoding = 'utf-8')
    #get dict_continents and key_list, make num equal to 0
    dict_continents = get_iso_codes_by_continent(continents_filename)
    key_list = list(dict_continents)
    num = 0
    #use for loop and do as fllow
    for line in fobj_1:
        continents = ''
        line_list = line.split('\t')
        #use for loop 
        for key in dict_continents:
            if line_list[0] in dict_continents[key]:
                #check special cases, such as contaion two continents
                if continents != '':
                    continents += ',' + str(key)
                    continue
                continents += str(key)
        #insert continents to right position and write new_line to file
        line_list.insert(2,continents)
        new_line = '\t'.join(line_list)
        fobj_2.write(new_line)
        #add 1 to num
        num += 1
    #close files    
    fobj_1.close()
    fobj_2.close()
    #return num
    return num
#end        








