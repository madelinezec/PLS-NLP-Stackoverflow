from __future__ import division
import json
import csv
from collections import Counter
import math

def main():
    with open("StackOverflow_2018_Data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        pytorch_counter = Counter()
        tensorflow_counter = Counter()
        cotag_list = []
        keras_counter = Counter()
        counte = 0
        for row in csv_reader:
            if row[2] == 'keras':
            	keras_counter[row[3]] += 1
            if row[2] == 'pytorch':
             	pytorch_counter[row[3]] += 1
            if row[2] == 'tensorflow':
             	tensorflow_counter[row[3]] += 1
            if row[3] not in cotag_list:
                cotag_list.append(row[3])
            counte += 1
    pytorch_sum = sum(pytorch_counter.values())
    keras_sum = sum(keras_counter.values())
    tensorflow_sum = sum(tensorflow_counter.values())
    pytorch_dict = {}
    tensorflow_dict = {}
    keras_dict = {}
    for cotag in cotag_list:
        num_docs = 0.0
        if cotag in pytorch_counter:
            num_docs += 1.0
        if cotag in keras_counter:
            num_docs += 1.0
        if cotag in tensorflow_counter:
            num_docs += 1.0
        if cotag in pytorch_counter:
            tf = pytorch_counter[cotag]/pytorch_sum
            idf = math.log(3/num_docs)
            pytorch_dict[cotag] = tf * idf
        if cotag in keras_counter:
            tf = keras_counter[cotag]/keras_sum
            idf = math.log(3/num_docs)
            keras_dict[cotag] = tf * idf
        if cotag in tensorflow_counter:
            tf = tensorflow_counter[cotag]/tensorflow_sum
            idf = math.log(3/num_docs)
            tensorflow_dict[cotag] = tf * idf
    with open("COTAG_TFIDF_Data.csv", "w") as csv_output:
        writer = csv.writer(csv_output, lineterminator='\n')
        for cotag in cotag_list:
            if cotag in pytorch_dict:
                writer.writerow([cotag, "pytorch", pytorch_dict[cotag]])
            if cotag in keras_dict:
                writer.writerow([cotag, "keras", keras_dict[cotag]]) 
            if cotag in tensorflow_dict:
                writer.writerow([cotag, "tensorflow", tensorflow_dict[cotag]])

if __name__ == '__main__':
    main()
