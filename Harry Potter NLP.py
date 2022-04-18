# 2. 해리포터 정제

# 파일 불러오기
txtfile = open('C:/Users/samsu/Desktop/HPBook1.txt',encoding='UTF8')
text = txtfile.read()
text = '\n'.join([sent for sent in text.split('\n') if not sent.startswith('Page |')])

# 문장부호 추출
import string
punc = list(string.punctuation)
extra = ['/', '\n', '— ','•','■']
punc.extend(list(extra))
punc.remove('-')

# 문장 부호 전처리
end_letter = ['. ','? ','! ', "'", '"']
abbreviations = ['Mr.','MR.','Mrs.','H.','J.K.','G.','M.']
text = text.replace('LIVED', 'LIVEDENDM').replace('...','').replace('. . . ', '').replace('“','"').replace('”','"').replace('‘',"'")  # ENDM의 경우엔 첫문장용

for i in abbreviations: # 단축어제거
    text = text.replace(i, i[:-1])
for i in end_letter: #개행 처리를 위한 문장 종결 부호 제거
    text = text.replace(i, 'ENDM')
for i in punc: #문장부호 제거
    text = text.replace(i, '')
text = text.replace('’',"'") # 어퍼스트로피 정제

# 문장 분절
sentence_tokens = [sentences for sentences in text.split('ENDM') if sentences]

# word tokenizer
word_tokens = [[word for word in sentence.split() if word] for sentence in sentence_tokens]

# 단어 정제
    # 'd는 불용어일 가능성이 크므로 삭제.
    # would는 원형과 부정형이 불용어이므로 삭제.
    # 's는 예상 가능한 단어가 불용어이기에 원형 또한 불용어에 가깝다 판단하여 삭제.
    # 그 외 줄임말과 구어체는 원래의 형태로 바꿔서 FreqDist 표시시 포함.

delete_abbr_1 = ["'m", "'re", "'s", "'d", "'em", "'ll", "'ve", "'atta", "'cause", "'snot"] # 어포스트로피가 앞에 있는 삭제 문자열
delete_abbr_2 = ["d'","o'", "abou'", "an'", "doin'", "jus'", "what'"] # 어포스트로피가 뒤에 있는 삭제 문자열
delete_abbr_3 = ["more'n", "shouldn'ta", "can't've"] # 어포스트로피가 사이에 있는 삭제 문자열
before_abbr = ["'til", "c'mon", "c'mere", "'night", "closer'n", "diff'rent", "myst'ry", "s'pose", "s'ppose", "s'pposed", \
                 "'course", "'smatter","'scuse", "'cept", "'undred", "firs'", "las'","flamel'v'","good'un"] # 수정 전 문자열
after_abbr = [["until"],["come"],["come"],["night"],["closer"],["different"],["mystery"],\
              ["suppose"],["suppose"],["supposed"],["course"],["matter"],["excuse"],["except"],\
              ["hundred"],["first"],["last"],["flamel"],["good","one"]] # 수정 후 문자열

output = []
for sentences in word_tokens:
    temp = []
    for w in sentences:
        if "'" in w:
            word = w.lower()
            idx = word.find("'")
            if word[idx:] in delete_abbr_1:
                words = [word[:idx]]
            elif word[:idx + 1] in delete_abbr_2:
                words = [word[idx + 1:]]
            elif word in delete_abbr_3:
                continue
            elif word in before_abbr:
                index = before_abbr.index(word)
                words = after_abbr[index]
            elif "n't" in word:
                words = [word[:idx - 1]]
            elif "in'" in word:
                words = [word[:idx] + 'g']
            else:
                words = [word[:-1]]
        else: 
            words = [w]
# 하이픈 분리
        for w in words:
            if '-' in w:
                words = w.split('-')
            else:
                words = [w]
        temp.extend(words)  
    output.append(temp)
    
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
results = [[word for word in sentences if word.lower() not in stopwords] for sentences in output] # 불용어 제거

# uncasing
corpus = [word.lower() for sentence in results for word in sentence if word] #혹시 모르는 빈 리스트 필터링

# 총 토큰 수
print(f'총 토큰 수: {len(corpus)}')

# Frequiency Distribution 상위 50개
from nltk import FreqDist
fdist = FreqDist(corpus)
fdist.plot(50)