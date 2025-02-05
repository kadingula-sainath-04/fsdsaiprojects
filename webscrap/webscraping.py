import os
os.chdir(r'D:\FULLSTACK DATASCIECE AND AI\Classroomwork\ARTIFICIALINTELLIGENCE\NATURAL LANGUAGE PROCESSING\NLPPTOJECTS\webscrap')
import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml")
root = tree.getroot()

root = ET.tostring(root,encoding='utf8').decode('utf8')

root


import re,string,unicodedata

import nltk

from bs4 import BeautifulSoup

def strip_html(text):
    soup = BeautifulSoup(text,'xml')
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]','',text)


def denoise_text(text):
    text = strip_html(text)
    text=remove_between_square_brackets(text)
    text = re.sub('  ','',text)
    return text

sample = denoise_text(root)
print(sample)




