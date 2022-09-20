#1 n명에 대해 3개의 점수를 입력받아서 과목별 총점 / 과목별 평균 / 개개인 총점 / 개개인 평균 표 만들기 (리스트로?)

kor_list = []  # 국어점수
mat_list = []  # 수학점수
eng_list = []  # 영어점수
sum_list = []  # 학생별 점수합

count = 0
sum_kor = 0     # 국어과목 점수합
sum_mat = 0     # 수학과목 점수합
sum_eng = 0     # 영어과목 점수합

while True:
    n = int(input('학생 번호:'))            # 학생 번호 입력
    if n == 0:
        print('\n')                         # 개행
        break
    
    kor = int(input('국어 점수:'))          # 국어 점수 입력
    mat = int(input('수학 점수:'))          # 수학 점수 입력
    eng = int(input('영어 점수:'))          # 영어 점수 입력
    
    sum_list.append(kor + mat + eng) 

    kor_list.append(kor)                    # 국어 점수 리스트
    mat_list.append(mat)                    # 수학 점수 리스트
    eng_list.append(eng)                    # 영어 점수 리스트
    count += 1                              # 과목별 평균 만들기 위한 개수

    print('\n')                             # 개행

for i in range(count):
    sum_kor += kor_list[i]                  # 국어점수 누적..
    sum_mat += mat_list[i]                  # 수학점수 누적..
    sum_eng += eng_list[i]                  # 영어점수 누적..

print(' 학생  |   국어     수학     영어   |  총점     평균')
print('------------------------------------------------------')

for j in range(count):
    print(' ',j+1,'   |   ',kor_list[j],'     ',mat_list[j],'     ',eng_list[j],'   | ',round(sum_list[j],1),'    ',round(sum_list[j]/3,1))

print('------------------------------------------------------')
print(' 총점  |  ',round(sum_kor,1),'    ',round(sum_mat,1),'    ',round(sum_eng,1),'   | ',round(sum_kor+sum_mat+sum_eng,1),'      - ')
print(' 평균  | ',round(sum_kor/count,1),'   ',round(sum_mat/count,1),'   ',round(sum_eng/count,1),'   |   -      ',round((sum_kor+sum_mat+sum_eng)/(count*3),1))
