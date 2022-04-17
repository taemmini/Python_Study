# 1. 구구단
while True:
    selection = input("""
구구단 출력기
----------------------------------------------------------------------
    1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
----------------------------------------------------------------------
메뉴를 선택하세요 >""") # 1.1. 메뉴 제시
    if selection.isalpha():
        while selection == 'q': # 1.4. 2 - 조건3, 
            print('이용해주셔서 감사합니다.')
            break
        else:
            print("선택지 오류") #1.5 재확인
            continue
        break
    elif selection.isalnum():
        selection = int(selection)
        while  selection == 1:
            num1 = input("구구단 외우기:")
            if num1.isalpha():
                while num1 == 'q': # 1.4. 조건3
                    print('이용해주셔서 감사합니다.')
                    break
                else:
                    print("입력 오류") #1.5 재확인
                    continue
            elif num1.isalnum():
                num1 = int(num1)
                while (0 < num1 < 10): # 1.2. 조건1
                    print(f'--------{num1}단------------')
                    for n in range(1, 10):
                        print(f'{num1} * {n} = {num1*n}')
                    else:
                        print('--------------------------')
                        print('이용해주셔서 감사합니다.')
                    break
                else:
                    print("입력 오류") #1.5 재확인
                    continue
            break
        while  selection == 2:
            num1 = input("끝낼 단:")
            if num1.isalpha():
                while num1 == 'q': # 1.4. 조건3
                    print('이용해주셔서 감사합니다.')
                    break
                else:
                    print("입력 오류") #1.5 재확인
                    continue
            else:
                num1 = int(num1)
                while (0 < num1 < 10): # 1.2. 조건1
                    for n in range(1, num1+1):
                        print(f'-----------{n}단------------')
                        for x in range(1,10):
                            print(f'{n} * {x} = {n*x}')
                    else:
                        print('--------------------------')
                        print('이용해주셔서 감사합니다.')
                    break
                else:
                    print("입력 오류") #1.5 재확인
                    continue
            break
        while selection == 3:
            num1 = input("시작 단:")
            num2 = input("끝낼 단:")
            if (num1.isalpha()) or (num2.isalpha()):
                while (num1 == 'q') or (num2 == 'q'): # 1.4. 조건3
                    print('이용해주셔서 감사합니다.')
                    break
                else:
                    print("입력 오류") #1.5 재확인
                continue
            elif (num1.isalnum()) and (num2.isalnum()):
                num1 = int(num1)
                num2 = int(num2)
                while (num1 <= num2) and (0 < num1 < 10) and (0 < num2 < 10): # 1.3. 조건1, 조건2 
                        for n in range(num1, num2+1):
                            print(f'------------{n}단-----------')
                            for x in range(1,10):
                                print(f'{n} * {x} = {n*x}')
                        else:
                            print('--------------------------')
                            print('이용해주셔서 감사합니다.')
                        break
                else:
                    print("입력 오류") #1.5 재확인
                    continue
            break
        break
    else:
        print("입력 오류") #1.5 재확인
        continue