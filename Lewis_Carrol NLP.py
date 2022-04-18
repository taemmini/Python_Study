from nltk.corpus import gutenberg   # Docs from project gutenberg.org
text = gutenberg.open('carroll-alice.txt').read()

#3.2.1
def sent_tokenize(text):
    """
    text: 문장 토큰화를 하려는 파일
    Returns: 문장 토큰화의 결과 
    """
    # 문장부호 추출
    import string
    punc = list(string.punctuation)
    extra = ['/', '\n', '— ','•','■', '⁕']
    punc.extend(list(extra))
    punc.remove('-')
    # 문장 분절 전처리
    end_letter = ['. ','? ','! ', "'", '"']
    text = text.replace('LIVED', 'LIVEDENDL') # 마침표 개행을 위한 준비
    # 문장/종결부호 제거
    for i in end_letter: #개행 처리를 위한 문장 종결 부호 제거
        text = text.replace(i, 'ENDL')
    for i in punc: #문장부호 제거
        text = text.replace(i, '')
    # 문장 분절
    sentence_tokens = [sentences for sentences in text.split('ENDL') if sentences]  
    return sentence_tokens
sent_token = sent_tokenize(text)

# 3.2.2
def word_tokenize(sentence_tokens):
    """
    sentence_tokens: 토큰화된 문장 입력
    Returns: 토큰화된 단어 전달
    """
    pre_words = [[word.split('-') for word in sentence.split() if word] for sentence in sentence_tokens]
    pre_tokens = [[word for word in sentence] for sentence in pre_words]
    word_tokens = sum(pre_tokens, [])
    return word_tokens
word_token = word_tokenize(sent_token)

# 3.3.3
def text_normalize(word_tokens):
    """_summary_
        불필요 토큰(stop words) 제거 (어포스트로피 제거)
        word_tokens: 토큰화된 단어 입력
        corpus: 정제된 코퍼스 출력
    """
    # 불필요 토큰 제거 (어포스트로피 제거)
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    pro_tokens = [[word.split("'") for word in sentence] for sentence in word_tokens]
    pro_tokens = sum(pro_tokens, [])
    go_words = [[word for word in sentences if word.lower() not in stop_words] for sentences in pro_tokens] 
    # uncasing
    corpus =  [word.lower() for sentence in go_words for word in sentence if word]
    return corpus

print(text_normalize(word_token))