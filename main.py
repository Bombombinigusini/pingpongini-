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
propyshenoP = 0
propyshenoL = 0

font.init()
font2 = font.SysFont('Arial', 35)  

text_propyshenoP = font2.render('Пропущено:' + str(propyshenoP), 1, (0,0,0))
text_propyshenoL = font2.render('Пропущено:' + str(propyshenoL), 1, (0,0,0))


clock = time.Clock()
FPS = 60
game = True
speed_x = 3
speed_y = 3
finish = False


while game:
    window.fill((200,255,255))
    
    
    if ball.rect.x < 0:
        ball.rect.x = 250
        ball.rect.y = 250
        propyshenoL += 1

    if ball.rect.x > 700:
        ball.rect.x = 250
        ball.rect.y = 250
        propyshenoP += 1  
    
    text_propyshenoP = font2.render('Пропущено:' + str(propyshenoP), 1, (0,0,0))
    window.blit(text_propyshenoP,(450,25))

    text_propyshenoL = font2.render('Пропущено:' + str(propyshenoL), 1, (0,0,0))
    window.blit(text_propyshenoL,(50,25))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if propyshenoP > 3:
        text_propyshenoP = font2.render(
            'YOU LOSE', True, (255,215,0) )
        text_propyshenoL = font2.render(
            'YOU WIN', True, (255,215,0) )
        finish = True
        window.blit(text_propyshenoP,(450,250))
        window.blit(text_propyshenoL,(50,250))
        display.update()     

    if propyshenoL > 3:
        text_propyshenoL = font2.render(
            'YOU LOSE', True, (255,215,0) )
        text_propyshenoP = font2.render(
            'YOU WIN', True, (255,215,0) )

        finish = True
        window.blit(text_propyshenoP,(450,250))
        window.blit(text_propyshenoL,(50,250))
        display.update()     

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_heigth-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(palka_l, ball)  or sprite.collide_rect(palka_r, ball):
            speed_x *= -1
    keys_pressed = key.get_pressed()
    if keys_pressed[K_RETURN]:
        propyshenoL = 0
        propyshenoP = 0
        finish = False


    palka_l.update_l()
    palka_l.reset()
    palka_r.update_r()
    palka_r.reset()
    ball.update()
    ball. reset()
    display.update()
    clock.tick(FPS)