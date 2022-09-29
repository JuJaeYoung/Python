f_name = input()                    # 파일명
f_word = input()                    # 단어
new_word = input()                  # 새로운 단어

d_name = f_name.split('.')[0]       # 문서이름
a = ['파일이름', '문서이름', '찾을단어', '출현횟수', '단어변화','변화횟수']


#1 한 줄씩 반환
f = open(f_name, 'r')

y = []
for k in f :
    if '\n' in k :
        y.append(k[:len(k)-1])
    else :
        y.append(k[:len(k)])
f.close()

#2 단어 개수 세기
f = open(f_name, 'r')
data = f.read()
word = data.split()                 # 단어 분리 후 리스트 반환

cnt = 0
for j in word:
    if f_word in j :
        cnt += 1                    # 단어 개수
f.close()


#3 다른 단어로 변환 후 새로운 파일 출력
f = open(f_name, 'r')
f1 = open(d_name+'_new.txt', 'w')

data = f.read()
word = data.split(f_word)

result = new_word.join(word)
f1.write(result)

f.close()
f1.close()


#4 새로운 파일 반환
f = open(d_name+'_new.txt', 'r')

z = []
for k in f :
    if '\n' in k :
        z.append(k[:len(k)-1])
    else :
        z.append(k[:len(k)])
f.close()


#5 출력
print('┌──────────────────────────┐')
print(f" {'%8s'%a[0]}   │   {f_name} ")
print('├──────────────────────────┤')
print(f" {'%8s'%a[1]}   │   {d_name} ")
print('├──────────────────────────┤')
print(f" {'%8s'%a[2]}   │   {f_word}")
print('├──────────────────────────┤')
print(f" {'%8s'%a[3]}   │   {cnt}")
print('├──────────────────────────┤')
for i in y :
    print(f"     {i}")
print('└──────────────────────────┘')
print('\n')

print('┌──────────────────────────┐')
print(f" {'%8s'%a[0]}   │   {d_name}_new.txt ")
print('├──────────────────────────┤')
print(f" {'%8s'%a[1]}   │   {d_name}_new ")
print('├──────────────────────────┤')
print(f" {'%8s'%a[4]}   │   {f_word} --> {new_word}")
print('├──────────────────────────┤')
print(f" {'%8s'%a[5]}   │   {cnt}")
print('├──────────────────────────┤')
for i in z :
    print(f"     {i}")
print('└──────────────────────────┘')
