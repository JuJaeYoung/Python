import random as rd
import string as st

f = open('result.csv', 'w')
f.write(f'이름,국어,영어,수학,컴퓨터')
f.write('\n')

for _ in range(50) :                # 50명 입력
    nam = ""
    for _ in range(3) :             # 3글자 이름 생성
        string = st.ascii_uppercase
        nam += rd.choice(string)
    kor = rd.randrange(0,101)       # 국어
    eng = rd.randrange(0,101)       # 영어
    mat = rd.randrange(0,101)       # 수학
    com = rd.randrange(0,101)       # 컴퓨터
    f.write(f'{nam},{kor},{eng},{mat},{com}\n')

f.close()
