import pygame
import random


#Sprites
sD='sprite/' #sprite directory
cavallo_bianco = [pygame.image.load(sD+'ice00.png'),pygame.image.load(sD+'ice01.png'),pygame.image.load(sD+'ice02.png'),pygame.image.load(sD+'ice03.png'),pygame.image.load(sD+'ice04.png'),pygame.image.load(sD+'ice05.png'),pygame.image.load(sD+'ice06.png')]
cavallo_marrone=[pygame.image.load(sD+'b00.png'),pygame.image.load(sD+'b01.png'),pygame.image.load(sD+'b02.png'),pygame.image.load(sD+'b03.png'),pygame.image.load(sD+'b04.png'),pygame.image.load(sD+'b05.png'),pygame.image.load(sD+'b06.png')]
cavallo_nero=[pygame.image.load(sD+'n00.png'),pygame.image.load(sD+'n01.png'),pygame.image.load(sD+'n02.png'),pygame.image.load(sD+'n03.png'),pygame.image.load(sD+'n04.png'),pygame.image.load(sD+'n05.png'),pygame.image.load(sD+'n06.png')]
cavallo_rosso=[pygame.image.load(sD+'r00.png'),pygame.image.load(sD+'r01.png'),pygame.image.load(sD+'r02.png'),pygame.image.load(sD+'r03.png'),pygame.image.load(sD+'r04.png'),pygame.image.load(sD+'r05.png'),pygame.image.load(sD+'r06.png')]


menu=pygame.image.load(sD+'menu1.png')

sfondo=pygame.image.load(sD+'sfondo.png')
clicca_un=pygame.image.load(sD+'clicca un.png')

gameover=pygame.image.load(sD+'gameover.png')
vincitore_b=pygame.image.load(sD+'WINNER BIANCO.png')
vincitore_n=pygame.image.load(sD+'WINNER NERO.png')
vincitore_m=pygame.image.load(sD+'WINNER MARRONE.png')
vincitore_r=pygame.image.load(sD+'WINNER ROSSO.png')



c_bianco=pygame.image.load(sD+'ice.png')
xb=-22
yb=475
c_nero=pygame.image.load(sD+'nero.png')
xn=-22
yn=380
c_marrone=pygame.image.load(sD+'marrone.png')
xm=-22
ym=270
c_rosso=pygame.image.load(sD+'rosso.png')
xr=-22
yr=180


#COSTANTI

screen = pygame.display.set_mode((1080, 620))
pygame.display.set_caption('Horsin Around')

clock = pygame.time.Clock()
FPS = 21
anima=0






def animazioni():
    global anima
    screen.blit(sfondo, (0, 0))

    if anima +1>=21:
        anima=0

    if partita_iniziata:
        screen.blit(cavallo_bianco[anima//3],(xb,yb))
        screen.blit(cavallo_nero[anima // 3], (xn, yn))
        screen.blit(cavallo_marrone[anima // 3], (xm, ym))
        screen.blit(cavallo_rosso[anima // 3], (xr, yr))
        anima+=1

    pygame.display.update()
def partenza():

    screen.blit(sfondo, (0, 0))
    screen.blit(clicca_un,(340,110))
    screen.blit(c_rosso,(xr,yr))
    screen.blit(c_marrone,(xm,ym))
    screen.blit(c_nero,(xn,yn))
    screen.blit(c_bianco, (xb, yb))
    aggiorna()

def fine_gara():


    screen.blit(c_rosso, (xr, yr))
    screen.blit(c_marrone, (xm, ym))
    screen.blit(c_nero, (xn, yn))
    screen.blit(c_bianco, (xb, yb))
    aggiorna()


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

start=False
#menu
while not start:
    aggiorna()
    screen.blit(menu, (0, 0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start=True


#game_loop
partita_iniziata=False

while start:

    aggiorna()
    animazioni()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            partita_iniziata=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                start=False
    if not partita_iniziata:
        partenza()

    if partita_iniziata:
        xb += random.randrange(1, 20)
        xn += random.randrange(1, 20)
        xm += random.randrange(1, 20)
        xr += random.randrange(1, 20)


    if xb > 820:
        screen.blit(vincitore_b,(340,110))
        partita_iniziata = False
    elif xn>820:
        screen.blit(vincitore_n,(340,110))
        partita_iniziata = False
    elif xm>820:
        partita_iniziata = False
        screen.blit(vincitore_m, (340, 110))
    elif xr>820:
        screen.blit(vincitore_r,(340,110))
        partita_iniziata = False

        fine_gara()










#NERO = (0, 0, 0)
#BIANCO = (255, 255, 255)
#ROSSO = (255, 0, 0)
#VERDE = (0, 255, 0)
#BLUE = (0, 0, 255)
