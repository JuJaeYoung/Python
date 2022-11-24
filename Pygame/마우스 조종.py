import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

x_pos = background.get_size()[0]//2      # 480 // 2
y_pos = background.get_size()[1]//2      # 360 // 2

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:      
            play = False
        if event.type == pygame.MOUSEMOTION:       # 마우스 움직임
            x_pos, y_pos = pygame.mouse.get_pos()
            # pygame.draw.circle(background, (255,0,255), (x_pos,y_pos), 10)
        # elif event.type == pygame.MOUSEBUTTONDOWN: # 마우스 누르고
        #     # print(event.button)                   # 마우스 움직임 출력
        #     # if event.button == 1:
        #     #     print('왼쪽 클릭')
        #     # elif event.button == 2:
        #     #     print('휠 클릭')
        #     # elif event.button == 3:
        #     #     print('오른쪽 클릭')
        #     # elif event.button == 4:
        #     #     print('휠 올리기')
        #     # elif event.button == 5:
        #     #     print('휠 내리기')
        #     # if event.button == 1:
        #     #     background.fill((0,0,0))
        # elif event.type == pygame.MOUSEBUTTONUP:   # 마우스 떼고
        #     # print("MOUSEBUTTONUP")
        #     pass

    background.fill((255,255,255))
    pygame.draw.circle(background, (0,0,255), (x_pos, y_pos), 5)
    pygame.display.update()



pygame.quit()