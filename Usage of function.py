# 3.1. 구구단을 def로 표현 시작범위, 끝범위를 정하면 각각 1, 2, 3번 선택지에 해당하는 부분을 작성할 수 있음
def gugudan(num1, num2):
    while True:
        if (num1.isalpha()) or (num2.isalpha()):
            if (num1 == 'q') or (num2 == 'q'): # 1.4. 조건3
                print('이용해주셔서 감사합니다.')
                break
            else:
                print("입력 오류")
                break
        elif (num1.isalnum()) and (num2.isalnum()):
            num1 = int(num1)
            num2 = int(num2)
            if (num1 <= num2) and (0 < num1 < 10) and (0 < num2 < 10): # 1.3. 조건1, 조건2 
                for n in range(num1, num2+1):
                    print(f'------------{n}단-----------')
                    for x in range(1,10):
                        print(f'{n} * {x} = {n*x}')
                else:
                    print('--------------------------')
                    print('이용해주셔서 감사합니다.')
                    break
        else:
            print("입력 오류")
            break

print( """ 
1. 하나의 구구단을 알고자 한다면 같은 숫자를 입력한다.
2. 1단부터 알고자 하는 부분까지의 구구단을 알고자 한다면 1, (알고자 하는 구구단)을 입력한다.
3. 알고싶은 범위가 정해져 있다면 (시작 단), (끝 단)을 입력한다.
4. 나가고 싶다면 q를 한번 이상 입력한다. """)
num1 = input("첫번째 숫자:")
num2 = input("두번째 숫자:")
gugudan(num1, num2)