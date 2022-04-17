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
    import string
    punc = list(string.punctuation)
    punc.remove('-') #하이픈에 따른 분류를 위해
    punc.append('\n')
    punc.append('')

    end_letter = ['. ','? ','! ','.”','?”','!”', "'", '"']

    for i in end_letter: #개행
        text = text.replace(i, 'ENDL')
    for i in punc: #문장부호
        text = text.replace(i, '')
    
    sentence_tokens = [sentences for sentences in text.split('ENDL') if sentences]
    return sentence_tokens

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

# 3.3.3
def text_normalize(word_tokens):
    """_summary_
        불필요 토큰 제거 (어포스트로피 제거)
        word_tokens: 토큰화된 단어 입력
        corpus: 정제된 코퍼스 출력
    """
    import nltk
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    pro_tokens = [[word.split("'") for word in sentence] for sentence in word_tokens]
    pro_tokens = sum(pro_tokens, [])
    go_words = [[word for word in sentences if word.lower() not in stop_words] for sentences in pro_tokens] 

    # uncasing
    corpus =  [word for sentence in go_words for word in sentence if word]
    return corpus