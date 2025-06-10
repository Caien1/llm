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


def max_freq_pair(tokens:dict)->str:
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

    return max(pair_freq.items(),key=lambda item:item[1])[0]
 
def merge_pairs(tokens:dict,pairs:str)->dict:

    new_tokens = tokens.copy()

    for token in tokens.keys():
        for i in range(len(token)):
            if( i==len(token)-1):
                break
            if( "".join((token[i],token[i+1]))==pairs):
                new_token = tuple(list(token)[:i] +[pairs]+list(token[i+len(pairs):]))
                value = new_tokens.pop(token)
                new_tokens.update({new_token:value})

    return dict(sorted(new_tokens.items(),key=lambda item:item[1],reverse=True))


text = fetch_data_sets("d_set.txt") 
filtered_text_stream= text.replace('\n',' ') #cleaning up the newlines the 
vocab = vocab_generator(filtered_text_stream)
tokens = word_freq_checker(filtered_text_stream)
pairs = max_freq_pair(tokens=tokens)
print(pairs)
new_tokens= merge_pairs(tokens,pairs)

vocab.append(pairs)


    




print(new_tokens,vocab,sep="\n")
# Tasks done till now
#Gernrate Vocab
# Make tokens of the words used in the d_set
#Find out Max freq pairs
#add max freq pair to vocab

# merge the pairs to reduce token size in a way

#TODO(caien) Test for bugs it seems there are a few but not sure 
#TODO()check for optimisation
