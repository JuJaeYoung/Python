def func():
    print("In function [func]")
    print("안녕하세요...^^")         # 반환값 없이 출력만 시행하는 함수

for i in range(3):
    print(i,'번째')
    func()

def funcc(s):
    print("안녕하세요.",s)           # 인자가 존재하는 함수 

for i in range(2):
    funcc(i)