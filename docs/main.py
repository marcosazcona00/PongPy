
#!/usr/bin/env Python3  
import os 
import time  
import pygame
import PySimpleGUI as sg
from ball import Ball
from player import PlayerJ1

def main():
    #------ Inicializo pygame ----------#
    pygame.init() 
    captured_event = None 
    screen = pygame.display.set_mode((600,450))
    middle_rect = pygame.Rect(300,0,10,450) #Es el rectangulo del medio que separa los lados
    
    player = PlayerJ1(5,200) #Crea al player
    player2 = PlayerJ1(580,200) #Crea al player 2
    ball = Ball(screen) #Crea a la pelota
    continue_playing = 0

    while continue_playing == 0:

        screen.fill((0,0,0)) #Dibujo el fondo

	#----- Capturo los eventos de la pantalla ------#
        for event in pygame.event.get():
            captured_event = event.type
        if event.type == 12:
            pygame.quit()
            break 
        elif event.type == pygame.KEYDOWN:
            os.system('clear')
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down(screen) #Manda como parametro screen para usar el screen.get_height()
            elif event.key == pygame.K_LEFT:
                player2.move_up()
            elif event.key == pygame.K_RIGHT:
                player2.move_down(screen)
            print('X {} Y {}'.format(player.get_position()[0],player.get_position()[1])) 

        # ---------------------------------------------#
      
        continue_playing = ball.evaluate_collition(player.get_tops()[0],player.get_tops()[1],player2.get_tops()[0],player2.get_tops()[1]) #Evalua las colisiones de la pelota con los dos jugadores. Si hubo colision, cambia la direccion de la pelota
        
        #---------DIBUJA LOS ELEMENTOS EN PANTALLA---------#
        pygame.draw.rect(screen,[255,255,255],middle_rect) #Dibuja el rectangulo del medio que separa los lados
        ball.draw() 
        player.draw(screen)
        player2.draw(screen)
        #--------------------------------------------------#
        
        pygame.display.flip()         
        time.sleep(0.06) #Actualiza cada 0.03 milesimas

        #Una vez que actualiza, hago que la pelota se mueva
        ball.move() #Mueve la pelota, no la dibuja. Crea un nuevo rectangulo con las posiciones actualzadas

    print('GANA J{}'.format(continue_playing))
if __name__ == '__main__':
    main()
    





