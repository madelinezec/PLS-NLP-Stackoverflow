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
        '''
        pytorch_doc = []
        tensorflow_doc = []
        cotag_list = []
        keras_doc = []
        counte = 0
        for row in csv_reader:
            if row[2] == 'keras':
            	keras_doc.append(row[3])
            if row[2] == 'pytorch':
             	pytorch_doc.append(row[3])
            if row[2] == 'tensorflow':
             	tensorflow_doc.append(row[3])
    print(keras_doc[0:10])
    print("BREAK")
    print(pytorch_doc[0:10])
    print("BREAK")
    print(tensorflow_doc[0:10])
    '''
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
    '''
    with open("StackOverflow_2018_Data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open("StackOverflow_2018_TFIDF_Data.csv", "w") as csv_output:
            appended_row = []
            writer = csv.writer(csv_output, lineterminator='\n')
            for row in csv_reader:
                if row[2] == 'keras':
                    row.append(keras_dict[row[3]])
                    appended_row.append(row)
                if row[2] == 'pytorch':
                    row.append(pytorch_dict[row[3]])
                    appended_row.append(row)
                if row[2] == 'tensorflow':
                    row.append(tensorflow_dict[row[3]])
                    appended_row.append(row)
            writer.writerows(appended_row)
    '''
if __name__ == '__main__':
    main()
