#Ziming Dong
#Student ID: 260951177

#import similarity_measures module
from similarity_measures import*

def get_sentences(text):
    ''' (str) -> list
    given a string returns a list of strings each representing one of the sentences from the input string.
    >>> text1 = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text1)
    ['No animal must ever kill any other animal', 'All animals are equal']
    
    >>> text2 = "How are you? I'm fine, and you?"
    >>> get_sentences(text2)
    ['How are you', "I'm fine, and you"]
    
    >>> text3 = "How are you? I'm fine, and you? Me too."
    >>> get_sentences(text3)
    ['How are you', "I'm fine, and you", 'Me too']
    '''
    #set an empty string sequence and an empty list new_list
    sequence = ''
    new_list = []
    #set a list of special characters
    special_chars = ['.','!','?']
    #use for loop to save sequence or append sequence to new_list
    for i in text:
        if i not in special_chars:
            sequence += i 
        else:
            #remove white characters from sequence
            sequence = sequence.strip()
            new_list.append(sequence)
            #reset sequence as empty string
            sequence = ''
    #check special case if last character not in special_chars,then append sequence to new_list
    if text[-1] not in special_chars:
        new_list.append(sequence)
    #return new_list
    return new_list

def get_word_breakdown(text):
    ''' (str) -> list
    given a string returns a 2D lists of strings.
    Each sublist contains a strings representing words from each sentence.
    >>> text1 = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his \
    own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill \
    any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text1)
    >>> s == w
    True
    
    >>> text2 = "How are you? I'm fine, and you?"
    >>> get_word_breakdown(text2)
    [['how', 'are', 'you'], ['i', 'm', 'fine', 'and', 'you']]
    
    >>> text3 = "How are you? I'm fine, and you? Me too."
    >>> get_word_breakdown(text3)
    [['how', 'are', 'you'], ['i', 'm', 'fine', 'and', 'you'], ['me', 'too']]
    '''
    #set word_breakdown as an empty list
    word_breakdown = []
    #set skip_chars list for special character
    skip_chars = [',', '-', '--', ':', ';', '"', "'"]
    #set sentence_list as get_sentence(text)
    sentences_list = get_sentences(text)
    #use nest for loop to get result
    for sentence in sentences_list:
        #lower sentence and remove white characters from sentence
        sentence = sentence.lower()
        sentence = sentence.strip()
        #set sequence as empty list and word as empty string
        sequence = []
        word = ''
        #use this for loop to save word or append word to sequence
        for i in range(len(sentence)):
            #check special character
            if sentence[i] == '\n':
                if word == '':
                    continue
                sequence.append(word)
                word = ''
                continue
            if sentence[i] not in skip_chars and sentence[i] != ' ':
                word += sentence[i]
            else:
                if word == '':
                    continue
                sequence.append(word)
                word = ''
        #check special case if word not empty,then append word to sequence
        if word != '':
            sequence.append(word)
        #append sequence to word_breakdown to get nest list
        word_breakdown.append(sequence)
    #return word_breakdown
    return word_breakdown



def build_semantic_descriptors_from_files(s):
    ''' (list) -> dict
    given a list of file names (strings) as input,
    and returns a dictionary of the semantic descriptors of all the words in the files received as input,
    with the files treated as a single text.
    >>> d1 = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> 'king' in d1['clever']
    True
    >>> 'brothers' in d1['clever']
    True
    >>> len(d1['man'])
    21
    
    >>> d2 = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d2['animal']['must']
    3
    
    >>> d3 = build_semantic_descriptors_from_files(['alice.txt'])
    >>> d3['the']['king']
    4
    '''
    #open first file and turn it into a string
    fobj = open(s[0],'r',encoding = 'utf-8')
    file_content = fobj.read()
    #get nest list from first file
    sum_list = get_word_breakdown(file_content)
    #close first file
    fobj.close()
    #use for loop to get new_list(a nest list)
    for i in range(1,len(s)):
        fobj = open(s[i],'r',encoding = 'utf-8')
        file_content = fobj.read()
        new_list = get_word_breakdown(file_content)
        fobj.close()
        #append sublist to new_list
        for sublist in new_list:
            sum_list.append(sublist)
    #return result from get_all_semantic_descriptors(sum_list)
    return get_all_semantic_descriptors(sum_list)
#end



    


