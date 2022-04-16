txtfile = open("C:/Users/samsu/Desktop/carroll-alice.txt",encoding='UTF8')
text = txtfile.read()






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
    return print(sentence_tokens)






def word_tokenize(sentence_tokens):
    """
    sentence_tokens: 토큰화된 문장 입력
    Returns: 토큰화된 단어 전달
    """
    word_tokens = [[word for word in sentence.split()] for sentence in sentence_tokens if sentence]
    return print(word_tokens)






def text_normalize(word_tokens):
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
    return output