
#!/usr/bin/env Python3   
import random
import pygame 
import PySimpleGUI as sg

class Ball:
    def __init__(self,screen):
        #Recibo screen para saber la altura y ancho
        self.__x_movement = 6 #Defino el movimiento sobre el x. Tambien define la velocidad a la que se mueve sobre el eje x
        self.__y_movement = self.__x_movement #Defino el movimiento sobre y
        self.__screen = screen
        self.__x_position = screen.get_width() / 2 
        self.__y_position = screen.get_height() / 2 
        self.__left_limit = self.__x_position #Define el limite del lado izquierdo del cuadrado
        self.__right_limit = self.__x_position + 20 #Define el limite del lado derecho del cuadrado
        self.__rect = pygame.Rect(self.__x_position, self.__y_position, 20, 20)
    
    def get_position(self):
        """
	        Devuelve los limites de la izquierda y derecha de la pelota
        """
        return [self.__left_limit,self.__right_limit]    

    def move(self):
        self.__x_position -= self.__x_movement #Muevo a la izquierda la pelota
        self.__y_position -= self.__y_movement #Muevo a la derecha la pelota
        self.__left_limit -= self.__x_movement
        self.__right_limit -= self.__x_movement
        self.__rect = pygame.Rect(self.__x_position,self.__y_position,20,20)
	
    def evaluate_collition(self,up_top_p1,down_top_p1,up_top_p2,down_top_p2):
        """
           Este método va a evaluar si colisiona con la pared o con el jugador y cambia la direccion de la pelota. En caso de que se pase de los limites izquierdos o derechos, pierden, por tanto, retorna 1 si pierde J2, y 2 si pierde J1. Si no pierde nadie, retorna 0
        """

        #--------------SE EVALUA SI LA PELOTA SE PASA DE LOS LIMITES IZQUIERDA O DERECHA PARA VER QUIEN PIERDE --------------------------#
        if self.__left_limit == 0 or self.__right_limit >= self.__screen.get_width(): #Si los limites de la pelota tocan los limites de la izquierda o derecha
            if self.__left_limit == 0:
                #Perdio el J1
                return (2,self.__y_movement)
            elif self.__right_limit >= self.__screen.get_width(): 
                #Perdio el J2
                return (1,self.__y_movement)
        #---------------------------------------------------------------------------------------------------------------------------------#

        #-------------EVALUA SI LA PELOTA COLISIONA CON LOS BORDES DE ARRIBA O ABAJO Y CAMBIA LA DIRECCION -------------------------------#
        if self.__y_position <= 0 or self.__y_position > self.__screen.get_height() - 20: #Si colisiona con los bordes de arriba o abajo
            self.__y_movement = self.__y_movement * -1 #Cambia la direccion del eje y para arriba o abajo porque chocó con los bordes
        #---------------------------------------------------------------------------------------------------------------------------------#

        #-------------EVALUA SI LA PELOTA COLISIONA CON ALGUNO DE LOS JUGADORES Y CAMBIA LA DIRECCION DE LA PELOTA -----------------------#
        if (self.__y_position >= up_top_p1 and self.__y_position <= down_top_p1 and self.__x_position <= 20) or (self.__y_position >= up_top_p2 and self.__y_position <= down_top_p2 and self.__x_position >= 560):
                #Esto es, evalua si está entre los topes de arriba o abajo del jugador 1 o 2. Si está en alguno de los topes, evalúa que esté en el mismo X que está el rectangulo
                self.__x_movement = self.__x_movement * -1 #Cambia la direccion del eje x
                if random.randint(0,1) == 1:
                    #Por un random, si da 1, vuelve a cambiar la direccion para arriba o abajo.
                    self.__y_movement = self.__y_movement * -1
        #----------------------------------------------------------------------------------------------------------------------------------#
        
        return (0,self.__y_movement) #Retorna 0 si no pierde nadie


    def draw(self):
        pygame.draw.rect(self.__screen,[250,99,99],self.__rect)

    
