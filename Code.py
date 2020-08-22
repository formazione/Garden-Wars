import pygame
from pygame import mixer
import time, math, random

pygame.init()
screen = pygame.display.set_mode((500, 500))
icon = pygame.image.load("Gem.png")
pygame.display.set_caption("Garden Wars")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


#Player
player = pygame.image.load("Player.png")
playerX = 215
playerY = 400
X_Change = 0
y_change = 0
#Bird
bird = pygame.image.load("Birdy.png")
birdX = 500
birdY = 100
birdX_Change = 0
b = 1
#title
title = pygame.image.load("title.png")
titleX = 200
titleY = 50
#end
end = pygame.image.load("Ending.png")
endX = 150
endY = -1000
#hints
hint = pygame.image.load("Hints.png")
hintX = 0
hintY = 100
#background
background = pygame.image.load("Background.png")
backgroundX = 0
backgroundY = 0
background_change = 0
#background2
background2 = pygame.image.load("background2.png")
background2X = 0
background2Y = -500
background_change2 = 0
#background3
background3 = pygame.image.load("background3.png")
background3X = 0
background3Y = -500
background_change3 = 0
c = 1
#background4
background4 = pygame.image.load("background3.png")
background4X = 0
background4Y = 0

#Apply
apple = pygame.image.load("Apply.png")
appleX = 250
appleY = -60
apple_change = 0
#Bullet
bullet = pygame.image.load("bullet.png")
bulletY = playerY
bulletX = playerX
bullet_change = 0
a = 1
#enemy 
enemy = pygame.image.load("enemy.png")
enemyX = 250
enemyY = 50
enemy_change = 0
enemy2X = 100
enemy2Y = 50
enemy_change2 = 0
enemy3X = 50
enemy3Y = 50
enemy_change3 = 0
#gem
gem = pygame.image.load("Gem.png")
gemX = 250
gemY = 450
gem_change = 3
gem_change2 = 0
score = 0
#Jack
jack = pygame.image.load("Jack.png")
jackX = 250
jackY = -60
health = 20
e = 1
f = 1
u = 2
#Score
text = pygame.font.Font("freesansbold.ttf", 15)
textX = 0
textY = 10
#Jack Healt
textss = pygame.font.Font("freesansbold.ttf", 15)
yy = -30
#over
over = pygame.image.load("Over.png")
overX = 150
overY = -1000
#over2
over2 = pygame.image.load("Over2.png")
overX2 = 150
overY2 = -1000
v = 1
high_scores = score





# mixer.music.load("Background.mp3")
# mixer.music.play(-1)

def Player():
    screen.blit(player,(playerX, playerY))

def Title():
    screen.blit(title,(titleX, titleY))

def End():
    screen.blit(end,(endX, endY))


def Background():
    screen.blit(background,(backgroundX, backgroundY))

def Background2():
    screen.blit(background2,(background2X, background2Y))

def Background3():
    screen.blit(background3,(background3X, background3Y))

def Background4():
    screen.blit(background4,(background4X, background4Y))

def Bullet():
    screen.blit(bullet,(bulletX, bulletY))


def Enemy(x, y ):
    screen.blit(enemy,(x, y))

def Birdy():
    screen.blit(bird,(birdX, birdY))

def collision(X2, Y2, X3, Y3):
        distance = math.sqrt(math.pow(X2 - X3, 2) + math.pow(Y2 - Y3, 2))
        if distance < 27:
            return True
        else:
            return False
def Gem():
    screen.blit(gem,(gemX,gemY))

def Apple():
    screen.blit(apple,(appleX,appleY))

def Jack():
    screen.blit(jack,(jackX, jackY))

def hints():
    screen.blit(hint,(hintX, hintY))

def scores(x, y):
    font = text.render("Score:" + str(score), True, (0, 255, 0))
    screen.blit(font,(x, y))
    

def healths(x):
    fonts = textss.render("Jack Health:" + str(health), True, (255, 0, 0))
    screen.blit(fonts,(x, yy))

def Over():
    screen.blit(over,(overX, overY))

def Over2():
    screen.blit(over2,(overX2,overY2))






bomb = mixer.Sound("Bomb.wav")
while True:
   #screen.fill((0, 150, 0))






   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()


       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT and u == 2:
               X_Change =  -2
               hintY = 1000
               f = 2
               titleX = 1000
           if event.key == pygame.K_RIGHT and u == 2:
               X_Change = 2
               hintY = 1000
               f = 2
               titleX = 1000
           if event.key == pygame.K_x:
                bullet_change = 2
                hintY = 1000
                f = 2
                titleX = 1000
                a = 2
           if event.key == pygame.K_SPACE and v == 2:
               playerX = 215
               playerY = 400
               X_Change = 0
               y_change = 0
               birdX = 500
               birdY = 100
               birdX_Change = 0
               b = 1
               titleX = 200
               titleY = 50
               endX = 150
               endY = -1000
               hintX = 0
               hintY = 100
               backgroundX = 0
               backgroundY = 0
               background_change = 0
               background2X = 0
               background2Y = -500
               background_change2 = 0
               background3X = 0
               background3Y = -500
               background_change3 = 0
               c = 1
               background4X = 0
               background4Y = 0
               appleX = 250
               appleY = -60
               apple_change = 0
               bulletY = playerY
               bulletX = playerX
               bullet_change = 0
               a = 1
               enemyX = 250
               enemyY = 50
               enemy_change = 0
               enemy2X = 100
               enemy2Y = 50
               enemy_change2 = 0
               enemy3X = 50
               enemy3Y = 50
               enemy_change3 = 0
               gemX = 250
               gemY = 450
               gem_change = 3
               gem_change2 = 0
               jackX = 250
               jackY = -60
               health = 20
               e = 1
               f = 1
               u = 2
               textX = 0
               textY = 10
               yy = -30
               overX = 200
               overY = -1000
               overX2 = 200
               overY2 = -1000
               mixer.music.load("Background.mp3")
               mixer.music.play(-1)
               v = 1
               score = 0









       if event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT or pygame.K_LEFT:
               X_Change = 0








   playerX += X_Change
   bulletY -= bullet_change
   enemyY += enemy_change
   enemy2Y += enemy_change2
   enemy3Y += enemy_change3
   gemX += gem_change
   backgroundY += background_change
   background2Y += background_change2
   background3Y += background_change3
   birdX -= birdX_Change
   appleY += apple_change
   playerY += y_change
   gemY += gem_change2




   if playerX >= 450:
       playerX = 450
   elif playerX <= -15:
       playerX = -15

   if gemX >= 450:
       gem_change = -3
   elif gemX <= 0:
       gem_change = 3

   if background2Y >= 0 and b == 1:
       apple_change = 1
       b = 2

   if background3Y >= 0:
       birdX_Change = 2


   if birdX <= 0:
       birdY += 90
       birdX += 500

   elif birdY >= 500:
       birdY -= 500

   if appleY >= 500 and u ==2:
       appleY -= 500
       appleX = random.randint(0, 400)

   if f == 2:
       enemy_change = 0.2
       enemy_change2 = 0.2
       enemy_change3 = 0.2












   if a == 1:
       bulletX = playerX
       bulletY = playerY


   if bulletY <= 0:
       bulletY = 450
       bullet_change = 0
       a = 1


   C = collision(enemyX, enemyY, bulletX, bulletY)
   A1 = collision(enemy3X, enemy3Y, bulletX, bulletY)
   C2 = collision(enemy2X, enemy2Y, bulletX, bulletY)
   C3 = collision(enemy2X, enemy2Y, gemX, gemY)
   C10 = collision(enemy3X, enemy3Y, gemX, gemY)
   C4 = collision(enemyX, enemyY, gemX, gemY)
   C5 = collision(birdX, birdY, gemX, gemY)
   C6 = collision(birdX, birdY, bulletX, bulletY)
   C7 = collision(appleX, appleY, bulletX, bulletY)
   C8 = collision(appleX, appleY, gemX, gemY)
   C9 = collision(jackX, jackY, bulletX, bulletY)
   D1 = collision(enemyX, enemyY, playerX, playerY)
   D2 = collision(enemy2X, enemy2Y, playerX, playerY)
   D3 = collision(appleX, appleY, playerX, playerY)
   D4 = collision(birdX, birdY, playerX, playerY)
   D5 = collision(enemy3X, enemy3Y, playerX, playerY)

   if C:
       bulletY = 450
       bullet_change = 0
       a = 1
       score += 1
       print("Collision")
       enemyY = 0
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()

   if A1:
       bulletY = 450
       bullet_change = 0
       a = 1
       score += 1
       print("Collision")
       enemy3Y = 0
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()

   if C2:
       bulletY = 450
       bullet_change = 0
       a = 1
       print("Collision")
       enemy2Y = 0
       score += 1
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()

   if C6:
       bulletY = 450
       bullet_change = 0
       a = 1
       print("Collision")
       birdY = 0
       score += 3
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()

   if C3 or C4 or C5 or C8 or C10:
       gemY = -1000
       playerY = 10000000
       bulletY = playerY
       bomb = mixer.Sound("Bomb.wav")
       overY2 = 20
       v = 2
       bomb.play()

   if C7:
       bulletY = 450
       bullet_change = 0
       a = 1
       print("Collision")
       appleY = -1000
       appleX = random.randint(0, 400)
       score += 2
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()

   if C9:
       bulletY = 450
       bullet_change = 0
       a = 1
       print("Collision")
       health -= 1
       score += 1
       bomb = mixer.Sound("Bomb.wav")
       bomb.play()




   if D1 or D2 or D3 or D4 or D5:
       v = 2
       playerY = 10000000
       bulletY = playerY
       
       overY2 = 20
       bomb.play()





   Background()

   if score >= 75 and e == 1:
       jackY = 0
       jackX = 200
       sounds = mixer.Sound("Laugh.wav")
       sounds.play()
       mixer.music.load("Boss.mp3")
       yy += 50
       mixer.music.play(-1)
       e = 2

   if health == 0 and u == 2:
       jackY = 100000
       yy = 10000
       gem_change = 0
       enemyY = -1000
       appleX = 10000
       enemy2X = 10000
       birdX = 100000
       sound = mixer.Sound("Bomb.wav")
       playerX = 215
       y_change -= 1
       endY = 20
       gemX = 215
       gem_change2  -= 1
       enemy3X = 1000
       overY = 250
       sound.play()
       health = 1000
       x_change = 0
       bulletX += 10000
       u = 1
       v = 2




















   Bullet()
   Gem()
   Player()
   Enemy(enemyX, enemyY)
   Enemy(enemy2X, enemy2Y)
   Enemy(enemy3X, enemy3Y)
   Birdy()
   Apple()
   Jack()
   scores(textX, textY)
   healths(380)
   hints()
   Title()
   End()
   Over()
   Over2()




   pygame.display.update()
   clock.tick(120)

pygame.quit()