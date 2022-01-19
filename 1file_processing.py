# Name: Yilin Lyu
# Student ID: 260952140

# import similarity_measures
from similarity_measures import *

# define global variables
punc = [".", "!", "?"]
punctuation = [',', '-', '--', ':', ';', '"', "'"]

def get_sentences(t):
    """ (str) -> list

    Given a string t
    a list of strings is returned
    with each string representing a sentence in the input string.
    
    >>> t = "All the sadness will disappear. No one is unhappy all the time."
    >>> get_sentences(t)
    ['All the sadness will disappear', 'No one is unhappy all the time']
    
    >>> t = "Life is like a box of chocolates. No one can be carefree all the time."
    >>> get_sentences(t)
    ['Life is like a box of chocolates', 'No one can be carefree all the time']
    
    >>> text = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text)
    ['No animal must ever kill any other animal', 'All animals are equal']
    """
    
    list_t = []
    sentence = ""

    for element in t:
        
        # if we do not encounter the elements in punc
        # this means that the sentence is not over yet
        if element not in punc:
            sentence += element
        
        else:# if we encounter the elements in punc
             # we need to use method strip to remove the punc
            sentence = sentence.strip()
            list_t.append(sentence)
            sentence = ""
    
    # check whether the last element of text is punc
    if t[-1] not in punc:
        list_t.append(sentence)

    return list_t


def get_word_breakdown(text):
    """ (str) -> list
    
    Given a string text returns a 2D lists of strings
    
    >>> text = "All the sadness will disappear. No one is unhappy all the time."
    >>> get_word_breakdown(text)
    [['all', 'the', 'sadness', 'will', 'disappear'], ['no', 'one', 'is', 'unhappy', 'all', 'the', 'time']]
    
    >>> text = "What they'll say about us?"
    >>> get_word_breakdown(text)
    [['what', 'they', 'll', 'say', 'about', 'us']]
    
    >>> text = "Life is like a box of chocolates. No one can be carefree all the time."
    >>> get_word_breakdown(text)
    [['life', 'is', 'like', 'a', 'box', 'of', 'chocolates'], ['no', 'one', 'can', 'be', 'carefree', 'all', 'the', 'time']]
    """
    
    # turn new line character into space
    text = text.replace("\n", " ")
    word_list = []
    sentences = get_sentences(text)

    for sentence in sentences:
        
        # remove every space which in the sentence
        sentence = sentence.strip()
        sentence_list = []
        word = ""
        
        for char in sentence:
            if char not in punctuation and char != " ":
                word += char.lower()

            else:# if char is not either a punctuation
                 # or a space, and the word is not an empty string
                if word != "":
                    sentence_list.append(word)
                word = ""
        word_list.append(sentence_list)
        
        # append the last word of the sentence into the list
        if word != "":
            sentence_list.append(word)

    return word_list


def build_semantic_descriptors_from_files(filenames):
    """ (list) -> dict
    
    Given a nested list called filenames as input
    returns a dictionary of the semantic descriptors
    of all the words in the files received as input
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> 'king' in d['clever']
    True
    >>> 'brothers' in d['clever']
    True
    >>> len(d['man'])
    21
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['all']['animal']
    1
    >>> d['habits']
    {'all': 1, 'the': 1, 'of': 1, 'man': 1, 'are': 1, 'evil': 1}
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['of']['man']
    1
    >>> d['man']
    {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'are': 1, 'evil': 1}
    """
    
    # assign the initial nest list is an empty list
    nest_lst = []
    
    for filename in filenames:
        fobj = open(filename, "r", encoding="utf-8")
        content = fobj.read()
        
        # remove some speicial characters from content
        strip_content = content.strip(' \t\n')
        fobj.close()

        nest_lst += get_word_breakdown(strip_content)

    dic = get_all_semantic_descriptors(nest_lst)

    return dic