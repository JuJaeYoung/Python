from turtle import *

def open_file(x):                      # 파일 열기
    f = open(x,"r") 
    lines = f.readlines()
    f.close()
    return lines

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
    
lines = open_file(input())

for line in lines:
    if "point" in line:
        l = line.split()
        p = Point(l[1], l[2], int(l[3]))
    elif "move" in line:
        l = line.split()
        p.move(int(l[1]), int(l[2]))
    elif "circle" in line:
        l = line.split()
        p.circle(int(l[1]), int(l[2]))
    elif "line" in line:
        l = line.split()
        p.line(int(l[1]))
    elif "angle" in line:
        l = line.split()
        p.angle(int(l[1]))
