import sys
from pygame.locals import *
from pygame import mixer
from RayCaster import *

pygame.init()
pygame.display.set_caption('Juegazazazazo Inc.')
screen = pygame.display.set_mode((1000, 500), pygame.DOUBLEBUF | pygame.HWACCEL)  # , pygame.FULLSCREEN)
screen.set_alpha(None)
clock = pygame.time.Clock()
mainClock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps


r = Raycaster(screen)
r.load_map('fondoDeBikini.txt')

def escribir(text, size, color, surface, x, y):
    font = pygame.font.Font(pygame.font.match_font('comicsansms'), size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def Jugar():
    isRunning = True
    while isRunning:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isRunning = False

            newX = r.player['x']
            newY = r.player['y']

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    isRunning = False
                elif ev.key == pygame.K_UP:
                    newX += cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY += sin(r.player['angle'] * pi / 180) * r.stepSize
                elif ev.key == pygame.K_DOWN:
                    newX -= cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY -= sin(r.player['angle'] * pi / 180) * r.stepSize
                elif ev.key == pygame.K_LEFT:
                    newX -= cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY -= sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
                elif ev.key == pygame.K_RIGHT:
                    newX += cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY += sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
                elif ev.key == pygame.K_a:
                    r.player['angle'] -= 5
                elif ev.key == pygame.K_d:
                    r.player['angle'] += 5

                i = int(newX / r.blocksize)
                j = int(newY / r.blocksize)

                if r.map[j][i] == ' ':
                    r.player['x'] = newX
                    r.player['y'] = newY

        screen.fill(pygame.Color("gray"))  # Fondo

        # Techo
        screen.fill(pygame.Color("saddlebrown"), (int(r.width / 2), 0, int(r.width / 2), int(r.height / 2)))

        # Piso
        screen.fill(pygame.Color("dimgray"), (int(r.width / 2), int(r.height / 2), int(r.width / 2), int(r.height / 2)))

        r.render()

        # FPS
        screen.fill(pygame.Color("black"), (0, 0, 30, 30))
        screen.blit(updateFPS(), (0, 0))
        clock.tick(30)

        pygame.display.update()

Jugar()

pygame.quit()
