import pygame
import numpy as np
from serpent import Serpent
import random


class Game: 
    def __init__(self,taille = 20, taille_carre = 30, color_carre = (255,255,255), nb_apple = 10):
        """create the game

        Args:
            taille (int, optional): taille de la fenetre (en nombre de carre). Defaults to 20.
            taille_carre (int, optional): taille du carré (en px). Defaults to 30.
            color_carre (tuple, optional): color . Defaults to (255,255,255) white.
            nb_apple (int, optional): [nombre de pomme sur l'ecran]. Defaults to 5.
        """
        self.taille = taille
        self.taille_carre = taille_carre
        self.color_carre = color_carre
        self.colors = {
            "white" : (255,255,255),
            "green" : (142, 254, 29),
            "red" : (221, 15, 5)
        }

        self.wind = pygame.display.set_mode((self.taille* self.taille_carre+4, self.taille * self.taille_carre+4))
        self.create_zone()
        self.array = self.create_grid_array()
        self.serpent = Serpent(self)
        self.serpent.spawn()
        self.restart = False
        self.point = 0 
        for i in range(nb_apple):
            self.create_apple()


    
        

    def create_zone(self):
        #self.wind.fill((255,255,255))
        for x in range(4,self.taille*self.taille_carre+4, self.taille_carre):
            for y in range (4,self.taille*self.taille_carre+4, self.taille_carre):

                Rect = pygame.Rect((x,y),(self.taille_carre -4,self.taille_carre-4))
                pygame.draw.rect(self.wind, self.color_carre, Rect)
        
               # print("rect created")

    def change_square_color(self, x, y , color):
        x *= self.taille_carre
        x+=4
        y *= self.taille_carre
        y+=4
        color = self.colors[color]
        Rect = pygame.Rect((x,y),(self.taille_carre -4,self.taille_carre-4))
        pygame.draw.rect(self.wind, color, Rect)

    def create_grid_array(self):
        array = np.tile("white", [self.taille, self.taille])
        return array

    def create_apple(self):
        rand_x = random.randint(0,self.taille-1)
        rand_y = random.randint(0,self.taille-1)
        if self.array[rand_x, rand_y] == "white":
            self.array[rand_x, rand_y] = "red"
            self.change_square_color(rand_x,rand_y,"red")
        else: 
            self.create_apple()


        
        #print (array)
    def game_restart(self):
        self.restart = True



if __name__ == "__main__":
    game = Game()
    game.create_grid_array()




        

