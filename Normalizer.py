
'''
lemmatisation - find the root word
'''

sinhala_dictionary = "sinhala_dictionary.txt"

sinhala_dict = [str(l) for l in open(sinhala_dictionary)]
stem_dictionary = {}

for s in sinhala_dict:
    s = s.split("\t")
    stem_dictionary[s[0].strip()] = s[1].strip('\n')


# print(stem_dictionary)

def Normaliser(word):
    r = word if (stem_dictionary.get(word, word) == '')  else stem_dictionary.get(word, word)
    # print (word, r)
    return  r

