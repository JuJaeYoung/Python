x = 1
n = 1
while True:
    print('#{}'.format(n))
    day_works = int(input('하루 몇 시간 일하나요?: '))
    days = int(input('주 몇 일 일하나요?: '))
    pay = int(input('시급이 얼마인가요?: '))

    if day_works * days >= 15:
        print(' ')
        print('기본급여:', day_works * days * pay)
        print('주휴수당:', day_works * pay)
        print('총 급여:', day_works * days * pay + day_works * pay)
        print(' ')
        x = int(input('끝내려면 0을 입력하세요. 그렇지 않으면 임의의 값을 입력하세요.')) # 끝내고 싶을 때 0 입력
        print(' ')
        if x == 0:
            break
        else:
            n += 1
    else:
        print(' ')
        print('총 급여:', day_works * days * pay)
        print(' ')
        x = int(input('끝내려면 0을 입력하세요. 그렇지 않으면 임의의 값을 입력하세요.'))   # 끝내고 싶을 때 0 입력
        print(' ')
        if x == 0:
            break
        else:
            n += 1
        
