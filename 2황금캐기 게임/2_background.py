# 배경 이미지 생성
import os
import pygame

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 배경 이미지 불러 오기
current_path = os.path.dirname(__file__) # 파일의 현재 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# print("지금 여기는 : ", current_path)





running = True
while running:
    clock.tick(30) # FPS (Frame Per Second) 값이 30으로 고정, 즉 game 속도가 일정하게 됨

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update() # 현재 화면 갱신



# pygame.time.delay(3000)
pygame.quit()



















