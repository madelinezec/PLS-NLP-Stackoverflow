import xml.etree.ElementTree as ET
from collections import Counter
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    tree = ET.parse('subposts.xml')
    root = tree.getroot()
    cnt = Counter()
    cnt_posts = 0
    co_occurent_pytorch = Counter()
    co_occurent_tensorflow = Counter()
    co_occurent_keras = Counter()
    cnt_pytorch = 0
    cnt_keras = 0
    cnt_tensorflow = 0
    for child in root:
        if child.get('CreationDate') and '2018' == child.get('CreationDate')[:4] or child.get('LastActivityDate') and '2018' == child.get('LastActivityDate')[:4] or child.get('LastEditDate') and '2018' == child.get('LastEditDate')[:4]:
            if child.get('Tags') and 'pytorch' in child.get('Tags'):
                results = re.findall(r'<(.+?)>', child.get('Tags'))
                results.remove('pytorch')
            
                for element in results: 
                    co_occurent_pytorch[(element)] += 1
        
            if child.get('Tags') and 'tensorflow' in child.get('Tags'):
                results = re.findall(r'<(.+?)>', child.get('Tags'))
                if 'tensorflow' not in results:
                    continue

                for element in results:
                    co_occurent_tensorflow[element] += 1
            
            if  child.get('Tags') and 'keras' in child.get('Tags'):
                results = re.findall(r'<(.+?)>', child.get('Tags'))
                if 'keras' not in results:
                    continue
                for element in results:
                    co_occurent_keras[element] += 1
    
    pf = open("pytorchFreq.txt", 'w+')
    tf = open("tensorflowFreq.txt", 'w+')
    kf = open("kerasFreq.txt", 'w+')

    for element in co_occurent_pytorch:
        pf.write(element + " ," + str(co_occurent_pytorch[element]) + '\n')
   
    for element in co_occurent_tensorflow:
        tf.write(element + " ," + str(co_occurent_tensorflow[element]) + '\n')
   
    for element in co_occurent_keras:
        kf.write(element + " ," + str(co_occurent_keras[element]) + '\n')
    pf.close()
    tf.close()
    kf.close()
    
