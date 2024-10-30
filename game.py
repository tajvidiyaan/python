import pygame
import random
import math
from pygame import mixer
#
#
pygame.init()
#
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('space.jpg')

# Sound
mixer.music.load("aspose_55e14ef8e781e1de9cb6a6239ba4cd10_vgxem5av.wav")
mixer.music.play(-1)

#
#
#
wall = pygame.image.load('space.jpg')
pygame.display.set_caption("Game")
icon = pygame.image.load('icons8-alien-48.png')
pygame.display.set_icon(icon)
#
#

# Player
playerImg = pygame.image.load('icons8-rocket-66.png')
playerX = 370
playerY = 480
playerX_change = 0


# player = pygame.image.load('icons8-money-bag-96.png')
# playerX = 268
# playerY = 560
# # play_x = 0
# #
#
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('icons8-alien1-96.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)








#
# enemyImageNumber = random.randint(1,4)
# if enemyImageNumber ==1:
#      enemy = pygame.image.load('e1.png')
# elif enemyImageNumber ==2:
#     enemy = pygame.image.load('e2.png')
# elif enemyImageNumber ==3:
#     enemy = pygame.image.load('e3.png')
# elif enemyImageNumber ==4:
#     enemy = pygame.image.load('e4.png')
# elif enemyImageNumber ==5:
#     enemyImg = pygame.image.load('e5.png')
# elif enemyImageNumber ==6:
#     enemyImg = pygame.image.load('e6.png')
# elif enemyImageNumber ==7:
#     enemyImg = pygame.image.load('e7.png')
# elif enemyImageNumber ==8:
#     enemyImg = pygame.image.load('e8.png')
# elif enemyImageNumber ==8:
#     enemyImg = pygame.image.load('e9.png')

# # enemy = pygame.image.load('icons8-color8-64.png')
# enemyX = random.randint(200,300)
# enemyY = random.randint(50,100)
# enemy_x =0.1
# enemy_y =10


# ball = pygame.image.load('ball.png')
# ballX = 0
# ballY = 720
# ball_x = 0
# ball_y = 10
# ball_state = "ready"

bulletImg = pygame.image.load('ball.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
#
# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
#
textX = 10
testY = 10
#
#
# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64 )

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
#
#
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
#
#
def player(x, y):
    screen.blit(playerImg, (x, y))
#
#
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
#
#
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
#
#
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# def dis (x1 , y1 , x2 , y2):
#     distance =math.sqrt(math.pow(x2-x1),2) + math.pow((y2-y1),2)
#     if distance <30:
#         return True
#     else:
#         return False
# def ba(x,y):
#     global ball_state
#     ball_state = "fire"
#     screen.blit(ball, (x+10, y+20))
# def en (x,y):
#     screen.blit(enemy, (x,y))
# def play(x,y):
#     screen.blit(player, (x, y))
# #
# #
# # # def scale_image(image, new_width):
# # #     image_scale = new_width / image.get_rect().width
# # #     new_height = image.get_rect().height*image_scale
# # #     scaled_size = (new_width , new_height)
# # #     return pygame.transform.scale((image,scaled_size)
# # #
# # #
# # # bg = pygame.image.load('Untitled.png')
# # # bg = scale_image(bg , pygame_width)
# #
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 play_x = 0.2
#             if event.key == pygame.K_LEFT:
#                 play_x = -0.2
# #
# #             if event.key == pygame.K_SPACE:
# #                 print("space")
# #                 if ball is ball_state:
# #                     ballX = playerX
# #                     ball_state = 'fire'
# #                     ba(ballX, ballY)
# #
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
#                 play_x = 0.1
# #
# #
# #
# #
# #     screen.blit(wall,(0,0))
# #     playerX += play_x
# #     if playerX <= 0:
# #         playerX = 0
# #     elif playerX >= 436:
# #         playerX = 436
# #
# #     enemyX += enemy_x
# #     if enemyX <= 0:
# #         enemy_x = 0.1
# #         enemy_y += enemy_y
# #     elif enemyX >= 436:
# #         enemy_x -= 0.1
# #         enemyY += enemy_y
# #
# #
# #
# #     if ball_state is "fire":
# #         ba(playerX, ballY)
# #         ballY -= ball_y
# #         # if ballY <= 0:
# #         #     ball_state = "ready"
# #         #     ballY = 720
# #
# #
# #
# #
#     # playerX += play_x
#     play(playerX, playerY)
# #     en(enemyX, enemyY)
#     pygame.display.update()

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #
    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("aspose_55e14ef8e781e1de9cb6a6239ba4cd10_vgxem5av.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    #
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    # #
    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()