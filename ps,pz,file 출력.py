# 예시와 같은 문자열에서 '/'로 구분된 각각의 옵션을 표시하고,
# 특히 PZ 옵션의 값을 x,y,w,h로 구분하여 표기하세요.
# 옵션의 순서는 변경 가능합니다.
# 최종 출력물은 다음과 같이 표기해 주세요.
# PS = 121
# PZ.x = 2 ... PZ.h = 100
# FILE = C:\Users\user13\Documents\Study\test.py

# 1
str = '/PS:121 /PZ:2,3,100,100 /FILE=test.py'

def spl( s ) :
    x = s.split()                           # 공백으로 분리
    
    for i in range(len(x)) :
        if "PS" in x[i]:                    # PS 값
            ps = x[i][4:]

        elif "PZ" in x[i]:                  # PZ 값
            pz_x = x[i][4]
            pz_y = x[i][6]
            pz_w = x[i][8:11]
            pz_h = x[i][12:15]
            
        elif "FILE" in x[i]:                # FILE 값
            file = x[i][6:]
            

    return ps, pz_x, pz_y, pz_w, pz_h, file

ps, pz_x, pz_y, pz_w, pz_h, file = spl(str)

print(f'PS = {ps}\nPZ.x = {pz_x}, PZ.y = {pz_y}, PZ.w = {pz_w}, PZ.h = {pz_h}\nFILE = {file}')


# 2
str1 = '/FILE=test.py /PZ:2,3,100,100 /PS:121'

def split( s ) :                # 공백으로 분리 함수
    x = s.split('/')

    return x

def ps( a ) :                   # ps 함수

    return a[3:]
    
def pz( b ) :                   # pz 함수

    return b[3], b[5], b[7:10], b[11:14]

def file( c ) :                 # file 함수

    return c[5:]

for x in split(str1) :          # 분리된 문자열에서 ps, pz, file 구분
    if "PS" in x :
        ps_ = x.strip()
        
    elif "PZ" in x :
        pz_ = x.strip()
        
    elif "FILE" in x :
        file_ = x.strip()
        

ps = ps(ps_)
pz_x, pz_y, pz_w, pz_h = pz(pz_)
file = file(file_)

print(f'PS = {ps}\nPZ.x = {pz_x}, PZ.y = {pz_y}, PZ.w = {pz_w}, PZ.h = {pz_h}\nFILE = {file}')


# 3
str1 = '/FILE=test.py /PZ:2,3,100,100 /PS:121'

def split( s ) :                # '/' 으로 분리 함수
    x = s.split('/')

    return x

def ps( a ) :                   # ps 함수
    x = a.split(':')
    
    return x[1]
    
def pz( b ) :                   # pz 함수
    x = b.split(':')
    y = x[1].split(',')
    
    return y

def file( c ) :                 # file 함수
    x = c.split('=')
    
    return x[1]

for x in split(str1) :          # 분리된 문자열에서 ps, pz, file 구분
    if "PS" in x :
        ps_ = x.strip()
        
    elif "PZ" in x :
        pz_ = x.strip()
        
    elif "FILE" in x :
        file_ = x.strip()
        

ps = ps(ps_)
pz_x, pz_y, pz_w, pz_h = pz(pz_)
file = file(file_)

print(f'PS = {ps}\nPZ.x = {pz_x}, PZ.y = {pz_y}, PZ.w = {pz_w}, PZ.h = {pz_h}\nFILE = {file}')



# 강사님 풀이 1
str0 = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"
str1 = "/PZ:2,3,100,100 /PS:121 /FILE=test.py"
str2 = "/PZ:2,3,100,100 /FILE=test.py /PS:121"

def get_PS(s) :                 # /PS 옵션을 인수로 받아서 옵션의 값을 리턴
    x = s.split(":")            # s = /PS:121
    return x[1]

def get_PZ(s) :                 # /PZ 옵션을 인수로 받아서 옵션의 값을 x,y,w,h 리스트로 리턴 
    x = s.split(":")            # s = /PZ:2,3,100,100
    y = x[1].split(",")         # y = ['2', '3', '100', '100']
    return y

def get_FILE(s) :               # /FILE 옵션을 인수로 받아서 옵션의 값을 리턴
    x = s.split("=")            # s = /FILE=test.py
    return x[1]

def Main() :                    # 옵션 해석 프로그램 메인 루틴
    s = str0.split('/')
    for s1 in s :
        if s1[0:2] == "PS" :
            a = get_PS(s1)
            print(f"PS = {a}")
        elif s1[0:2] == "PZ" :
            a = get_PZ(s1)
            print(f"PZ.x = {a[0]}\nPZ.y = {a[1]}\nPZ.w = {a[2]}\nPZ.h = {a[3]}")
        elif s1[0:4] == "FILE" :
            a = get_FILE(s1)
            print(f"FILE = {a}")

Main()


# 강사님 풀이 2
str0 = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"
str1 = "/PZ:2,3,100,100 /PS:121 /FILE=test.py"
str2 = "/PZ:2,3,100,100 /FILE=test.py /PS:121"

def getOptionValue(s,d) :       # /_xxx_(d)_vvv_ 옵션을 인수로 받아서 옵션의 값(val) 리턴
        x = s.split(d)          # s : PS, FILE 옵션 , d : 구분자
        return x[1]
    
def get_PZ(s) :                 # /PZ 옵션을 인수로 받아서 옵션의 값을 x,y,w,h 리스트로 리턴 
    x = s.split(":")            # s = /PZ:2,3,100,100
    y = x[1].split(",")         # y = ['2', '3', '100', '100']

def Main() :                    # 옵션 해석 프로그램 메인 루틴
    s = str0.split('/')
    for s1 in s :
        if s1[0:2] == "PS" :
            b = getOptionValue(s1,":")
            print(f"PS = {b}")
        elif s1[0:2] == "PZ" :
            a = get_PZ(s1)
            print(f"PZ.x = {a[0]}\nPZ.y = {a[1]}\nPZ.w = {a[2]}\nPZ.h = {a[3]}")
        elif s1[0:4] == "FILE" :
            b = getOptionValue(s1, "=")
            print(f"FILE = {b}")

Main()
