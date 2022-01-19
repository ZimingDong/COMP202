#Ziming Dong
#Student ID: 260951177

#import math module for function
from math import*
def add_vectors(dict_1,dict_2):
    ''' (dict,dict) -> Void
    given two dictionaries representing vectors, it adds the second vector to the first one.
    And modifies only the first input dictionary.
    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1
    {'a': 2, 'b': 3, 'c': 1}
    
    >>> v3 = {'a' : 1}
    >>> v4 = {'b' : 2}
    >>> add_vectors(v3, v4)
    >>> len(v3)
    2
    >>> v3
    {'a': 1, 'b': 2}
    
    >>> v5 = {'a' : 1, 'b' : 3, 'c' : 2}
    >>> v6 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v5, v6)
    >>> len(v5)
    3
    >>> v5
    {'a': 2, 'b': 3, 'c': 3}
    '''
    #make a list of keys of dict_1
    key_list_dict1 = list(dict_1)
    #use for loop 
    for k in dict_2:
        #check if key in dict_2 in dict_1
        if k in key_list_dict1:
            #if True then change key in dict_1
            dict_1[k] = dict_1[k] + dict_2[k]
        else:
            #else add key to dict_1
            dict_1[k] = dict_2[k]
        
        
def sub_vectors(dict_1,dict_2):
    ''' (dict,dict) -> dict
    given two dictionaries representing vectors, it returns a dictionary,
    which is the result of subtracting the second vector from the first one.
    >>> d1 = {'a' : 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c' : -1}
    True
    >>> d1 == {'a' : 3, 'b': 2}
    True
    >>> d2 == {'a': 2, 'c': 1, 'b': 2}
    True
    
    >>> d3 = {'a' : 3, 'b': 2 , 'c': 1}
    >>> d4 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d3, d4)
    >>> d
    {'a': 1}
    
    >>> d5 = {'a': 2, 'c': 1, 'b': 2}
    >>> d6 = {'a' : 3, 'b': 2}
    >>> d = sub_vectors(d5, d6)
    >>> d
    {'a': -1, 'c': 1}
    '''
    #set an empty dictionary
    dict_new = {}
    #make lists of keys of dict_1 and dict_1
    key_list_dict1 = list(dict_1)
    key_list_dict2 = list(dict_2)
    #use for loop to check keys in dict_1
    for k in dict_1:
        #check if keys in dict_1 also in dict_2
        if k in key_list_dict2:
            #if True then caclulate new_value for key
            new_value = dict_1[k] - dict_2[k]
            #if new_value equal to 0, then continue
            if new_value == 0:
                continue
            else:
                #else set dict_new key as value new_value
                dict_new[k] = new_value
        else:
            #if key not in dict_2,then set dict_new key as corresponding value in dict_1
            dict_new[k] = dict_1[k]
    #use for loop to check keys in dict_2
    for k in dict_2:
        #check if key not in dict_1
        if k not in key_list_dict1:
            #dict_new key as negative corresponding value in dict_2
            dict_new[k] = -dict_2[k]
    #return dict_new
    return dict_new

def merge_dicts_of_vectors(dict_1,dict_2):
    ''' (dict,dict) -> Void
    given two dictionaries containing values which are dictionaries representing vectors,
    the function modifies the first input by merging it with the second one.
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya': 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> d1['a'] == {'apple': 2}
    True
    >>> d1['p'] == {'pear': 1, 'plum': 3, 'papaya' : 6}
    True
    >>> d2 == {'p' : {'papaya': 6}}
    True
    
    >>> d3 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d4 = {'p' : {'papaya' : 6, 'orange' : 4}}
    >>> merge_dicts_of_vectors(d3, d4)
    >>> d3
    {'a': {'apple': 2}, 'p': {'pear': 1, 'plum': 3, 'papaya': 6, 'orange': 4}}
    
    >>> d5 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d6 = {'p' : {'pear': 6}}
    >>> merge_dicts_of_vectors(d5, d6)
    >>> d5
    {'a': {'apple': 2}, 'p': {'pear': 7, 'plum': 3}}
    '''
    #make a list of keys in dict_1
    key_list_dict1 = list(dict_1)
    #use for loop to check keys in dict_2
    for k in dict_2:
        #if key in list,then use add_vectors to get corresponding value for key
        if k in key_list_dict1:
            add_vectors(dict_1[k],dict_2[k])
            dict_1[k] = dict_1[k]
        else:
            #else get corresponding value in dict_2
            dict_1[k] = dict_2[k]
            
def get_dot_product(dict_1,dict_2):
    ''' (dict,dict) -> int
    given two dictionaries representing vectors,returns the dot product of the twovectors.
    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10
    
    >>> v3 = {'a' : 3, 'b': 2, 'c':3}
    >>> v4 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v3, v4)
    13
    
    >>> v5 = {'c': 3}
    >>> v6 = {'a': 2, 'b': 2}
    >>> get_dot_product(v5, v6)
    0
    '''
    #set sum_result as 0
    sum_result = 0
    #make a list of keys in dict_2
    key_list_dict2 = list(dict_2)
    #use for loop
    for k in dict_1:
        #if key in list,then get sum_result plus value of key in dict_1 and dict_2 product
        if k in key_list_dict2:
            sum_result += dict_1[k] * dict_2[k]
    #return sum_result
    return sum_result

def get_vector_norm(vector):
    ''' (dict) -> float
    given a dictionary representing a vector, returns the norm of such vector.
    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0
    
    >>> v2 = {'a' : 12, 'b': 5}
    >>> get_vector_norm(v2)
    13.0
    
    >>> v3 = {'a' : 1, 'b': 1}
    >>> round(get_vector_norm(v3),1)
    1.4
    '''
    #set number as 0
    number = 0
    #use for loop to get sum 
    for k in vector:
        number += vector.get(k)**2
    #return sqrt of number
    return sqrt(number)

def normalize_vector(vector):
    ''' (dict) -> Void
    given a dictionary representing a vector, the function modifies the dictionary by dividing each value by the norm of the vector.
    >>> v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6
    >>> v1['b']
    0.8
    
    >>> v2 = {'a' : 5, 'b': 12}
    >>> normalize_vector(v2)
    >>> round(v2['a'],3)
    0.385
    >>> round(v2['b'],3)
    0.923
    
    >>> v3 = {'a' : 1, 'b': 1, 'c':2}
    >>> normalize_vector(v3)
    >>> round(v3['c'],3)
    0.816
    '''
    #get vector normalize of vector
    vector_norm = get_vector_norm(vector)
    #use for loop to continue
    for k in vector:
        #if value is 0,then break
        if vector[k] == 0:
            break
        #if not change key to corresponding value of vector
        vector[k] = vector[k]/vector_norm
#end

    
    
    
    
