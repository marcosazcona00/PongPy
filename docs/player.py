
#!/usr/bin/env Python3     
import pygame
import PySimpleGUI as sg

class Player:
    def __init__(self):
        self.__x_position = 5
        self.__y_position = 200
        self.__top_y = self.__y_position #Define el tope del rectangulo
        self.__y_limit = self.__y_position + 100 #Define el tope de abajo del rectangulo
        self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,100) #Obtengo el objeto rect
   
    def get_position(self):
        """
           Retorna una lista con la posicion x,y del player
        """  
        return [self.__x_position,self.__y_position]    

    def get_tops(self):
        """
           Retorna una lista con los topes de arriba y abajo del rectangulo
        """
        return [self.__top_y,self.__y_limit]

    def move_up(self):
        """
  	   Mueve al rectangulo para arriba
        """
        self.__top_y -= 10 #Acutalizo el limite de arriba del rectangulo
        self.__y_limit -= 10 #Actualizo el limite de abajo del rectangulo
        self.__y_position -= 10 #Decrementa la posicion para bajar
        self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,100)  #Crea un nuevo rectangulo con las posiciones actualizadas


    def move_down(self):
        """
           Mueve al rectangulo para abajo
        """
        self.__top_y += 10 #Acutalizo el limite de arriba del rectangulo
        self.__y_limit += 10 #Acutalizo el limite de abajo del rectangulo
        self.__y_position += 10 #Incrementa la posicion para bajar
        self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,100) #Crea un nuevo rectangulo con las posiciones actualizadas

    def collide(self,x_ball,y_ball):
        pass

    def draw(self,screen):
        pygame.draw.rect(screen,[255,255,255],self.__rect)

class PlayerJ1(Player):

    def __init__(self):
        super().__init__() #Llamo al constructor del padre 
