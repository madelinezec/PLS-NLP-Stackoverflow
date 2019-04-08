import xml.etree.ElementTree as ET
from collections import Counter
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    tree = ET.parse('Posts.xml')
    root = tree.getroot()
    cnt = Counter()
    cnt_posts = 0

    for child in root: 
        if child.get('Tags') and 'pytorch' in child.get('Tags') or child.get('Tags') and 'tensorflow' in child.get('Tags') or child.get('Tags') and 'keras' in child.get('Tags'):
            results = re.findall(r'<(.+?)>', child.get('Tags'))
            cnt_posts += 1
            for tag in results:
                if tag != 'pytorch' and tag != 'keras' and tag != 'tensorflow':
                    cnt[tag] += 1
  #  print(cnt_posts)
 #   print(len(cnt.keys()))
    num_plots = 10
    cnt = {k:v for k,v in cnt.items() if v > 1.0}
    df = pd.DataFrame.from_dict(cnt, orient='index')
    sample_size = int(len(df.index)/ num_plots)
#    print(len(df.index))

    for i, n in enumerate(np.linspace(0, len(df.index), num_plots+1, dtype=int)[:-1]):
        fig = plt.figure()
        df.iloc[n:n+sample_size, :].plot(kind='bar')
    # … format your figure here
        plt.rcParams["figure.figsize"] = (100,16)
#        plt.yticks(np.range(0, 30000, 1000.0))
        plt.savefig('histogram_{}.png'.format(i))
        plt.close()
#    plt.rcParams.update({'font.size': 4})    

