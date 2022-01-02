# 집게 클래스 만들기
import os
import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image  # 필수 선언
        self.rect = image.get_rect(center=position)  # 필수 선언

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image  # 필수 선언
        self.rect = image.get_rect(center=position)  # 필수 선언


def setup_gemstone():
    # 작은 금
    # 0 번째 이미지를 (200, 380) 위치에 둔다
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold)  # 그룹에 추가
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("황금 캐기 (Gold Miner)")
clock = pygame.time.Clock()

# 배경 이미지 불러 오기
current_path = os.path.dirname(__file__)  # 파일의 현재 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")), pygame.image.load(os.path.join(current_path, "big_gold.png")), pygame.image.load(os.path.join(current_path, "stone.png")), pygame.image.load(os.path.join(current_path, "diamond.png"))]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()  # 게임에 원하는 만큼의 보석을 정의

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30)  # FPS (Frame Per Second) 값이 30으로 고정, 즉 game 속도가 일정하게 됨

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)  # 그룹 내 모든 스프라이트를 screen 에 그림
    claw.draw(screen)  #

    pygame.display.update()  # 현재 화면 갱신
# pygame.time.delay(3000)
pygame.quit()
