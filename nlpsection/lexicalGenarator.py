from nlpsection.Normalizer import Normaliser
import re
import csv

'''
Pre Process meta data Input 
'''
outPut_file = open('meta_data_post_process.csv', 'w')
writer = csv.writer(outPut_file)

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

        rootWord = Normaliser(j[0])

        j.insert(1, rootWord)

        writer.writerow(j)


outPut_file.close()

 # සිසුන්ගේ ලකුණු දෙන්න
