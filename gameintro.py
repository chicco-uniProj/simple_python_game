import pygame
pygame.display.set_caption('Horsin Around')
screen = pygame.display.set_mode((1080, 620))
clock = pygame.time.Clock()
FPS=60
area=pygame.Rect(700,500,800,600)

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

menu=pygame.image.load('menu1.png')

while True:
    aggiorna()
    screen.blit(menu, (0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


        if event.type==pygame.mouse.get_pressed():
            if area.collidepoint(event.pos,):
                print('Area clicked.')




