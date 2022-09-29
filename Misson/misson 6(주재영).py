n = int(input('숫자(홀수)를 입력하시오  '))
for i in range(1, n+1,2) :
    print(' ' * int((n - i) / 2) + '*' * i + ' ' * int((n - i) / 2))    
