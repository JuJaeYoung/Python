import turtle as t
import msvcrt           # 키보드 제어

class pt:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

def Line(p1, p2):       # p1과 p2를 잇는 직선 드로잉
    t.pu()
    t.setpos(p1.x, p1.y)
    t.pd()
    t.setpos(p2.x, p2.y)

end = 0
p1 = pt(0,0)
p2 = pt(0,0)
while (end != 1):
    p1.x = p2.x
    p1.y = p2.y
    k = input()
    
    if k.lower() == "x" or k.lower() == "q":
        t.hideturtle()
        break
    elif k.lower() == "a" :
        t.seth(180)
        p2.x -= 10
    elif k.lower() == "s" :
        t.seth(-90)
        p2.y -= 10
    elif k.lower() == "d" :
        t.seth(0)
        p2.x += 10
    elif k.lower() == "w" :
        t.seth(90)
        p2.y += 10
        
    Line(p1,p2)
    print(p1.x,p1.y,p2.x,p2.y)
    
