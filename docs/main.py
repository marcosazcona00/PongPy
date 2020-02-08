
#!/usr/bin/env Python3  
import os 
import time  
import pygame
import PySimpleGUI as sg
from player import PlayerJ1

def main():
    #------ Inicializo pygame ----------#
    pygame.init() 
    captured_event = None 
    screen = pygame.display.set_mode((600,450))
    middle_rect = pygame.Rect(300,0,10,450) #Es el rectangulo del medio que separa los lados
    #-----------------------------------#
    
    player = PlayerJ1() #Crea al player
    print('X {} Y {}'.format(player.get_position()[0],player.get_position()[1])) 
    print('TOP ARRIBA {} TOPE ABAJO {}'.format(player.get_tops()[0],player.get_tops()[1])) 

    while True:

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
            print('X {} Y {}'.format(player.get_position()[0],player.get_position()[1])) 
            print('TOP ARRIBA {} TOPE ABAJO {}'.format(player.get_tops()[0],player.get_tops()[1])) 

        # ---------------------------------------------#

        pygame.draw.rect(screen,[255,255,255],middle_rect) #Dibuja el rectangulo del medio que separa los lados
        player.draw(screen)
        pygame.display.flip()         
        time.sleep(0.06) #Actualiza cada 0.03 milesimas


if __name__ == '__main__':
    main()
    




