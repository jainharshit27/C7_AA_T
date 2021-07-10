import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((450,300))

b1 = pygame.Rect(50,100,50,50)
b2 = pygame.Rect(150,100,50,50)
b3 = pygame.Rect(250,100,50,50)
b4 = pygame.Rect(350,100,50,50)


while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen,(0,0,0),b1)
    pygame.draw.rect(screen,(0,0,0),b2)
    pygame.draw.rect(screen,(0,0,0),b3)
    pygame.draw.rect(screen,(0,0,0),b4)
    
    pygame.display.update()