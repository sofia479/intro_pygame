# bandera_de colombia

import pygame

amarillo = (255,255,0)
azul =(0,0,255)
rojo =(255,0,0)



# ver 

pygame.init()

# establecer titulo de bandera

pygame.display.set_caption("superface")

# establescamos las dimenciones de la ventana 
ventana =pygame.display.set_mode((400,400))

# definir el color de la bandera
color_1aleatorio=()
#creamos  una superficie
amarillo_superficie=pygame.Surface((400,200))
azul_superficie=pygame.Surface((400,100))
rojo_superficie=pygame.Surface((400,100))


# rellenar la superficie
amarillo_superficie.fill(amarillo)
azul_superficie.fill(azul)
rojo_superficie.fill(rojo)

# inserto o muevo la superficie en la ventana 
ventana.blit(amarillo_superficie,(0,0))
ventana.blit(azul_superficie,(0,200))
ventana.blit(rojo_superficie,(0,300))


# actualizacion lavisualizacion de la ventana
pygame.display.flip() 

#bucle del juego

while True:
     event=pygame.event.wait()
     if event.type == pygame.QUIT:
       break
     

