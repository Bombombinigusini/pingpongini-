from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,shirina=65, visota=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(shirina,visota))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
 
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 295:
            self.rect.y  += self.speed
    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y  -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 295:
            self.rect.y  += self.speed
        

palka_l = Player('pfkri.png',10, 20, 10, 70, 200)
palka_r = Player('pfkr.png',600, 20, 10, 70, 200)
ball = GameSprite('t.png', 250, 250, 100, 60, 60)
win_width = 700
win_heigth = 500
window = display.set_mode(
    (win_width, win_heigth)
)

clock = time.Clock()
FPS = 60
game = True
speed_x = 3
speed_y = 3
finish = False

while game:
    window.fill((200,255,255))
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_heigth-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(palka_l, ball)  or sprite.collide_rect(palka_r, ball):
            speed_x *= -1


        palka_l.update_l()
        palka_l.reset()
        palka_r.update_r()
        palka_r.reset()
        ball.update()
        ball. reset()
    display.update()
    clock.tick(FPS)