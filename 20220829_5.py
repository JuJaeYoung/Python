#1 n명에 대해 3개의 점수를 입력받아서 과목별 총점 / 과목별 평균 / 개개인 총점 / 개개인 평균 표 만들기 (리스트로?)

a = []  # 학생들
b = []  # 국어점수
c = []  # 수학점수
d = []  # 영어점수
count = 0

while True:
    n = int(input('학생 번호:'))            # 학생 번호 입력
    if n == 0:
        print('-끝-')
        break
    
    kor = int(input('국어 점수:'))         # 국어 점수 입력
    mat = int(input('수학 점수:'))          # 수학 점수 입력
    eng = int(input('영어 점수:'))          # 영어 점수 입력
    
    x = [kor,mat,eng]
    a.append(x)
    b.append(kor)
    c.append(mat)
    d.append(eng)
    count += 1

    for i in range(count):
        print(i+1,'번 학생의 총점:',)
        print(i+1,'번 학생의 평균:',)
        
        
    
    
