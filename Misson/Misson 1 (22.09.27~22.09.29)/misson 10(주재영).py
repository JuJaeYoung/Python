def factorial(a) :
    result = 1
    for i in range(a,0,-1) :
        result *= i
    return result

def multiple(a,b) :
    x1 = a*(b-b//10*10)
    x2 = a*(b//10-b//100*10)
    x3 = a*(b//100)
    x4 = a*b
    return x1,x2,x3,x4

def permutation(n,k) :
    result = 1
    for i in range(n,n-k,-1) :
        result *= i
    return result

while 1 :                           # 0이면 끝내기
    x = input('선택 --> ')           # 몇 번 프로그램?

    if x == '1' :                     # 선택 = 1 이라면 => 팩토리얼
        print(' < Factorial > ')
        a = int(input('숫자를 입력해 주세요 : '))
        f = factorial(a)
        print(f'{a}! = {f} 입니다.\n')

    elif x == '2' :                   # 선택 = 2 이라면 => 곱셈
        print(' < 3자리 X 3자리 > ')
        a, b = map(int,input('3자리 숫자 2개를 입력해 주세요 : ').split())
        x1, x2, x3, x4 = multiple(a,b)
        print(f'     {a}')
        print(f' X   {b}')
        print('---------')
        print(f"{'%8d'%x1}")
        print(f"{'%7d'%x2} ")
        print(f"{'%6d'%x3}  ")
        print('---------')
        print(f"{'%8d'%x4}\n")

    elif x == '3' :                   # 순열, 조합
        print(' < 순열, 조합 > ')
        a, b = map(int,input('숫자 2개를 입력해주세요 : ').split())
   
        if a >= b :
            N = a
            K = b
        elif a < b :
            N = b
            K = a
            
        per = permutation(N,K)
        bin = int(factorial(N) / (factorial(K) * factorial(N-K)))
        print(f'>순열 : {N} Permutation {K} = {per} 입니다.')
        print(f'>조합 : {N} Combination {K} = {bin} 입니다.\n')

    elif x == 'Q' :
        break

    
