
#!/usr/bin/env Python3     
import pygame
import PySimpleGUI as sg

class Player:
    def __init__(self,x,y):
        self.__x_position = x
        self.__y_position = y
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
        if self.__top_y > 0:
            self.__top_y -= 10 #Acutalizo el limite de arriba del rectangulo
            self.__y_limit -= 10 #Actualizo el limite de abajo del rectangulo
            self.__y_position -= 10 #Decrementa la posicion para bajar
            self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,100)  #Crea un nuevo rectangulo con las posiciones actualizadas


    def move_down(self,screen):
        """
           Mueve al rectangulo para abajo. Recibe screen para saber la altura del screen con screen.get_height()
        """
        if self.__y_limit < screen.get_height():
            self.__top_y += 10 #Acutalizo el limite de arriba del rectangulo
            self.__y_limit += 10 #Acutalizo el limite de abajo del rectangulo
            self.__y_position += 10 #Incrementa la posicion para bajar
            self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,100) #Crea un nuevo rectangulo con las posiciones actualizadas

    def collide(self,x_ball,y_ball):
        pass

    def draw(self,screen):
       pygame.draw.rect(screen,[255,255,255],self.__rect)

class PlayerJ1(Player):

    def __init__(self,x,y):
        super().__init__(x,y) #Llamo al constructor del padre 



