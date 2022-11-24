import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

play = True
while play:
   for event in pygame.event.get():      # 발생하는 이벤트
      if event.type == pygame.QUIT:      # 종료하고 싶다면
         play = False


pygame.quit()