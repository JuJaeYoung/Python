day_works = int(input('하루 몇 시간 일하나요?: '))
days = int(input('주 몇 일 일하나요?: '))
pay = int(input('시급이 얼마인가요?: '))

if day_works * days >= 15:
    print(' ')
    print('기본급여:', day_works * days * pay)
    print('주휴수당:', day_works * pay)
    print('총 급여:', day_works * days * pay + day_works * pay)
else:
    print(' ')
    print('총 급여:', day_works * days * pay)
