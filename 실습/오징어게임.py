import turtle as t
import math as m

def move(x,y):              # 특정 위치로 펜 옮기기
    t.pu()
    t.goto(x,y)
    t.pd()

l = [120,120,300,120,300,120,120,270,60,270,120,90,200,90,300,90,200,90,120,270,60]

move(30,0)
for i in range(len(l)):
    if i % 2 == 0:          # 짝수 = 각도   
        t.fd(l[i])
    else:                   # 홀수 = 길이
        t.lt(l[i])
move(180,-30)
t.circle(30)
move(-120,-30)
t.circle(30)
move(50,m.sqrt(3) * 150)
t.circle(50)
move(50,-260)
t.circle(50)
