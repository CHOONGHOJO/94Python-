# 기본 뼈대 생성
import pygame

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

running = False
while running:
    clock.tick(30) # FPS (Frame Per Second) 값이 30으로 고정, 즉 game 속도가 일정하게 됨

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.time.delay(3000)


pygame.quit()

















