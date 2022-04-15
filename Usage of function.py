# 3.1. 구구단을 def로 표현 시작범위, 끝범위를 정하면 각각 1, 2, 3번 선택지에 해당하는 부분을 한번에 표현할 수 있음
def multiplicaton_table (selection, num1 = 'q', num2 = 'q'): 
    """
        selection (_type_): 선택지 설정
        num1 (str, optional): 공통 선택지의 첫번째 인수. 탈출을 기본값으로 지정
        num2 (str, optional): 3번 선택지의 두번째 인수. 탈출을 기본값으로 지정
    """
    if selection.isalpha():
        if selection == 'q':
            print('이용해주셔서 감사합니다.')
        else:
            print("선택지 오류")
    elif selection.isalnum():
        selection = int(selection)
        if  selection == 1:
            if num1.isalpha():
                if num1 == 'q':
                    print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
            elif num1.isalnum():
                num1 = int(num1)
                if (0 < num1 < 10):
                    print(f'--------{num1}단------------')
                    for n in range(1, 10):
                        print(f'{num1} * {n} = {num1*n}')
                    else:
                        print('--------------------------')
                        print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
        elif  selection == 2:
            if num1.isalpha():
                if num1 == 'q':
                    print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
            else:
                num1 = int(num1)
                if (0 < num1 < 10):
                    for n in range(1, num1+1):
                        print(f'-----------{n}단------------')
                        for x in range(1,10):
                            print(f'{n} * {x} = {n*x}')
                    else:
                        print('--------------------------')
                        print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
        elif selection == 3:
            if (num1.isalpha()) or (num2.isalpha()):
                if (num1 == 'q') or (num2 == 'q'):
                    print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
            elif (num1.isalnum()) and (num2.isalnum()):
                num1 = int(num1)
                num2 = int(num2)
                if (num1 <= num2) and (0 < num1 < 10) and (0 < num2 < 10):
                        for n in range(num1, num2+1):
                            print(f'------------{n}단-----------')
                            for x in range(1,10):
                                print(f'{n} * {x} = {n*x}')
                        else:
                            print('--------------------------')
                            print('이용해주셔서 감사합니다.')
                else:
                    print("입력 오류")
    else:
        print("입력 오류")

selection = input("1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기")        
num1 = input("(까지, 부터) 외울 단:")
num2 = input("까지 외울 단(3번 미선택시 입력 필요 X):")

multiplicaton_table(selection, num1, num2)