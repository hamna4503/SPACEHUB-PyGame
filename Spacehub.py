#importing

import random
import sys
import math
import pygame

# game variables

pygame.init()
pygame.mixer.init()

screen_width = 900
screen_height = 600

exit_game = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
score = 0

l = [0]

positive = pygame.mixer.Sound("audio/positive.mp3")
font = pygame.font.Font("freesansbold.ttf", 38)

# for collision

def iscollision(aestroid_1x, aestroid_1y, ship_x, ship_y):
    distance = abs(math.sqrt((math.pow(aestroid_1x - ship_x, 2) + math.pow(aestroid_1y - ship_y, 2))))

    if distance < 50:
        return True

    else:
        return False


# gameover function

def gameover():

    #gameover image loading

    over = pygame.image.load("game_obj/gameover.png")
    over = pygame.transform.scale(over, (screen.get_width(), screen.get_height())).convert_alpha()
    screen.blit(over, (0, 0))

    #score display on game over

    score_total = font.render('Score: ' + str(int(l[-1])), True, (255, 255, 255))
    screen.blit(score_total, (screen.get_width() / 3, screen.get_height() / 3 + 100))
    high_score = font.render('High Score: ' + str(int(max(l))), True, (255, 255, 255))
    screen.blit(high_score, (screen.get_width() / 3, (screen.get_height() / 2) + 60))

    pygame.display.update()
    exit_game = False

    while not exit_game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True
                sys.exit()

            if event.type == pygame.WINDOWRESIZED:
                over = pygame.transform.scale(over, (screen.get_width(), screen.get_height())).convert_alpha()
                screen.blit(over, (0, 0))
                screen.blit(score_total, (screen.get_width() / 3, (screen.get_height() / 3) + 100))
                screen.blit(high_score, (screen.get_width() / 3, (screen.get_height() / 2) + 60))
                pygame.display.update()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(positive)
                    gameloop()

                if event.key == pygame.K_ESCAPE:
                    exit_game = True
                    sys.exit()

# title screen for game

def title():

    icon = pygame.image.load('game_obj/icon2.png').convert_alpha()
    pygame.display.set_caption("SPACEHUB")
    pygame.display.set_icon(icon)
    welcome = pygame.image.load("game_obj/welcome.png")
    welcome = pygame.transform.scale(welcome, (screen.get_width(), screen.get_height())).convert_alpha()
    screen.blit(welcome, (0, 0))
    pygame.display.update()
    exit_game = False


    while not exit_game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.WINDOWRESIZED:
                welcome = pygame.transform.scale(welcome, (screen.get_width(), screen.get_height()))
                screen.blit(welcome, (0, 0))
                pygame.display.update()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(positive)
                    gameloop()

                if event.key == pygame.K_ESCAPE:
                    exit_game = True
                    sys.exit()


# main game loop

def gameloop():
    # gamevars

    fps = 60
    score = 0
    exit_game = False
    clock = pygame.time.Clock()

    # setting initial coordinates

    ship_x = 3
    ship_y = 250
    aestroid1_x = 1500
    aestroid1_y = 40
    aestroid2_x = 1500
    aestroid2_y = 80
    aestroid3_x = 1500
    aestroid3_y = 20

    # for moving aestroid (speed of aestroids)

    aestroid3_x_change = -15
    aestroid1_x_change = -10
    aestroid2_x_change = -17

    # displayvars

    background = pygame.image.load('game_obj/background1.png').convert_alpha()
    icon = pygame.image.load('game_obj/icon2.png').convert_alpha()
    ship = pygame.image.load('game_obj/ship4.png').convert_alpha()
    ship = pygame.transform.scale(ship, (90, 90)).convert_alpha()
    aestroid1 = pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid1 = pygame.transform.scale(aestroid1, (100, 100)).convert_alpha()
    aestroid2 = pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid2 = pygame.transform.scale(aestroid2, (100, 100)).convert_alpha()
    aestroid3 = pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid3 = pygame.transform.scale(aestroid3, (100, 100)).convert_alpha()
    pygame.display.set_caption("SPACEHUB")
    pygame.display.set_icon(icon)
    pygame.display.update()

    # audio

    #for game music

    pygame.mixer.music.load("audio/main_audio2.mp3")
    pygame.mixer.music.set_volume(40)
    pygame.mixer.music.play(-1)  # to play song infinitely

    #for game sounds

    whoosh = pygame.mixer.Sound("audio/whoosh.mp3")
    crash = pygame.mixer.Sound("audio/crash.mp3")

    # to display ship multiple times

    def displayship(x_shipfun, y_shipfun):
        screen.blit(ship, (x_shipfun, y_shipfun))

    # main game loop
    while not exit_game:

        # blitting

        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height())).convert_alpha()
        screen.blit(background, (0, 0))
        displayship(ship_x, ship_y)

        # aestroid blit at start

        screen.blit(aestroid1, (aestroid1_x, aestroid1_y))
        screen.blit(aestroid2, (aestroid2_x, aestroid2_y))
        screen.blit(aestroid3, (aestroid3_x, aestroid3_y))

        # score blit

        score_show = font.render('Score:' + str(int(score)), True, (255, 255, 255)).convert_alpha()
        screen.blit(score_show, (720, 10))
        high_score = font.render('High SCORE :' + str(int(max(l))), True, (255, 255, 255)).convert_alpha()
        screen.blit(high_score, (20, 10))

        pygame.display.update()

        # pygame events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True
                sys.exit()

            if event.type == pygame.WINDOWRESIZED:
                background = pygame.transform.scale(background, (screen.get_width(), screen.get_height())).convert_alpha()
                screen.blit(background, (0, 0))
                screen.blit(score_show, (960, 10))
                screen.blit(high_score, (20, 10))
                pygame.display.update()

            # keyboard controls

            if event.type == pygame.KEYDOWN:

                if ship_y <= 575 and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    pygame.mixer.Sound.play(whoosh)
                    ship_y += 45

                if ship_y > 0 and (event.key == pygame.K_UP or event.key == pygame.K_w):
                    ship_y -= 45
                    pygame.mixer.Sound.play(whoosh)

                if ship_x <= 1280 and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    ship_x += 45
                    pygame.mixer.Sound.play(whoosh)

                if ship_x > 3 and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    ship_x -= 45
                    pygame.mixer.Sound.play(whoosh)

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        # aestroid blit logic

        aestroid1_x += aestroid1_x_change
        aestroid2_x += aestroid2_x_change
        aestroid3_x += aestroid3_x_change
        if aestroid1_x <= -100:
            screen.blit(background, (0, 0))
            displayship(ship_x, ship_y)
            aestroid1_x = 1500
            aestroid1_y = random.randint(-30, 200)
            screen.blit(aestroid1, (aestroid1_x, aestroid1_y))
            pygame.display.update()

        if aestroid2_x <= -100:
            screen.blit(background, (0, 0))
            displayship(ship_x, ship_y)
            aestroid2_x = 1500
            aestroid2_y = random.randint(350, 570)
            screen.blit(aestroid2, (aestroid2_x, aestroid2_y))
            pygame.display.update()

        if aestroid3_x <= -100:
            screen.blit(background, (0, 0))
            displayship(ship_x, ship_y)
            aestroid3_x = 1500
            aestroid3_y = random.randint(150, 410)
            screen.blit(aestroid3, (aestroid3_x, aestroid3_y))
            pygame.display.update()

        # to check collision

        collision = iscollision(aestroid1_x, aestroid1_y, ship_x, ship_y) \
                    or iscollision(aestroid2_x, aestroid2_y, ship_x, ship_y) or \
                    iscollision(aestroid3_x, aestroid3_y, ship_x, ship_y)

        # score

        score += (0.025 * 3)

        # for gameover

        if collision:
            pygame.mixer.music.fadeout(10)
            pygame.mixer.Sound.play(crash)
            l.append(score)
            gameover()
            screen.blit(score_show, (760, 10))
            pygame.display.update()

        #
        displayship(ship_x, ship_y)
        pygame.display.update()
        clock.tick(fps)

title()
pygame.quit()
quit()
