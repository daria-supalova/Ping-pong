from pygame import *
from random import *

font.init()
font1 = font.Font(None, 36)

img_back = "background.png"

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y += self.speed
       if keys[K_DOWN] and self.rect.y < 495:
           self.rect.y -= self.speed
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y += self.speed
       if keys[K_s] and self.rect.y < 495:
           self.rect.y -= self.speed

win_width = 700
win_height = 500

display.set_caption("Shooter")
#background = transform.scale(image.load(img_back), (win_width, win_height))

back = (200, 255, 255) 
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
       if e.type == QUIT:
           game = False

    if not finish:
        window.fill(back)
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.reset()

        display.update()

    time.delay(50)

