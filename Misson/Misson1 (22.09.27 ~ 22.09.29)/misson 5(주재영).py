s = input()             # 입력 문자
x = ord(s)              # 숫자로 변환

for i in range(x,96,-1) :
    lt = []                 # 입력 문자보다 순위가 낮은 알파벳 반환 리스트
    for j in range(97,i+1) :
        lt.append(chr(j))
        
    print("".join(lt))
