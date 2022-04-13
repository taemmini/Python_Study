while True:
    selection = input("""
구구단 출력기
----------------------------------------------------------------------
    1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
----------------------------------------------------------------------
메뉴를 선택하세요 > 
""")
    if selection == '1':
        num1 = input("몇단을 외워볼까요? ")
        if num1 == 'q':
            print('이용해주셔서 감사합니다.')
            break
        elif (int(num1) > 0) and (int(num1) < 10):
            num1 = int(num1)
            print(f'--------{num1}단------------')
            for n in range(1, 10):
                print(f'{num1} * {n} = {num1*n}')
            else:
                print('--------------------------')
                print('이용해주셔서 감사합니다.')
            break
        else:
            print("잘못 입력하셨습니다.")
    elif selection == '2':
        num1 = input("몇단까지 외워볼까요? ")
        if num1 == 'q':
            print('이용해주셔서 감사합니다.')
            break
        elif (int(num1) > 0) and (int(num1) < 10):
            num1 = int(num1)
            for n in range(1, num1+1):
                print(f'-----------{n}단------------')
                for x in range(1,10):
                    print(f'{n} * {x} = {n*x}')
            else:
                print('--------------------------')
                print('이용해주셔서 감사합니다.')
            break
        else:
            print("잘못 입력하셨습니다.")
    elif selection == '3':
        while True:
            num1 = input("몇단부터 외워볼까요? ")
            num2 = input("몇단까지 외워볼까요? ")
            if (num1 == 'q') or (num2 == 'q'):
                print('이용해주셔서 감사합니다.')
                break
            elif (int(num1) > int(num2)) or (int(num1) <= 0) or (int(num1) >= 10) or (int(num2) <= 0) or (int(num2) >= 10):
                print("잘못 입력하셨습니다.")
            else:
                num1 = int(num1)
                num2 = int(num2)
                while num1 <= num2:
                    for n in range(num1, num2+1):
                        print(f'------------{n}단-----------')
                        for x in range(1,10):
                            print(f'{n} * {x} = {n*x}')
                    else:
                        break
                print('--------------------------')
                print('이용해주셔서 감사합니다.')
                break
        break
    elif selection == 'q':
        print('이용해주셔서 감사합니다.')
        break
    else:
        print("선택지를 잘못 입력하셨습니다.")