
stopwords = []


with open('/Users/sskmal/Documents/Nlpk/NlpkPhaseOne/nlpsection/StopWords_425.txt', encoding='utf-16') as f:
    for i in f:
        s = i.split("\t")
        stopwords.append(s[0])

# for i in list_of_words:
#     s = s.split("\t")
#     stopwords.append(s[0])

print(stopwords)
def get_stopwordlist():

    return stopwords
