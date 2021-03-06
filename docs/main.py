
#!/usr/bin/env Python3  
import os 
import time  
import pygame
import PySimpleGUI as sg
from ball import Ball
from player import Player,Machine

def return_points(p1,p2,who_win):
    """
       Retorna los puntajes actualizados en una lista [puntos_j1,puntos_j2]
    """
    if who_win is 1: #Si gana el jugador 1
        return [p1 + 1,p2] #A los puntos del j1 le sumo 1
    return [p1,p2 + 1] #Si gana el jugador 2, a los puntos del j2 le sumo 1
       
def draw_elements(screen,ball,player,player2,middle_rect,direction,text_points_j1,text_points_j2):
    """
        Esta función dibuja los elementos en pantalla
    """
    ball.draw() #Dibujo la pelota
    player.draw(screen) #Dibujo el jugador
    player2.draw(direction,screen) #El draw de la máquina evalúa para dónde moverse y dibuja al jugador
               
    ball.move() #Mueve la pelota, no la dibuja. Crea un nuevo rectangulo con las posiciones actualzadas
      
    pygame.draw.rect(screen,[255,255,255],middle_rect) #Dibuja el rectangulo del medio que separa los lados
    screen.blit(text_points_j1,((screen.get_width() / 2 - 100),20)) #Dibujo en la pantalla el texto de puntos del jugador 1
    screen.blit(text_points_j2,((screen.get_width() / 2 + 100),20)) #Dibujo en la pantalla el texto de puntos del jugador 2



def main():
    #------------------------------- Inicializo pygame ----------------------------------------#
    pygame.init() 
    pygame.font.init()
    pygame.display.set_caption('Pong')
    captured_event = None 
    screen = pygame.display.set_mode((600,450))
    

    middle_rect = pygame.Rect(300,0,10,450) #Es el rectangulo del medio que separa los lados
    font_text = pygame.font.SysFont('arial',30)
    #------------------------------------------------------------------------------------------#

    #---------------------------------Defino las cosas necesarias para los textos de los puntos ----------------------------#
    points_j1 = 0 #Puntos jugador 1
    points_j2 = 0 #Puntos jugador_2
    text_points_j1 = font_text.render(str(points_j1),True,[255,255,255],[0,0,0]) #Se renderiza el texto de puntos del j1
    text_points_j2 = font_text.render(str(points_j2),True,[255,255,255],[0,0,0]) #Se renderiza el texto de puntos del j2   
    #------------------------------------------------------------------------------------------------------------------------#
   
    while points_j1 != 10 or points_j2 != 10: #Mientra nadie llegue a los 10 puntos
        try:
            #----------------INSTANCIO LOS OBJETOS DEL JUEGO ----------------------------------#
            player = Player(5,200,10)
            player2 = Machine(580,200,6.5)
            ball = Ball(screen)
            continue_playing = (0,0) #Continue_playing es 0 si nadie pierde. Será 1 si gana el J1, 2 si gana el J2
            #Como lo cambié, la tupla es en la posicion 0 quien gana, y la posicion 1 si la pelota sobre el eje Y va positiva o negativamente
            
            
            #----------------------------------------------------------------------------------#
            while continue_playing[0] == 0: #Mientras nadie haya perdido

                screen.fill((0,0,0)) #Dibujo el fondo de color negro

                #------------------------ Capturo los eventos de la pantalla -----------------------------#
                for event in pygame.event.get():
                    captured_event = event.type
                if event.type == 12:
                    pygame.quit() 
                    break 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.move_up()
                    elif event.key == pygame.K_DOWN:
                        player.move_down(screen) #Manda como parametro screen para usar el screen.get_height   
                # -----------------------------------------------------------------------------------------#
            
                continue_playing = ball.evaluate_collition(player.get_tops()[0],player.get_tops()[1],player2.get_tops()[0],player2.get_tops()[1]) 
                #Evalua las colisiones de la pelota con los dos jugadores. 
                #Retorna la tupla [quien_gana,direccion_pelota]
                #Si hubo colision, cambia la direccion de la pelota. Retorna 0 si todavia no pierde nadie.
                #Retorna 1 si gana el jugador 1, retorna 2 si gana el jugador 2
                
                
                #---------------------------DIBUJA LOS ELEMENTOS EN PANTALLA-------------------------------------------#
                draw_elements(screen,ball,player,player2,middle_rect,continue_playing[1],text_points_j1,text_points_j2)
                #------------------------------------------------------------------------------------------------------#
                
                pygame.display.flip() #Actualizo      
                time.sleep(0.04) #Actualiza cada 0.05 milesimas

            #---------------------- UNA VEZ QUE ALGUIEN PIERDE ---------------------------------------------------------------------#
        
            #----------------------------Actualizo la puntuacion -------------------------------------------------------------------#
            points = return_points(points_j1,points_j2,continue_playing[0]) #Guardo los puntajes actualizados
            points_j1 = points[0] #points[0] tiene guardado los puntos del jugador 1
            points_j2 = points[1] #points[1] tiene guaardado los puntos del jugador 2

            text_points_j1 = font_text.render(str(points_j1),True,[255,255,255],[0,0,0]) #Se renderiza el texto de puntos del j1
            text_points_j2 = font_text.render(str(points_j2),True,[255,255,255],[0,0,0]) #Se renderiza el texto de puntos del j2
        except pygame.error:
            break #Si cierra la pantalla, se levanta esta excepcion. Corto el primer while
        #-----------------------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    main()
    










