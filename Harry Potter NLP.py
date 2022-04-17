# 2.
txtfile = open('C:/Users/samsu/Desktop/HPBook1.txt','rt',encoding='UTF8')
text = txtfile.read()[7:]
text = '\n'.join([sent for sent in text.split('\n') if not sent.startswith('Page |')])

# 문장부호 추출
import imp
import string
from turtle import goto
punc = list(string.punctuation)
punc.remove('-') #하이픈에 따른 분류를 위해

# sentence tokenizer
end_letter = ['. ','? ','! ','.”','?”','!”', "'", '"']
abbreviations = ['Mr.','MR.','Mrs.','H.','J.K.','G.','M. McGonagall']
extra = ['/', '\n', '','...','• k k k', '. . .', '— ','•','■']

text = text.replace('“','"').replace('”','"').replace('‘',"'").replace('LIVED', 'LIVEDENDL') # 문장부호 쓰임 통일 (D의 경우엔 첫분장용)

for i in abbreviations: # 단축어
    text = text.replace(i, i[:-1])
for i in extra: # 예외적으로 쓰인 부분
    text = text.replace(i, '')
for i in end_letter: #개행
    text = text.replace(i, 'ENDL')
for i in punc: #문장부호
    text = text.replace(i, '')

sentence_tokens = [sentences for sentences in text.split('ENDL') if sentences]

# word tokenizer (하이픈 분리, 어포스트로피 구분)
pre_words = [[word.replace('’', "'").split('-') for word in sentence.split() if word] for sentence in sentence_tokens]
pre_tokens = [[word for word in sentence] for sentence in pre_words]
word_tokens = sum(pre_tokens, [])

# 불필요 토큰 제거 (어포스트로피 제거)
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
pro_tokens = [[word.split("'") for word in sentence] for sentence in word_tokens]
pro_tokens = sum(pro_tokens, [])
go_words = [[word for word in sentences if word.lower() not in stop_words] for sentences in pro_tokens] 

# uncasing
corpus = [word.lower() for sentence in go_words for word in sentence if word]

# 총 토큰 수
print(f'총 토큰 수: {len(set(corpus))}')

# Frequiency Distribution
from nltk.probability import FreqDist 
fdist = FreqDist(corpus)
fdist.plot(50, cumulative=False)