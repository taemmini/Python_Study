#Week 3 Quiz's
#Quiz 1
from nltk import book
Thursday = book.text9
Monty = book.text6

diversity_txt9 = round(len(set(hursday.tokens)) / len(Thursday.tokens) * 100)
print(f'Text 9\'s text diversity is approximately {diversity_txt9}%.')

text6_tokens = sorted((set(Monty.tokens)), reverse = True) [:10]
print(text6_tokens) #첫번째 조건 추출

for text6_alligned in range(10):
    if 'z' in text6_tokens[text6_alligned]: #z가 있을 때
        print(text6_tokens[text6_alligned].capitalize())
    elif len(text6_tokens) >= 4: #z가 없을 때 4글자 이상일 때
        temporary = (text6_tokens[text6_alligned]) [::-1]
        temporary = temporary.capitalize()
        temporary = temporary[::-1]
        print(temporary)
    else: #z도 없고 4자 이상도 아닐 때 출력
        print(text6_tokens[text6_alligned])
          
# Quiz2
Id_number = input("주민번호를 입력하세요: ")
Cell_number = input("휴대폰번호를 입력하세요: ")
Email = input("이메일 아이디를 입력하세요: ")

if Id_number[0] == '0' or Id_number[0] == '1' or Id_number[0] == '2': #19xx년과 20xx년 구분용
    Birthyear = '20' + Id_number[0:2]
else:
    Birthyear = '19' + Id_number[0:2]

if Id_number[6] == '1' or Id_number[6] == '3' or Id_number[6] == '5': #남성은 홀수, 여성은 짝수, 정부 규정상 6까지 있음.
    gender = '남성' 
else:
    gender = '여성'

print(f'당신은 {Birthyear}년 {Id_number [2:4]}월 {Id_number [4:6]}일 출생의 {gender}입니다.')
print(f'당신의 휴대전화 번호는 {Cell_number[:3]}-{Cell_number[3:7]}-{Cell_number[7:11]}입니다.')
print(f'당신의 이메일 주소는 {Email}@hufs.ac.kr 입니다.')