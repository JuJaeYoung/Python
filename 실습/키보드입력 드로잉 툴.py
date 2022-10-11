from turtle import *

class Point:            
    def __init__(self, color, size, speed):    
        # 펜 색상
        self.color = color

        # 펜 크기
        self.size = size

        # 속도
        self.speed = speed

        # 터틀 적용
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.pencolor(color)
        self.turtle.pensize(size)
        self.turtle.speed(speed)        # 0 : 제일빠른 , 1~10 : 점점 빨라짐

    def line(self, a):                  # 선 긋기
        self.turtle.forward(a)

    def circle(self, r, o):                # 원 그리기
        self.turtle.circle(r, o)
       
    def move(self, x, y):               # 특정 위치로 펜 옮기기      
        self.turtle.pu()
        self.turtle.goto(x, y)
        self.turtle.pd()

    def angle(self, h):
        self.turtle.seth(h)


while 1:
    x = input()
    if x == 'set':
        a = input('펜색깔 : ')
        b = input('펜굵기 : ')
        c = int(input('속도 : '))
        p = Point(a, b, c)
    elif x == 'w':
        p.angle(90)
        p.line(50)
    elif x == 'a':
        p.angle(180)
        p.line(50)
    elif x == 's':
        p.angle(270)
        p.line(50)
    elif x == 'd':
        p.angle(0)
        p.line(50)
    elif x == 'wd' or x == 'dw':
        p.angle(45)
        p.line(50)
    elif x == 'wa' or x == 'aw':
        p.angle(135)
        p.line(50)
    elif x == 'as' or x == 'sa':
        p.angle(225)
        p.line(50)
    elif x == 'sd' or x == 'ds':
        p.angle(-45)
        p.line(50)        
    elif x == 'c':
        s = int(input('원반지름 : '))
        o = int(input('중심각 : '))
        p.circle(s,o)
    elif x == 'm':
        a = int(input('x좌표 : '))
        b = int(input('y좌표 : '))
        p.move(a,b)
    elif x == 'x':
        break
