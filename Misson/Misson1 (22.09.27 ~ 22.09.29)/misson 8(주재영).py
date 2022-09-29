#from operator import itemgetter

f = open('result.csv', 'r')
f1 = open('rank_result.csv', 'w')
lt = []
tt = []
result = []

for x in f :
    lt.append(x.strip().split(','))                 # '\n' 제거, ',' 구분 후 리스트로 반환


for line in lt :                                    # 석차 값 입력 x
    if '이름' in line :
        continue
    
    tot = sum(map(int,line[1:5]))
    avg = int(tot / 3)
    
    line.append(tot)
    line.append(avg)
    

for i in range(1,len(lt)) :                         # 합계를 기준으로 순위 정하자 = lt[i][5]
    tt.append(lt[i][5])
tt.sort(reverse = True)                             # 역순 정렬된 tt
                                       

for i in range(1,len(lt)) :
    rnk = tt.index(lt[i][5]) + 1                    # 인덱스 + 1 => 순위
    lt[i].append(rnk)


result = sorted(lt[1:], key = lambda x : x[7])     # 합계를 기준으로 정렬

f1.write(f'이름,국어,영어,수학,컴퓨터,합계,평균,순위')
f1.write('\n')
for l in result :
    f1.write(f'{l[0]},{l[1]},{l[2]},{l[3]},{l[4]},{l[5]},{l[6]},{l[7]}')
    f1.write('\n')

f.close()
f1.close()
