import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

x = background.get_size()[0]//2
y = background.get_size()[1]//2

play = True
while play:
   for event in pygame.event.get():      # 발생하는 이벤트
      if event.type == pygame.QUIT:      # 종료하고 싶다면
         play = False
   background.fill((255,255,255))

   # 선
   # pygame.draw.line(화면, 색, 시작위치, 끝위치, 선굵기)
   # pygame.draw.line(background, (0,0,0), (240,0), (240,360))
   # pygame.draw.line(background, (0,0,0), (0,180), (480,180))

   # for i in range(0,480,30):
   #    pygame.draw.line(background, (0,0,0), (i,0), (i,360))    # 세로선 여러개
   # for i in range(0, 360, 30): 
   #    pygame.draw.line(background, (0,0,0), (0, i), (480, i))  # 가로선 여러개

   # 원
   # pygame.draw.circle(화면, 색, 중심좌표, 반지름, 선굵기)
   # pygame.draw.circle(background, (255,0,0), (240,180), 50)     # 선굵기 지정안하면 채우기
   # pygame.draw.circle(background, (255,0,0), (240,180), 50, 5)

   # 사각형
   # pygame.draw.rect(화면, 색, 위치와 크기, 선굵기)
   # pygame.draw.rect(background, (0,255,0), (240,180,100,50))    # 선굵기 지정안하면 채우기
   # pygame.draw.rect(background, (0,255,0), (240,180,100,50), 5)

   # 타원
   # pygame.draw.ellipse(화면, 색, 위치와 크기, 선굵기)
   # pygame.draw.ellipse(background, (0,0,255), (240,180,100,50))
   # pygame.draw.ellipse(background, (0,0,255), (240,180,100,50), 5)

   # 다각형
   # pygame.draw.polygon(화면, 색, 점들위 위치, 선굵기)
   # pygame.draw.polygon(background, (255,255,0), [[100,100],[0,200],[200,200]])
   # pygame.draw.polygon(background, (255,255,0), [[100,100],[0,200],[200,200]], 5)
   # pygame.draw.polygon(background, (255,255,0), [[146,0],[291,106],[236,277],[56,277],[0,106]])

   # 축
   pygame.draw.line(background, (0,0,0), (x,0), (x,y*2))
   pygame.draw.line(background, (0,0,0), (0,y), (x*2,y))

   pygame.display.update()

pygame.quit()