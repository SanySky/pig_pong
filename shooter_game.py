
from pygame import *
from random import randint

win_wid = 700
win_hei = 500

right_score = 0
left_score = 0

window = display.set_mode((win_wid, win_hei))
display.set_caption('Пинг-понг')
window.fill((200, 255, 255))
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = (200, 255, 255)
        if color:
            self.fill_color = color

    def fill(self):
        draw.rect(window, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Player(Area):
    def __init__(self, fillname, x=0, y=0, width=10, height=10, speed=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image=image.load(fillname)
        self.speed = speed

    def draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

    def update1(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_hei - 60:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_hei - 60:
            self.rect.y += self.speed


player1 = Player('platform2.png', 30, 200, 30, 100, 9)
player2 = Player('platform2.png', win_wid - 60, 200, 30, 100, 9)
ball = Player('ball.png', 250, 225, 50, 50, 2)

fps = 60
game = True
finish = False
clock = time.Clock()
font.init()
font1  = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 50)
speed_x = ball.speed
speed_y = ball.speed

while game:
    for i in  event.get():
        if i.type == QUIT:
            game = False 

    if not finish:
        # text_win = font2.render(' you win',1,(0,0,255))
        # window.blit(text_win,(250,230))
        player1.fill()
        player2.fill()
        ball.fill()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(player1.rect) or ball.colliderect(player2.rect):
            speed_x *= -1
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            speed_y *= -1
        if ball.rect.x <= 0:
            right = font1.render("Игрок слева проиграл", True, (255, 0, 0))
            window.blit(right, (220, 220))
            finish = True
        if ball.rect.x >= 650:
            left = font1.render("Игрок справа проиграл", True, (255, 0, 0))
            window.blit(right, (220, 220))
            finish = True


        player1.update1()
        player2.update2()
        player1.draw()
        player2.draw()
        ball.draw()
       
        
    display.update()
    clock.tick(fps)
