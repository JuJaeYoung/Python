def rp(x, op) :                         # 기호 입력받아서 제거하는 함수
    result = x.replace(op,'')
    return result

x = {}
y = 'Writing programs (or programming) is a very creative and rewarding activity. You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem. This book assumes that everyone needs to know how to program and that once you know how to program, you will figure  out what you want to do with your newfound skills. We are surrounded in our daily lives with computers ranging from laptops to cell phones. We can think of these computers as our “personal assistants” who can take care of many things on our  behalf. The hardware in our current-day computers is essentially built to continuously ask us the question, “What would you like me to do next?” Our computers are fast and have vast amounts of memory and could be very helpful to us if we only knew the language to speak to explain to the computer what we would like it to do next. If we knew this language we could tell the computer to do tasks on our behalf that were repetitive. Interestingly, the kinds of things computers can do best are often the kinds of things that we humans find boring and mind-numbing.'
z = ['.',',','?','“','”','(',')']       # 제거 할 기호

for i in z:                             # 기호 제거 중..
    y = rp(y,i)
    
y = y.replace('-',' ')                  # 기호 제거 중..
y = y.lower()                           # 소문자로 변경 중..

lst = y.split()                         # 공백단위 분리 후 리스트로 !

for j in lst:
    x[j] = x.get(j,0) + 1               # 갯수 세는 중..

#for k in x:                             # 출력 1..
#    val = x.get(k)
#    print(f'{k} : {val}')

for k in sorted(x.keys()):
    print(k, x[k])





