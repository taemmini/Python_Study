txtfile = open('C:/Users/samsu/Desktop/HarryPotter.txt','rt',encoding='UTF8')
text = txtfile.read()
txtfile.close()

import string
punc = list(string.punctuation)

import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

splits1 = text.split("\n")

while '/ ' in splits1: 
    splits1.remove('/ ')

while '' in splits1:
    splits1.remove('')

page = [sents for sents in splits1 if sents.endswith("J.K. Rowling ")] 
splits2 = [sent for sent in splits1 if sent not in page]
            
temp = ''
sent_combined = []
check = 0
for element in splits2:
    if element == 'Mr.':
        check += 1
    elif element == 'Mrs.':
        check += 1
    else:
        temp += element
if temp.strip():
    sent_combined.append(temp)

sent_combined = "".join(sent_combined)
tokens = sent_combined.split(' ')

word1 = []
for word in tokens:
    word1 += word.split('-')
    
word2 = []
for word in tokens:
    word2 += word.split('.')
    
print(word2)