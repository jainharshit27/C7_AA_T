import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((450,300))

img0 = pygame.image.load("objects/0.png")
img1 = pygame.image.load("objects/1.png")
img2 = pygame.image.load("objects/2.png")
img3 = pygame.image.load("objects/3.png")

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
    
    screen.blit(img0, b1)
    screen.blit(img1, b2)
    screen.blit(img2, b3)
    screen.blit(img3, b4)
    
    pygame.display.update()
