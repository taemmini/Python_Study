# 3.1. 구구단을 def로 표현 시작범위, 끝범위를 정하면 각각 1, 2, 3번 선택지에 해당하는 부분을 한번에 표현할 수 있음
def gugudan( num1 = 'q', num2 = 'q'):
    """
        num1 (str, optional): 1, 3번 선택지의 첫번째 인수. q을 기본값으로 지정
        num2 (str, optional): 공통 선택지의 첫번째 인수. q를 기본값으로 지정
    """
    if (num1.isalpha()) or (num2.isalpha()):
        if (num1 == 'q') or (num2 == 'q'):
            print('이용해주셔서 감사합니다.')
        else:
            print("입력 오류")
    elif (num1 <= num2) and (num1.isalnum()) and (num2.isalnum()):
        num1 = int(num1)
        num2 = int(num2)
        if (0 < num1 < 10) and (0 < num2 < 10):
            for n in range(num1, num2+1):
                print(f'-----------{n}단------------')
                for x in range(1,10):
                    print(f'{n} * {x} = {n*x}')
            else:
                print('--------------------------')
                print('이용해주셔서 감사합니다.')
    else:
        print("입력 오류")

print("종료를 원하면 enter를 한 번 이상 눌러주세요.")              
num1 = input("처음 외울 단(1단부터 출력한다면 1을 입력합니다.):")
num2 = input("마지막으로 외울 단(하나의 단만 외울거라면 처음 외울 단과 같이 입력합니다.):")

gugudan(num1, num2)