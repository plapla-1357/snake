import pygame
from game import Game
import time

pygame.init()

pygame.display.set_caption("snake")

game = Game()
#game.change_square_color(0,0,"red")

running = True
#print(time.time())
time_start = time.time()
coldown = 0.125

myfont = pygame.font.SysFont("monospace", 30)

while running:
    # render text
    label = myfont.render(str(game.point), True, (30, 30, 30), (255, 255, 255))
    game.wind.blit(label, (0, 0))

    if game.restart == False:
        pygame.display.update() # mettre a jour les modification faite sur le fenetre
        if time_start + coldown < time.time():
            game.serpent.avancer()
            time_start = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print(time.time())
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:   # fleche gauche
                    game.serpent.tourner(-1,0)
                elif event.key == pygame.K_RIGHT:# fleche droite
                    game.serpent.tourner(1,0)
                elif event.key == pygame.K_UP:  # fleche haut
                    game.serpent.tourner(0,-1)
                elif event.key == pygame.K_DOWN:    # fleche bas
                    game.serpent.tourner(0,1) 
    
    else:
        print("ok")
        game = Game()
