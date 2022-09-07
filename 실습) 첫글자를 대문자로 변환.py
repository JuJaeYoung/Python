# 새로운 문자를 입력받아 첫글자는 무조건 대문자 나머지는 소문자로 출력!

def clear(x):
    ab = []
    words = x.lower().split()

    for word in words:
        a = word[0].upper()
        b = word[1:]
        ab.append(a + b)
        
    return ab


read = input('변환 할 문자를 입력해주세요.:')
a = clear(read)
print(*a)


# 강사님 풀이

def func(s):
    str = s.split()                     # 입력받은 문자열 구분짓기
    ret = ''                            # 문자열 미리 만들기
    for s1 in str:
        ss1 = s1.lower()                # 소문자로 변환
        ss2 = ss1[0].upper() + ss1[1:]  # 첫글자 대문자, 나머지 소문자 만들기
        ret = ret + ' ' + ss2           # 나온 결과값 받아적기(반복문 돌면서 누적해서 쌓임
    return ret


x = input('영어 문장을 입력하세요 : ')
y = func(x)
print(x)
print(y)
