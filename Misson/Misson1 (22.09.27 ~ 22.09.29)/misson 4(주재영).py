x, y = map(int,input().split())
x_l = []                        # x의 약수
y_l = []                        # y의 약수
lt = []                         # 공약수 리스트
def yak(n) :                
    lt = []
    for i in range(1,n+1) :     # 약수 구하는 함수
        if n % i == 0 :
            lt.append(i)
    return lt

x_l = yak(x)
y_l = yak(y)

for i in x_l :
    if i in y_l :
        lt.append(i)
        
print(max(lt))
    
