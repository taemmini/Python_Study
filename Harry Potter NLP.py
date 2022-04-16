# 3.
txtfile = open('C:/Users/samsu/Desktop/HPBook1.txt','rt',encoding='UTF8')
text = txtfile.read()[7:]
text = '\n'.join([sent for sent in text.split('\n') if not sent.startswith('Page |')])

# 문장부호 추출
import string
punc = list(string.punctuation)
punc.remove('-') #하이픈에 따른 분류를 위해\

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

# word tokenizer
word_tokens = [[word for word in sentence.split() if word] for sentence in sentence_tokens]

# 불필요 토큰 제거
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
go_words = [[word for word in sentences.split() if word.lower() not in stop_words] for sentences in sentence_tokens]

HYPHEN, APOSTROPHE = '-', '’'

output = []
for sentence in go_words:
    temp = []
    for word in sentence:
        # 문장부호 아닌지 다시 확인
        if word not in punc and word: # not empty
            if APOSTROPHE in word:
                # She's -> [She, 's] 
                # fur-pieces's -> [fur-pieces, 's]
                index = word.find(APOSTROPHE)
                words = word[:index], word[index:]
                print('[Case 1: {}] {}'.format(APOSTROPHE, words))
            else: 
                words = [word]
            # Change hypens
            for word in words:
                if HYPHEN in word:
                    index = word.find(HYPHEN)
                    words = word[:index], word[index+1:]
                    print('[Case 2: {}] {}'.format(HYPHEN, words))
                else:
                    words = [word]     
            temp.extend(words)       
    output.append(temp)
