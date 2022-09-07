def change(word) :
    for i in range(len(word)):
        a = word[i][0].upper()
        b = word[i][1:].lower()
        word[i] = a + b

    print("\n다음으로 변환 되었습니다.\n------------>>\t", " ".join(word))
        
while 1:
    word = []
    word = input("\n변환할 문자를 입력하세요\n------------>>\t ").split()
    
    change(word)               # 함수 실행

    ask = input("\n계속 하시겠습니까? ( YES / NO )\n------------>>\t ")
    
    if ask.upper() == "YES":   # 사용자가 또 다른 입력을 원할 경우 다시 시작
        continue
    else:
        print("\n\n프로그램을 종료합니다. \n\n감사합니다.")
        break






def change2(word) :

    for i in range(len(word)):
        a = word[i][0].upper()
        b = word[i][1:].lower()
        word[i] = a + b
        result = ' '.join(word)                 # " ".join() : 문자열 합칠 때, 각각의 문자열 사이에 들어갈 내용.join(문자열)
    return  result


words = []
words = input('변환할 문자를 입력하세요 : ').split()



print(change2(words))





















