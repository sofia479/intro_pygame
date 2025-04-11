import pygame
import sys
import random
import math
color_ventana = (255, 255, 255)
negro = (0, 0, 0)
azul1=(51, 164, 255)
amarillo2=(253, 255, 51)
cafe3=(255, 183, 51)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)


PI= math.pi

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("lineas aleatorias")

clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(rosado)
    fuente_area = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_area.render("Colegio Guanenta", 1, blanco)
    ventana.blit(texto, (100, 0))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("esp. sistemas", 1, blanco)
    ventana.blit(texto, (150, 30))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("sofia galvis", 1, rojo)
    ventana.blit(texto, (0, 475))

    #rectangulo (bordes de la imagen)
    pygame.draw.rect(ventana, negro, ((50, 100), (400, 340)), 1)
    #tren
    pygame.draw.rect(ventana, verde, (150,280, 270,100))
    pygame.draw.rect(ventana, azul1, (300, 200, 90,80))
    pygame.draw.rect(ventana, negro, (270, 150, 150,50))
    pygame.draw.rect(ventana, negro, (300, 130, 90,30))
    pygame.draw.rect(ventana, cafe3, (320, 210, 50,50))
    pygame.draw.circle(ventana,rojo,(150,330),50,100)
    pygame.draw.rect(ventana,amarillo2,(130,280,20,100))
    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("tren", 1, negro)
    ventana.blit(texto, (170,300))
    #ruedas
    pygame.draw.circle(ventana, naranja , (180,400),35,60)
    pygame.draw.circle(ventana, naranja, (390,400),35,70)
    pygame.draw.circle(ventana, naranja , (320,400),35,70)
    pygame.draw.circle(ventana, naranja , (250,400),35,60)
    #cara
    
    pygame.draw.rect(ventana, verde, (320, 190, 50,50))
    pygame.draw.rect (ventana, negro, (320, 210, 50,50))

    # Personita
    pygame.draw.circle(ventana, naranja, (380, 90), 35, 0)D

    # Ojos
    pygame.draw.circle(ventana,naranja, (365, 80), 12, 0)
    pygame.draw.circle(ventana, verde, (395, 80), 12, 0)

    # Pupilas
    pygame.draw.circle(ventana, verde, (365, 80), 6, 0)
    pygame.draw.circle(ventana, verde, (395, 80), 6, 0)

    # Boca
    pygame.draw.circle(ventana, negro, (380, 106), 9, 0)

    # Cejas
    pygame.draw.line(ventana, negro, (360, 60), (370, 70), 3)
    pygame.draw.line(ventana, negro, (390, 70), (400, 60), 3)

    pygame.display.flip()




    



 

