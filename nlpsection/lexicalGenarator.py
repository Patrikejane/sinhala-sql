from nlpsection.Normalizer import Normaliser
from nlpsection.MetaDataExtractor import MetaDataExtractor
import re
import csv

'''
Pre Process meta data Input 
'''

outPut_file = open('meta_data_post_process.csv', 'w')
writer = csv.writer(outPut_file)

normalizer = Normaliser("/Users/sskmal/Documents/Nlpk/NlpkPhaseOne/nlpsection/sinhala_dictionary.txt")

user, password, host, database = 'root', 'sunimalroot', '127.0.0.1', 'nlpDb'
metadata_extractor = MetaDataExtractor(user, password, host, database)
metadata_Dictionary = metadata_extractor.getDbMetadataDict()

with open('Lexicon_updated.csv', 'r') as file:
    headerline = file.readline().split(',')[1::]
    headerline.insert(1, 'Root_word')
    writer.writerow(headerline)
    print(headerline)
    for i in file:
        # i.encode('utf-8')
        j = i.split(',')[1::]

        j[-1] = j[-1].strip('\n')
        regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
        j[0] = regex.sub('', j[0])

        rootWord = normalizer.normalise(j[0])

        j.insert(1, rootWord)

        writer.writerow(j)

    # for k,v in metadata_Dictionary:
    #     print(k)
    #     print(v)

    for key, val in metadata_Dictionary.items():
        keyrow = []
        keysinhalaword, keyrootword, keysqlsyntax, keysemeticmean = key[0], normalizer.normalise(key[0]), key[0], key[1]
        keyrow.extend([keysinhalaword, keyrootword, keysqlsyntax, keysemeticmean])
        writer.writerow(keyrow)
        for j in val:
            valrow = []
            valsinhalaword, valrootword, valsqlsyntax, valsemeticmean = j[0], normalizer.normalise(j[0]), j[0], j[1]
            valrow.extend([valsinhalaword, valrootword, valsqlsyntax, valsemeticmean])
            writer.writerow(valrow)
        print(key, "=>", val)

outPut_file.close()

# සිසුන්ගේ ලකුණු දෙන්න
