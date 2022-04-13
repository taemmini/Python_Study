# 2. 해리포터 정제하기

# 2.1. 해리포터 불러오기
txtfile = open('C:/Users/samsu/Desktop/HarryPotter.txt','rt',encoding='UTF8')
text = txtfile.read()
txtfile.close()

# 2.2. punctuation 가져오기
import string
punc = list(string.punctuation)

# 2.3. 불용어 가져오기
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

raw = text.split('. ')
splits1 = [text.split(' ') for text in raw]

splits2 = splits1[:-1].split()

# 2.2. Punctuation 삭제