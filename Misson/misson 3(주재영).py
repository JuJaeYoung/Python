# 팰린드롬 문자열
s = input()
cnt = []                                    # 팰린드롬 수치 리스트


for i in range(len(s)-1) :
    t = []                                  # 서로 같은 문자 인덱스 리스트
    ss = s[i+1:]                            # 위치 찾기
    a = ss.find(s[i]) + 1 + i
    if ss.find(s[i]) != -1 :
        t.append(a)

        while 1 :
            ss = s[a+1:]
            if ss.find(s[a]) == -1 :
                break
            a = ss.find(s[a]) + a + 1
            if a >= len(s) :
                break
            else :
                t.append(a)                 # 여기까지
    if t == [] :
        break
    else :                                  
        for j in t :                        # 팰린드롬 수치 구하는 과정
            l = s[i:j+1]
            l_1 = "".join(l)
            l_2 = "".join(reversed(l))
            if l_1 == l_2 :
                cnt.append(len(l_1))
    
print(max(cnt))

