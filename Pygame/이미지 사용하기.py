import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

# 공통된 경로는 없애도 ㄱㅊ / 확장자 svg,jpg,png 다 가능
image_bg = pygame.image.load("image/Blue Sky.svg")
image_banana = pygame.image.load("image/bananas.svg")
image_monkey = pygame.image.load("image/monkey.svg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]    # 이미지 가로
size_banana_height = image_banana.get_rect().size[1]   # 이미지 세로

x_pos_banana = size_bg_width/2 - size_banana_width/2
y_pos_banana = 0

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

x_pos_monkey = size_bg_width/2 - size_monkey_width/2
y_pos_monkey = size_bg_height - size_monkey_height

play = True
while play:
   for event in pygame.event.get():      # 발생하는 이벤트
      if event.type == pygame.QUIT:      # 종료하고 싶다면
         play = False

   background.blit(image_bg, (0,0))      # 게임창과 크기가 같은 배경을 가져와야함. 왼쪽위모서리(0,0)
   background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
   background.blit(image_banana, (x_pos_banana, y_pos_banana))
   pygame.display.update()

pygame.quit()