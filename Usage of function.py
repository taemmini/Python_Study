#구구단을 def로 표현한 것. 결국 세번째
def gugudan(num1, num2):
    if (num1 > num2) or (num1 <= 0) or (num1 >= 10) or (num2 <= 0) or (num2 >= 10):
        print("잘못 입력하셨습니다.")
    else:
        while (num1 <= num2):
            for n in range(num1, num2+1):
                print(f'------------{n}단-----------')
                for x in range(1,10):
                    print(f'{n} * {x} = {n*x}')
            else:
                break
        print('--------------------------')
        print('이용해주셔서 감사합니다.')


gugudan(2, 2)
