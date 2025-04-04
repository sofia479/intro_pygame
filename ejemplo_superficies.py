# importamos la libreria pygame

import pygame
import random

rojo = random.randint(0,255)
azul = random.randint(0,255) 
verde= random.randint(0,255)



# inicializamos los modulos de pygame

pygame.init()

# establecer titulo a la ventana 

pygame.display.set_caption("superface")

# establescamos las dimenciones de la ventana 
ventana =pygame.display.set_mode((400,400))

# definimos un color 

#creamos  una superficie
color_aleatorio_superficie=pygame.Surface((400,400))


# rellenos la sueperficie azul
color_aleatorio_superficie.fill(azul)


# inserto o muevo la superficie en la ventana 
ventana.blit(color_aleatorio_superficie,(100,100))


# actualizacion lavisualizacion de la ventana
pygame.display.flip() 

#bucle del juego

while True:
     event=pygame.event.wait()
     if event.type == pygame.QUIT:
       break
     

