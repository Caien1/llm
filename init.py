import pprint
from typing import Union

def fetch_data_sets(file_name:str)->str:
    with open( file_name,"r") as file:
        data_set = file.read()
        return data_set

def vocab_generator(filtered_text_stream:str)->list:
    vocab = set()
    for char in filtered_text_stream:
        vocab.add(char)
    return list(vocab)

def word_freq_checker(filtered_text_stream:str)->dict:

    word_frequency = dict()
    words = filtered_text_stream.split(" ")
    for word in words:
        word = tuple(word)
        if word in word_frequency:
            word_frequency[word] +=1
        else:
            word_frequency[word] = 1

    return dict(sorted(word_frequency.items(),key=lambda item:item[1],reverse=True))


def pair_generator(tokens:dict)->dict:
    pair_freq = dict()
    for token in tokens.keys():
        for i in range(len(token)):
            if i == len(token)-1:
                break
            pair = token[i]+token[i+1]
            if pair in pair_freq:
                pair_freq[pair]+=1
            else:
                pair_freq[pair]=1

    return dict(sorted(pair_freq.items(),key=lambda item:item[1],reverse=True))
 
   
text = fetch_data_sets("d_set.txt") 
filtered_text_stream= text.replace('\n',' ') #cleaning up the newlines the 
vocab = vocab_generator(filtered_text_stream)
tokens = word_freq_checker(filtered_text_stream)
pairs = pair_generator(tokens=tokens)

max_pair = next(iter(pairs))
freq_max_pair = pairs[max_pair]
vocab.append(max_pair)

#
for token in tokens.keys():
    for i in range(len(token)):
        if max_pair[0] == token[i]:
        
            for i in range(len(max_pair)):
                pass



        

        

#print(max_pair,freq_max_pair,vocab)


# print(pairs)





    
