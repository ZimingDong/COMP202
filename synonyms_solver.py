#Ziming Dong
#Student ID: 260951177

#import similarity_measures module and file_processing module
from similarity_measures import*
from file_processing import*
#import matplotlib module
import matplotlib.pyplot as plt

def most_sim_word(word,choices,semantic_descriptors,similarity_fn):
    ''' (str,list,dict,function) -> str
    This function takes four inputs: a string word, a list of strings choices,
    and a dictionary semantic_descriptors which is built according to the requirements for get_all_semantic_descriptors,
    and a similarity function similarity_fn.
    The function returns the element of choices which has the largest semantic similarity to word,
    with the semantic similarity computed using the data in semantic_descriptors and the similarity function similarity_fn.
    >>> choices1 = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs1 = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices1, sem_descs1, get_cos_sim)
    'cat'
    
    >>> choices2 = ['apple', 'banana', 'pear']
    >>> o = {'sour' : 3, 'juice' : 5, 'tree' : 4}
    >>> a = {'tree' : 2, 'juice' : 5}
    >>> b = {'yellow' : 3, 'sweet' : 5, 'milkshake' : 8}
    >>> p = {'sweet' : 4, 'yellow' : 2}
    >>> sem_descs2 = {'orange' : o, 'apple' : a, 'banana' : b, 'pear' : p}
    >>> most_sim_word('orange', choices2, sem_descs2, get_cos_sim)
    'apple'
    
    >>> choices3 = ['orange', 'banana', 'pear']
    >>> o = {'sour' : 3, 'juice' : 5, 'tree' : 4}
    >>> a = {'tree' : 2, 'juice' : 5}
    >>> b = {'yellow' : 3, 'sweet' : 5, 'milkshake' : 8}
    >>> p = {'sweet' : 4, 'yellow' : 2}
    >>> sem_descs3 = {'orange' : o, 'apple' : a, 'banana' : b, 'pear' : p}
    >>> most_sim_word('apple', choices3, sem_descs3, get_norm_euc_sim)
    'orange'
    '''
    #set value and answer from first choice
    try:
        value = similarity_fn(semantic_descriptors[choices[0]],semantic_descriptors[word])
    except KeyError:
        value = float('-inf')
    answer = choices[0]
    #use for loop to get new_value and compare with value,select the bigger one corresponding answer as answer
    for i in choices:
        #use try block to avoid KeyError and consider special cases
        try:
            new_value = similarity_fn(semantic_descriptors[i],semantic_descriptors[word])                
        except KeyError:
            new_value = float('-inf')
        finally:
            if new_value > value:
                value = new_value
                answer = i
    #check special cases
    if value == float('-inf'):
        return ''
    #return answer    
    return answer
        
    
def run_sim_test(filename,semantic_descriptors,similarity_fn):
    ''' (str,dict,function) -> float
    This function takes three inputs: a string filename,
    a dictionary semantic_descriptors, and a function similarity_fn.
    The function returns the percentage of questions on which
    most_sim_word guesses the answer correctly using the semantic descriptors stored in semantic_descriptors,
    and the similarity function similarity_fn.
    >>> descriptors1 = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors1, get_cos_sim)
    15.0
    
    >>> descriptors2 = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors2, get_euc_sim)
    20.0
    
    >>> descriptors3 = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors3, get_norm_euc_sim)
    15.0
    '''
    #open file and set sequence,key_line,right_result and num_result
    fobj = open(filename,'r',encoding = 'utf-8')
    sequence = ''
    key_line = []
    right_result = 0
    num_result = 0
    #use for loop to check result from each line in file
    for line in fobj:
        new_line = line.strip()
        #use for loop to get key_line
        for char in new_line:
            if char is not ' ':
                sequence += char
            else:
                sequence = sequence.strip()
                key_line.append(sequence)
                sequence = ''
        sequence = sequence.strip()
        key_line.append(sequence)
        sequence = ''
        #get word and answer and remove them from key_line
        word = key_line[0]
        answer = key_line[1]
        key_line.remove(word)
        key_line.remove(answer)
        #get result and num_result plus 1
        result =  most_sim_word(word,key_line,semantic_descriptors,similarity_fn)
        num_result += 1
        key_line = []
        #check if result is correct,then right_result plus 1
        if result == answer:
            right_result += 1
    #close the file 
    fobj.close()
    #return the percentage
    return round(float(right_result/num_result)*100,1)


def generate_bar_graph(similarity_fns,filename):
    ''' (list,str) -> Void
    given a list of similarity functions,
    and a string filename generates a bar graph,
    where the performance of each function on the given file test is plotted.
    '''
    #set functions and percentage
    functions = []
    percentage = []
    #set descriptors from two text
    descriptors = build_semantic_descriptors_from_files(['war_and_peace.txt', 'swanns_way.txt'])
    #use for loop to append x-axis and y-axis values to functions and percentage
    for similarity_fn in similarity_fns:
        functions.append(similarity_fn.__name__)
        percentage.append(run_sim_test('test.txt', descriptors, similarity_fn))
    #creat a bar graph and name title   
    plt.bar(functions,percentage)
    plt.title('Correct percentage of test')
    #save bar graph
    plt.savefig('synonyms_test_results.png')
#end