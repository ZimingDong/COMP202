#Ziming Dong
#Student ID: 260951177

def find_delim(line):
    ''' （str) -> str
    The function takes a string as input representing a single line.
    A "delimiter" is a string that is used to separate columns of data on a single line.
    The function returns the most commonly used delimiter in the input string.
    
    >>> find_delim("cat\\tdog bat\\tcrab-cod")
    '\\t'
    >>> find_delim('You are so great,Bob')
    ' '
    >>> find_delim('1,2,3,4 5')
    ','
    '''
    #set dict_delim for 4 delimters
    dict_delim = {'\t':0, ',':0, ' ':0, '-':0}
    #set an empty dictionary and empty list
    dict_num = {}
    list_num = []
    #use for loop to check each character in line, if it is delimter,then add 1 to value in dict_delim
    for char in line:
        if char in dict_delim:
            dict_delim[char] += 1
    #use for loop to append value to list_num, and get dict_num
    for key in dict_delim:
        list_num.append(dict_delim[key])
        dict_num[dict_delim[key]] = key
    #find maximum number in list_num
    result_num = max(list_num)
    #return value in dict_num, when key is result_num
    return dict_num[result_num]

def clean_one(input_filename,output_filename):
    ''' (str,str) -> int
    The function takes as input two strings: the file name for a file to be read (input_filename),
    and file name for a file to be written (output_filename) respectively.
    The function will read the input_filename, make changes to each of the lines
    and write the new version to output_filename.
    
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10
    >>> clean_one('small_text.txt', 'small_tab_sep_text.tsv') #small_text is a file I created for testing, which contain 5 lines and 3 different countries
    5
    >>> clean_one('large_text.txt', 'large_tab_sep_text.tsv') #large_text is a file I created for testing, which contain 50 lines and 30 different countries
    50
    '''
    #open input and output file
    fobj_1 = open(input_filename,'r',encoding = 'utf-8')
    fobj_2 = open(output_filename,'w',encoding = 'utf-8')
    #make num equal to 0
    num = 0
    #use for loop to find most common delimter in each line and replace it with tab,num add 1, write line in output file
    for line in fobj_1:
        char = find_delim(line)
        line = line.replace(char,'\t')
        num += 1
        fobj_2.write(line)
    #close two file
    fobj_1.close()
    fobj_2.close()
    #return num
    return num
        
def final_clean(input_filename,output_filename):
    ''' (str,str) -> int
    The function takes as input two strings: the file name for a file to be read (input_filename),
    and file name for a file to be written (output_filename) respectively.
    The function will read the input_filename, make changes to each of the lines
    and write the new version to output_filename.
    
    >>> final_clean('small_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    10
    >>> final_clean('small_tab_sep_text.tsv', 'small_clean_text.tsv') #small_tab_sep_text is file I get from clean_one('small_text.txt', 'small_tab_sep_text.tsv')
    5
    >>> final_clean('large_tab_sep_text.tsv', 'large_clean_text.tsv') #large_tab_sep_text is file I get from clean_one('large_text.txt', 'large_tab_sep_text.tsv')
    50
    '''
    #open two files and make num equal to 0
    fobj_1 = open(input_filename,'r',encoding = 'utf-8')
    fobj_2 = open(output_filename,'w',encoding = 'utf-8')
    num = 0
    #use for loop to check each line, and make it into a list
    for line in fobj_1:
        line_list = line.split('\t')
        #if length of list is equal or less than 5, then do as follow
        if len(line_list) <= 5:
            if ',' in line:
                line = line.replace(',','.')
            fobj_2.write(line)
            num += 1
            continue
        #use for loop 
        for i in range(len(line_list)):
            #use try block to find year position
            try:
                int(line_list[i])
                #if year position is 2, which means before is no problem, so do as fllow
                if i is 2:
                    result = '.'.join(line_list[3:5])
                    new_line = '\t'.join([line_list[0],line_list[1],line_list[2],result,line_list[-1]])
                    fobj_2.write(new_line)
                    num += 1
                    break
                #get result_country and do as fllow                 
                result_country = ' '.join(line_list[1:i])
                if ',' in line_list[i+1]:
                    line_list[i+1] = line_list[i+1].replace(',','.')
                line = '\t'.join([line_list[0],result_country,line_list[i],line_list[i+1],line_list[i+2]])
                fobj_2.write(line)
                num += 1
                break
            #try block
            except ValueError:
                continue
    #close two file
    fobj_1.close()
    fobj_2.close()
    #return num
    return num
#end