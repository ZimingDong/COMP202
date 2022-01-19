#To type hello in your phone, you would have pressed the keys in the following order: 44-33-555-555-
#666. To denote the pauses you have to take between entering each series of numbers, we will be using
#space characters. So, the string '44 33 555 555 666' would be translated into 'hello'. To represent
#the mapping between a sequence of digits and the letter that it represents we will be using a dictionary.
#The dictionary will be mapping integers between 0 and 9 to lists of strings. The position of the string
#in the letter denotes how many times the integer should be repeated for it to represent such string. So,
#for instance the dictionary {2 : ['a', 'b', 'c'], 7 : ['p', 'q', 'r', 's']} tells us that to represent
#the string 'a' we need the integer 2 repeated once (because 'a' is the first string in the list to which the
#key 2 maps). On the other hand, to represent the string 'r' we need to use the integer 7 repeated three
#times, since 'r' is the third string in the list to which 7 maps

def same_chars(chars):
    ''' (str) -> bool
    check if string contains same chararcter
    >>> same_chars('COMP202')
    False
    >>> same_chars('aaaaaa')
    True
    >>> same_chars('aaaAaa')
    False
    '''
    #use a for loop to check if two adjacent elements are the same
    for i in range(len(chars)-1):
        if chars[i] != chars[i+1]:
            return False
    return True

def get_txt_msg(code,code_map):
    ''' (str,dict) - > str
    get message form dictionary
    >>> map_one = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], \
    5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], \
    8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z'], 0: [' ']}
    >>> code = '222 666 3 444 66 4 0 444 7777 0 333 88 66'
    >>> msg = get_txt_msg(code, map_one)
    >>> msg
    'coding is fun'
    
    >>> map_two = {0 : ['a ', 'the ', 'an '], 1 : ['lion ', 'bear ', 'cat '], \
    2 : ['is ', 'are ', 'has '], 3 : ['over ', 'under ', 'below ', 'in '], \
    4 : ['table ', 'forest ', 'tree ', 'cave ']}
    >>> s = '00 1 2 33 00 444'
    >>> get_txt_msg(s, map_two)
    'the lion is under the tree '
    
    >>> d = {2 : ['A', 'B', 'c'], 7 : ['p', 'q', 'r', 'S']}
    >>> get_txt_msg('222 2 777', d)
    'cAr'
    >>> get_txt_msg('227', d)
    Traceback (most recent call last):
    ValueError: Invalid input string
    
    '''
    #set digits and space character in a list
    digit_space = ['0','1','2','3','4','5','6','7','8','9',' ']
    #set an empty string for checking sequence 
    sequence = ''
    #make a list contain all keys in dictionary
    list_key = list(str((code_map)))
    #set an empty string to get message
    message = ''
    
    if code[0] == ' ' or code[-1] == ' ':
        #It begins or ends with space characters
        raise ValueError ('Invalid input string')
    #use for loop to check every elements in string and get its message
    for i in range(len(code)):
        if code[i:i+2] == '  ':
            #It contains two or more consecutive space characters raise ValueError
            raise ValueError ('Invalid input string')
        if code[i] not in digit_space:
            #It contains characters other than digits or space characters
            raise ValueError ('Invalid input string')
        if code[i] is not ' ':
            sequence += code[i]
        else:
            if same_chars(sequence):
                if sequence[0] not in list_key:
                    #It contains sequences of digits which cannot be translated using the input dictionary raise ValueError
                    raise ValueError ('Invalid input string')
                if len(sequence) > len(code_map[int(sequence[0])]):
                    #It contains sequences of digits which cannot be translated using the input dictionary raise ValueError
                    raise ValueError ('Invalid input string')
                #get message
                message += code_map[int(sequence[0])][len(sequence)-1]
                #reset sequence
                sequence = ''
                continue
            else:
                #It contains sequences built using different different digits
                raise ValueError ('Invalid input string')
    if same_chars(sequence):
        if sequence[0] not in list_key:
            #It contains sequences of digits which cannot be translated using the input dictionary raise ValueError
            raise ValueError ('Invalid input string')
        if len(sequence) > len(code_map[int(sequence[0])]):
            #It contains sequences of digits which cannot be translated using the input dictionary raise ValueError
            raise ValueError ('Invalid input string')
        message += code_map[int(sequence[0])][len(sequence)-1]
        sequence = ''
    else:
        #It contains sequences built using different different digits
        raise ValueError ('Invalid input string')
    return message 
    
    
map_one = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], \
           5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], \
           8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z'], 0: [' ']}
code = '222 666 3 444 66 4 0 444 7777 0 333 88 66'
msg_1 = get_txt_msg(code, map_one)
print(msg_1)

map_two = {0 : ['a ', 'the ', 'an '], 1 : ['lion ', 'bear ', 'cat '], \
           2 : ['is ', 'are ', 'has '], 3 : ['over ', 'under ', 'below ', 'in '], \
           4 : ['table ', 'forest ', 'tree ', 'cave ']}
code = '00 1 2 33 00 444'
msg_2 = get_txt_msg(code, map_two)
print(msg_2)
   
map_three = {0:[' '],1: ['13C','23C','33C'], 2: ['are','is'], \
             3:['a','an'],4:['amazing','great','awesome'],\
             5:['group','people']}   
code = '1 0 22 0 33 0 444 0 5'
msg_3 = get_txt_msg(code,map_three)
print(msg_3)
   