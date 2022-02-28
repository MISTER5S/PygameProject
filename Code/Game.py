import pygame
import random
import sys
from pygame.locals import *


class Button:
    def __init__(self, text, color, x, y, font, screen):
        pygame.font.init()
        font = pygame.font.SysFont('arial', font)
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.font.init()
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))


class Button_s:
    def __init__(self, text, color, x, y, font, screen, h, w, music):

        # height  # высота
        # width   ширина
        self.width = w
        self.height = h
        pygame.font.init()
        font = pygame.font.SysFont('arial', font)
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.meteorit_group = []

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, (21, 20, 24), (x - 10, y, self.width, self.height))
            if click[0] == 1 and x == 500:
                music.stop()
                game_go()
            elif click[0] == 1 and y == 200:
                music.stop()
                tabl_go()
            elif click[0] == 1 and y == 300:
                music.stop()
                castomize()
        pygame.font.init()
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))


class Button_n:
    def __init__(self, text, color, x, y, font, screen, h, w, music):
        self.width = w
        self.height = h
        pygame.font.init()
        font = pygame.font.SysFont('arial', font)
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.meteorit_group = []
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, (21, 20, 24), (x - 10, y, self.width, self.height))
            if click[0] == 1 and x == 100:
                music.stop()
                cast_boat(r'Photo/boat_2_shield.png')
                WaitForPlayerToPressKey(1)
            elif click[0] == 1 and x == 500:
                music.stop()
                cast_boat(r'Photo/pixil_shield_1.png')
                WaitForPlayerToPressKey(1)
        pygame.font.init()
        text_r = font.render(text, True, color)
        screen.blit(text_r, (x, y))


class Surphase:
    def __init__(self, screen):
        image = pygame.image.load(r'Photo/horizon-stars-space-pixels-wallpaper-preview.jpg')
        image = pygame.transform.scale(image, (1200, 700))
        screen.blit(image, (0, 0))


def terminate():
    pygame.quit()
    sys.exit()


def game_go():
    global shield, boat, num_ch
    pygame.mixer.init()
    music = pygame.mixer.Sound(pygame.mixer.Sound(r'Music/main_music.mp3'))
    music.play(-1, 0)
    pygame.time.delay(150)
    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 700
    TEXTCOLOR = (0, 0, 0)
    FPS = 120
    BADDIEMINSIZE = 10
    BADDIEMAXSIZE = 40
    BADDIEMINSPEED = 1
    BADDIEMAXSPEED = 8
    ADDNEWBADDIERATE = 6
    PLAYERMOVERATE = 5

    def terminate():
        pygame.quit()
        sys.exit()

    def waitForPlayerToPressKey():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # pressing escape quits
                        if event.key == K_ESCAPE:  # pressing escape quits
                            WINDOWWIDTH = 1200
                            WINDOWHEIGHT = 700
                            mainClock = pygame.time.Clock()
                            windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                            pygame.display.set_caption('Dodger')
                            pygame.mouse.set_visible(True)

                            pygame.display.update()
                            while pygame.event.wait().type != pygame.QUIT:
                                music.stop()
                                WaitForPlayerToPressKey(1)
                    return

    def playerHasHitBaddie(playerRect, baddies):
        global shield, boat, num_ch
        for b in baddies:
            if playerRect.colliderect(b['rect']):
                if shield == 0:
                    return True
                elif shield == 1:
                    num_ch = 1
                    shield -= 1
                    baddies.remove(b)
                    return False
                else:
                    shield -= 1
                    baddies.remove(b)
                    return False
        return False

    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dodger')
    pygame.mouse.set_visible(False)

    font = pygame.font.SysFont(None, 48)

    playerImage = pygame.image.load(cast_boat())
    print(cast_boat())
    playerRect = playerImage.get_rect()
    baddieImage = pygame.image.load(r'Photo/metorit.png')
    image = pygame.image.load(r'Photo/horizon-stars-space-pixels-wallpaper-preview.jpg')
    image.set_colorkey((255, 255, 255))
    image = pygame.transform.scale(image, (1200, 700))
    windowSurface.blit(image, (0, 0))

    Button('Нажмите любую кнопку, чтобы начать', (255, 255, 255), (WINDOWWIDTH / 3) - 30,
           (WINDOWHEIGHT / 3) + 50, 40, windowSurface)
    pygame.display.update()
    waitForPlayerToPressKey()

    topScore = 0
    shield = 3
    while True:
        baddies = []
        score = 0
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        baddieAddCounter = 0
        # pygame.mixer.music.play(-1, 0.0)
        while True:
            if num_ch == 1:
                if boat == 'Photo/pixil_shield_1.png':
                    playerImage = pygame.image.load(r'Photo/pixil-frame-0 (2).png')
                else:
                    playerImage = pygame.image.load(r'Photo/boat_2.png')
                pygame.display.update()
                num_ch = 0
            score += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == K_z:
                        reverseCheat = True
                    if event.key == K_x:
                        slowCheat = True
                    if event.key == K_LEFT or event.key == K_a:
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == K_d:
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == K_w:
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == K_s:
                        moveUp = False
                        moveDown = True

                if event.type == KEYUP:
                    if event.key == K_z:
                        reverseCheat = False
                        score = 0
                    if event.key == K_x:
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                        WINDOWWIDTH = 1200
                        WINDOWHEIGHT = 700
                        mainClock = pygame.time.Clock()
                        windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                        pygame.display.set_caption('Dodger')
                        pygame.mouse.set_visible(True)

                        pygame.display.update()
                        while pygame.event.wait().type != pygame.QUIT:
                            music.stop()
                            WaitForPlayerToPressKey(1)

                    if event.key == K_LEFT or event.key == K_a:
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                        moveRight = False
                    if event.key == K_UP or event.key == K_w:
                        moveUp = False
                    if event.key == K_DOWN or event.key == K_s:
                        moveDown = False
                if event.type == MOUSEMOTION:
                    playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

            if not reverseCheat and not slowCheat:
                baddieAddCounter += 1
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
                newBaddie = {
                    'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize,
                                        baddieSize,
                                        baddieSize),
                    'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                    'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                }
                baddies.append(newBaddie)

            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)
            for b in baddies:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif reverseCheat:
                    b['rect'].move_ip(0, -5)
                elif slowCheat:
                    b['rect'].move_ip(0, 1)

            for b in baddies[:]:
                if b['rect'].top > WINDOWHEIGHT:
                    baddies.remove(b)
            image = pygame.image.load(r'Photo/horizon-stars-space-pixels-wallpaper-preview.jpg')
            image.set_colorkey((255, 255, 255))
            image = pygame.transform.scale(image, (1200, 700))
            windowSurface.blit(image, (0, 0))
            Button('Ваш результат: %s' % (score), (255, 255, 255), 10, 0, 40, windowSurface)
            Button('Лучший результат данной сессии: %s' % (topScore), (255, 255, 255), 10, 40, 40, windowSurface)
            Button('Нажмите esc для возвращения в главное меню', (255, 255, 255), 10, 80, 40, windowSurface)

            windowSurface.blit(playerImage, playerRect)

            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])

            pygame.display.update()

            if playerHasHitBaddie(playerRect, baddies):
                if score > topScore:
                    topScore = score
                break
            mainClock.tick(FPS)

        pygame.mixer.music.stop()
        image = pygame.image.load(r'Photo/game-over2.jpg')
        image = pygame.transform.scale(image, (1200, 700))
        windowSurface.blit(image, (0, 0))
        Button('Нажмите любую кнопку, чтобы начать заного', (255, 255, 255), 250,
               520, 40,
               windowSurface)
        pygame.display.update()
        file_o = open(r'Code/top_score.txt', 'a', encoding='utf-8')
        file_o.write('\n' + str(score))
        file_o.close()
        waitForPlayerToPressKey()


def tabl_go():
    def terminate():
        pygame.quit()
        sys.exit()

    pygame.mixer.init()
    music_t = pygame.mixer.Sound(pygame.mixer.Sound(r'Music/tabl_menu.mp3'))
    music_t.play()
    pygame.time.delay(150)
    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 700
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dodger')
    pygame.mouse.set_visible(True)
    pygame.display.update()
    file_o = open(r'Code/top_score.txt', 'r', encoding='utf-8')
    file = file_o.readlines()
    file_o.close()
    file.sort(key=lambda x: int(x))
    for i in range(len(file)):
        if '\n' in file[i]:
            file[i] = file[i][:-1]
    file.reverse()
    image = pygame.image.load(r'Photo/horizon-stars-space-pixels-wallpaper-preview.jpg')
    image.set_colorkey((255, 255, 255))
    image = pygame.transform.scale(image, (1200, 700))
    windowSurface.blit(image, (0, 0))
    while True:
        Button('Нажмите esc для возвращения в главное меню', (255, 255, 255), 0, 0, 40, windowSurface)
        Button('Лучшие результаты:', (255, 255, 255), 450, 100, 40, windowSurface)
        Button(file[0], (255, 255, 255), 550, 150, 40, windowSurface)
        Button(file[1], (255, 255, 255), 550, 200, 40, windowSurface)
        Button(file[2], (255, 255, 255), 550, 250, 40, windowSurface)
        Button(file[3], (255, 255, 255), 550, 300, 40, windowSurface)
        Button(file[4], (255, 255, 255), 550, 350, 40, windowSurface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    WINDOWWIDTH = 1200
                    WINDOWHEIGHT = 700
                    mainClock = pygame.time.Clock()
                    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                    pygame.display.set_caption('Dodger')
                    pygame.mouse.set_visible(True)

                    pygame.display.update()
                    while pygame.event.wait().type != pygame.QUIT:
                        music_t.stop()
                        WaitForPlayerToPressKey(1)
                return


def castomize():
    def terminate():
        pygame.quit()
        sys.exit()

    pygame.mixer.init()
    music = pygame.mixer.Sound(pygame.mixer.Sound(r'Music/main_music.mp3'))
    music.play()
    pygame.time.delay(150)
    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 700
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dodger')
    pygame.mouse.set_visible(True)
    pygame.display.update()
    while True:
        Surphase(windowSurface)
        Button('Нажмите esc для возвращения в главное меню', (255, 255, 255), 0, 0, 40, windowSurface)
        boat_1 = pygame.image.load(r'Photo/boat_2_shield.png')
        boat_1 = pygame.transform.scale(boat_1, (300, 300))
        boat_1.set_colorkey((255, 255, 255))
        windowSurface.blit(boat_1, (100, 100))
        Button_n('выбрать', (255, 255, 255), 100, 420, 40, windowSurface, 50, 150, music)
        boat_2 = pygame.image.load(r'Photo/pixil_shield_1.png')
        boat_2 = pygame.transform.scale(boat_2, (300, 300))
        boat_2.set_colorkey((255, 255, 255))
        windowSurface.blit(boat_2, (500, 100))
        Button_n('выбрать', (255, 255, 255), 500, 420, 40, windowSurface, 50, 150, music)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    WINDOWWIDTH = 1200
                    WINDOWHEIGHT = 700
                    mainClock = pygame.time.Clock()
                    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                    pygame.display.set_caption('Dodger')
                    pygame.mouse.set_visible(True)
                    pygame.display.update()
                    while pygame.event.wait().type != pygame.QUIT:
                        music.stop()
                        WaitForPlayerToPressKey(1)
                return


def cast_boat(*photo):
    global boat
    if photo:
        boat = photo[0]
    else:
        return boat


def WaitForPlayerToPressKey(code):
    pygame.mixer.init()
    music_st = pygame.mixer.Sound(pygame.mixer.Sound(r'Music\start_menu.mp3'))
    music_st.play()
    while True:
        if code == 1:
            Surphase(windowSurface)
            Button_s('Новая игра', (255, 255, 255), 500, 100, 40, windowSurface, 50, 190, music_st)
            Button_s('Таблица лидеров', (255, 255, 255), 460, 200, 40, windowSurface, 50, 290, music_st)
            Button_s('Кастомизация', (255, 255, 255), 485, 300, 40, windowSurface, 60, 235, music_st)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    terminate()
                return


timeout = 60.0

clock = pygame.time.Clock()
FPS = 120
boat = r'Photo/pixil_shield_1.png'

WINDOWWIDTH = 1200
WINDOWHEIGHT = 700
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(True)
pygame.display.update()
shield = 3
num_ch = 0
while pygame.event.wait().type != pygame.QUIT:
    WaitForPlayerToPressKey(1)
