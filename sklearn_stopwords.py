from __future__ import division
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import csv
from collections import Counter
import math

def main():
    with open("StackOverflow_2018_Data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        pytorch_doc = ''
        tensorflow_doc = ''
        cotag_list = []
        keras_doc = ''
        counte = 0
        for row in csv_reader:
            if row[2] == 'tensorflow':
            	tensorflow_doc += row[3] + ' '
            if row[2] == 'keras':
            	keras_doc += row[3] + ' '
            if row[2] == 'pytorch':
                pytorch_doc += row[3] + ' '

    corpus = [pytorch_doc, tensorflow_doc, keras_doc]
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(corpus)
    x.toarray()
    ict = []
    feat = vectorizer.get_feature_names()
    for i,arr in enumerate(x.toarray()):
        for x, ele in enumerate(arr):
            if i == 0:
                ict.append(('pytorch', feat[x], ele))
            if i == 1:
                ict.append(('tensorflow', feat[x], ele))
            if i == 2:
                ict.append(('keras', feat[x], ele))
    sorted_arr = sorted(ict, key=lambda tup: tup[2])
    print(sorted_arr[-10:])
    #print(vectorizer.get_stop_words())
    keras_dict = {}
    with open("termFrequencies.csv", "w") as csvFile:
        writer = csv.writer(csvFile, lineterminator='\n')
        appended_row = []
        for ele in reversed(sorted_arr):
            print(ele)
            appended_row.append(ele)

        writer.writerows(appended_row)

if __name__ == '__main__':
    main()
