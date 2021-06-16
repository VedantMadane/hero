#pip install urllib3
#pip install bs4
from heapq import nlargest
from typing import DefaultDict
import urllib
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk
from nltk.probability import FreqDist
#nltk.download('punkt')

parva_part=''
parva_number=str(input(print("Select a Parva from 01 to 18")))
if parva_number=='01':
    page_number=str(input(print(f"You have selected the Ādi Parva. Now select a number from 000 to 237:")))
elif parva_number=='02':
    page_number=str(input(print(f"That is the Sabhā Parva. Now select a number from 000 to 080:")))
elif parva_number=='03':
    page_number=str(input(print(f"That would be the Vana Parva. Now select a number from 000 to 313:")))
elif parva_number=='04':
    page_number=str(input(print(f"That would be the Virāṭa Parva. Now select a number from 000 to 072:")))
elif parva_number=='05':
    page_number=str(input(print(f"That would be the Udyoga Parva. Now select a number from 000 to 191:")))
elif parva_number=='06':
    page_number=str(input(print(f"That would be the Bhīṣma Parva. Now select a number from 000 to 124:")))
elif parva_number=='07':
    page_number=str(input(print(f"That would be the Droṇa Parva. Now select a number from 000 to 199:")))
elif parva_number=='08':
    page_number=str(input(print(f"That would be the Karṇa Parva. Now select a number from 000 to 096:")))
elif parva_number=='09':
    page_number=str(input(print(f"That would be the Śalya Parva. Now select a number from 000 to 065:")))
elif parva_number=='10':
    page_number=str(input(print(f"That would be the Sauptika Parva. Now select a number from 000 to 018:")))
elif parva_number=='11':
    page_number=str(input(print(f"That would be the Strī Parva. Now select a number from 000 to 026:")))
elif parva_number=='12':
  parva_part=str(input(print("That would be the Śanti Parva. Type a for Part A, b for Part B or c for Part C:")))
  if parva_part == 'a':
    page_number=print("Select a number from 000 to 172")
  elif parva_part== 'b':
    page_number=print("Select a number from 000 to 128")
  else:
    page_number=print("Select a number from 000 to 063")
elif parva_number=='13':
    parva_part=str(input(print(f"That would be the Anuśāsana Parva. Now Type a for Part A or b for Part B:")))
    if parva_part=='a':
      print('Select a number from 000 to 035')
    else:
      print('Select a number from 000 to 133')
elif parva_number=='14':
    page_number=str(input(print(f"That would be the Aśvamedha Parva. Now select a number from 000 to 092:")))
elif parva_number=='15':
    page_number=str(input(print(f"That would be the Āśramavāsika Parva. Now select a number from 000 to 039:")))
elif parva_number=='16':
    page_number=str(input(print(f"That would be the Mausala Parva. Now select a number from 000 to 008:")))
elif parva_number=='17':
    page_number=str(input(print(f"That would be the Mahāpratiṣṭhānika Parva. Now select a number from 000 to 003:")))
else:
    page_number=str(input(print(f"That would be the Svargārohaṇa Parva. Now select a number from 000 to 006:")))


PageURL = f'https://www.sacred-texts.com/hin/m{parva_number}/m{parva_number}{parva_part}{page_number}.htm'


"""
page = urllib.request.urlopen(PageURL).read().decode('utf8','ignore') 
soup = BeautifulSoup(page,"lxml")
soup.find('p').text
text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
"""

def getSacredText(url):
    page = urllib.request.urlopen(url).read().decode('utf8', 'ignore')
    soup = BeautifulSoup(page,"lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return text#.encode('ascii', errors='replace')#.replace("?"," ")


text = getSacredText(PageURL)


def summarize(text, n):
    sents = sent_tokenize(text)
    
    assert n <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))
    
    word_sent=[word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)
    
    
    ranking = DefaultDict(int)
    
    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
             
        
    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]

#print(summarize(text,3))
