from random import*
fruits = ['banana','strawberry','apple','pear','watermelon','mango','grape']
caclulat_dict = {'banana':0,'strawberry':0,'apple':0,'pear':0,'watermelon':0,'mango':0,'grape':0}
for i in range(100):
    position = randint(0,6)
    caclulat_dict[fruits[position]] = caclulat_dict[fruits[position]] + 1
    
def get_word_breakdown(text):
    sum_list = []
    new_list = []
    sentence = ''
    sequence = ''
    special_chars = ['.','!','?',]
    skip_chars = [',', '-', '--', ':', ';', '"', "'"]
    for i in text:
        if i in skip_chars:
            continue
        if i not in special_chars:
            sentence += i
        else:
            sentence = sentence.lower()
            sentence = sentence.strip()
            for char in sentence:
                if char not in skip_chars and char is not ' ':
                    sequence += char
                else:
                    if sequence == '':
                        continue
                    else:
                        sequence = sequence.strip()
                        new_list.append(sequence)
                        sequence = ''
            new_list.append(sequence)
            sequence = ''
            sentence = ''
            sum_list.append(new_list)
            new_list = []
    if len(sentence) > 1:
        for char in sentence:
                if char not in skip_chars and char is not ' ':
                    sequence += char
                else:
                    if sequence == '':
                        continue
                    else:
                        sequence = sequence.strip()
                        new_list.append(sequence)
                        sequence = ''
        new_list.append(sequence)
        sequence = ''
        sentence = ''
        sum_list.append(new_list)
        new_list = []
        
    return sum_list