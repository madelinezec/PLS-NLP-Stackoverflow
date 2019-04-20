import xml.etree.ElementTree as ET

if __name__ == '__main__':
    posts = ET.Element('data')
    tree = ET.parse('Posts.xml')
    root = tree.getroot()
   
    for child in root:
        if child.get('Tags') and 'pytorch' in child.get('Tags') or child.get('Tags') and 'tensorflow' in child.get('Tags') or child.get('Tags') and 'keras' in child.get('Tags'):
        	posts.append(child)
    
    mydata = ET.tostring(posts).decode()
    myfile = open("subposts.xml", "w")
    myfile.write(mydata)
