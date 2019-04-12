import nltk
import nltk.tag, nltk.data
import re
from sklearn.externals import joblib



# model = {'මිනිස්සුන්': 'T','කුරුල්ලන්':'T','ගස':'Attr','ලගින':'O','කපන':'O'}
tagger_model = {}
with open('meta_data_post_process.csv') as post_p_file:

    headerline = post_p_file.readline()
    for i in post_p_file:
        singleline = i.rstrip("\n").split(',')
        if len(singleline) == 4 :
            tagger_model[singleline[1]] = singleline[3]
        else:
            print("Invalid row : ", singleline)




default_tagger = nltk.DefaultTagger('unknown')
tagger = nltk.tag.UnigramTagger(model=tagger_model, backoff=default_tagger)


joblib.dump(tagger, 'posTagger.pkl')
