# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:40:04 2019

@author: amy_s
"""
def languagefrequency(filename):
    with open(filename, encoding = 'utf-8') as file_object:
        contents = file_object.read()
    s = contents.split()
    list =[]
    for word in s:
        x = word.lower().strip('¡¿!-?¡#“_.:')
        list.append(x)
        
    counts ={}
    for word in list:
        if not word in counts:
            counts[word] =0
        counts[word] += 1
    
    sorted_counts = sorted(counts.items(), key = lambda kv: kv[1], reverse = True)
    
    most_frequent = dict(sorted_counts[:11])
    
    for word in most_frequent.keys():
        most_frequent[word] = most_frequent[word]/len(sorted_counts)
    
    return most_frequent
    
    for key, value in most_frequent.keys():
        print((key,value))
    
english = languagefrequency('eaton-boy-scouts_EN.txt')
spanish = languagefrequency('cherbonnel-mi-tio_SP.txt')
german = languagefrequency('schloemp-tolle-koffer_DE.txt')
unknown = languagefrequency('unknown-lang.txt')
    
for u in unknown.keys():
    sp = spanish.get(u,0)
    u = unknown.get(u,0)
    sp_dif=abs(sp-u)
    print(sp_dif)
for u in unknown.keys():
    en = english.get(u,0)
    u = unknown.get(u,0)
    eng_dif=abs(en-u)
    print(eng_dif)
for u in unknown.keys():
    uk = unknown.get(u,0)
    ger = german.get(u,0)
    germ=abs(ger-uk)
    print(germ)


    
print(cmp(english,unknown))
print(languagefrequency('eaton-boy-scouts_EN.txt'))
print("These are the most frequent words in Spanish file ", languagefrequency('cherbonnel-mi-tio_SP.txt'))
print("These are the most frequent words in German ", languagefrequency('schloemp-tolle-koffer_DE.txt'))
print("These are the most frequent words in ", languagefrequency('unknown-lang.txt'))