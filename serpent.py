import pygame
import numpy as np
class Serpent:
    def __init__(self,game,taille_depart = 5):  # ne pas changer taille de depart car les modification ne se font pas partout
        self.taille = taille_depart
        self.taille_depart = taille_depart
        self.direction = [0,1]
        self.game = game
        self.tete_x = 10
        self.tete_y = 8
        self.direction_x = 0
        self.direction_y = -1
        self.snake_parts = [[10,12],[10,11],[10,10],[10,9],[10,8]]
        self.eat = False
        self.change_direction = False

    def spawn(self):
        for i in range(8,8+self.taille_depart):
            self.game.change_square_color(10,i,"green")
            self.game.array[10,i] = "green"
        #print(self.game.array)

    def move (self):
        self.game.change_square_color(self.tete_x+self.direction_x , self.tete_y +self.direction_y, "green")

        # change the array
        self.game.array[self.tete_x+self.direction_x , self.tete_y + self.direction_y] = "green"
        self.snake_parts.append([self.tete_x+self.direction_x , self.tete_y + self.direction_y])

        # change position tete
        self.tete_x = self.tete_x+self.direction_x 
        self.tete_y = self.tete_y+self.direction_y 

    def avancer (self):
        
        #print(self.game.array[self.tete_x+self.direction_x , self.tete_y + self.direction_y])
        if not 0 <= self.tete_x+self.direction_x :
            print("sortie de l'ecran")
            self.tete_x = self.game.taille
        elif not self.tete_x+self.direction_x < self.game.taille:
            self.tete_x = -1
        elif not 0 <= self.tete_y+self.direction_y :
            self.tete_y = self.game.taille
        elif not self.tete_y+self.direction_y < self.game.taille:
            self.tete_y = -1

        
        if self.game.array[self.tete_x+self.direction_x , self.tete_y + self.direction_y] == "white":  # verifie si en face de lui s'il n'y a pas d'obstacle
            self.move()

            self.eat = False
        else:
            #print("probleme")
            #print(self.game.array)
            if self.game.array[self.tete_x+self.direction_x , self.tete_y + self.direction_y] == "red":
                print("color_red")
                self.move()
                
                
                # dire qu'il a manger 
                self.eat = True
                self.game.point += 1
                print(self.game.point)
                self.game.create_apple()
            elif self.game.array[self.tete_x+self.direction_x , self.tete_y + self.direction_y] == "green":
                print("color_green")
                self.mourrir()
            else:
                print("c'est pas possible")
                print(self.game.array)
            

        if not self.eat:
            self.game.change_square_color(self.snake_parts[0][0],self.snake_parts[0][1], "white")  # delete the last square 
            self.game.array[self.snake_parts[0][0],self.snake_parts[0][1]] = "white"
            self.snake_parts.pop(0)

        self.change_direction = False

    def tourner (self,x,y):
        if not self.change_direction:
            if x != 0 and self.direction_x == 0:
                self.direction_x = x
                self.direction_y = y
                self.change_direction = True
            elif y !=0 and self.direction_y == 0:
                self.direction_x = x
                self.direction_y = y
                self.change_direction = True
            else:
                print("vous ne pouvez pas faire demi tour directement")
        

    # def manger(self):
    #     pass

    def mourrir(self):
        self.game.game_restart()

