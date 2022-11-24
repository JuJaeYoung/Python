import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

fps = pygame.time.Clock()

image_bg = pygame.image.load("image/Blue Sky.svg")
image_monkey = pygame.image.load("image/monkey.svg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

x_pos_monkey = size_bg_width/2 - size_monkey_width/2
y_pos_monkey = size_bg_height - size_monkey_height

to_x = 0
to_y = 0

play = True
while play:
   deltaTime = fps.tick(60)
   for event in pygame.event.get():      # 발생하는 이벤트
      if event.type == pygame.QUIT:      # 종료하고 싶다면
         play = False
      if event.type == pygame.KEYDOWN:   # 키보드 입력값을 아스키코드로 변환
         if event.key == pygame.K_UP:
            to_y = -2
         elif event.key == pygame.K_DOWN:
            to_y = 2
         elif event.key == pygame.K_RIGHT:
            to_x = 2
         elif event.key == pygame.K_LEFT:
            to_x = -2
      elif event.type == pygame.KEYUP:   
         if event.key == pygame.K_UP:
            to_y = 0
         elif event.key == pygame.K_DOWN:
            to_y = 0
         elif event.key == pygame.K_RIGHT:
            to_x = 0
         elif event.key == pygame.K_LEFT:
            to_x = 0

   x_pos_monkey += to_x                         # 누적 x
   y_pos_monkey += to_y                         # 누적 y

   background.blit(image_bg, (0,0))      # 게임창과 크기가 같은 배경을 가져와야함. 왼쪽위모서리(0,0)
   background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
   pygame.display.update()

pygame.quit()