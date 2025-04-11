import pygame
import sys
import random

azul=(0,0,255) 
rojo=(255,0,0)
amarillo=(255,255,0)
verde=(0,255,0)

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("los cuadrados que rebotan")

clock = pygame.time.Clock()
 
XX = 300
MOVIMIENTO =3
YY = 300
MOVIMIENTO =3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul) 

    XX = XX + MOVIMIENTO
    YY = YY + MOVIMIENTO
    

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3
    if YY >= 450:
        YY = 450
        MOVIMIENTO = -3
    elif YY <= 0:
        YY = 0
        MOVIMIENTO = 3
    
    pygame.draw.rect(ventana,rojo ,(XX,00,50,50)) 
    pygame.draw.rect(ventana,rojo ,(XX,450,50,50)) 
    pygame.draw.rect(ventana, amarillo,(00,YY ,50, 50))
    pygame.draw.rect(ventana,verde,(450,YY,50,50))
    pygame.display.flip() 
    color_aleatorio=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
    pygame.draw.rect(ventana,color_aleatorio,(200,200,100,100))
    pygame.display.flip()


    