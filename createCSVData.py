import xml.etree.ElementTree as ET
from collections import Counter
import re
import csv

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
    with open('StackOverflow_2018_Data.csv', mode='w') as stackOverflow_2018_Data:
        stackoverflow_writer = csv.writer(stackOverflow_2018_Data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for child in root:
            if child.get('CreationDate') and '2018' == child.get('CreationDate')[:4] or child.get('LastActivityDate') and '2018' == child.get('LastActivityDate')[:4] or child.get('LastEditDate') and '2018' == child.get('LastEditDate')[:4]:
                if child.get('Tags') and 'pytorch' in child.get('Tags'):
                    results = re.findall(r'<(.+?)>', child.get('Tags'))
                    results.remove('pytorch')
                    creation_date = child.get('CreationDate')
                    post_id = child.get('Id')
                    for element in results:
                        if element == 'keras' or element == 'tensorflow':
                            continue
                        stackoverflow_writer.writerow([post_id, creation_date, 'pytorch', element])
            
                if child.get('Tags') and 'tensorflow' in child.get('Tags'):
                    results = re.findall(r'<(.+?)>', child.get('Tags'))
                    if 'tensorflow' not in results:
                        continue

                    results.remove('tensorflow')
                    creation_date = child.get('CreationDate')
                    post_id = child.get('Id')
                    for element in results:
                        if element == 'keras' or element == 'pytorch':
                            continue;
                        stackoverflow_writer.writerow([post_id, creation_date, 'tensorflow', element])
            
                if  child.get('Tags') and 'keras' in child.get('Tags'):
                    results = re.findall(r'<(.+?)>', child.get('Tags'))
                    if 'keras' not in results:
                        continue
                    results.remove('keras')
                    creation_date = child.get('CreationDate')
                    post_id = child.get('Id')
                    for element in results:
                        if element == 'tensorflow' or element == 'pytorch':
                            continue
                        stackoverflow_writer.writerow([post_id, creation_date, 'keras', element])
    
    
