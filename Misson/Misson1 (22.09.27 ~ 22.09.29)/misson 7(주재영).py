s = input('문자를 입력하시오  ').upper()       # 대문자 : 65 ~ 90
n = ord(s)                                  # e : 69

for i in range(65,n+1) :
    print(' ' * (ord(s) - n) + chr(i) * (n-64))
    n -= 1
    
