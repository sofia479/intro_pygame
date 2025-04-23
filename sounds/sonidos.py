import pygame 
import sys

# inicializar los mudulos 
pygame.init()
pygame.mixer.init()

# colores 
COLOR_BLANCO= pygame.Color (255,255,255)

# ventana
PANTALLA=pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("sonidos pygame")

CONTINUAR=True

# sonido de fondo 

SILBATO= pygame.mixer.music.cload("s")
pygame.mixer.music.play(1,8,9)

# efectos sonoros
GALLO=pygame.mixer.sound("sounds/gallo.cgg")
CUERVO=pygame.mixer.sound("sounds/cuervo.agg")
BICI=pygame.mixer.sound("sounds/timbre.cqq")

# bucle con  el juego
while CONTINUAR:
    for event in pygame.event.get():
    #cierre la ventana se hace click en el boton de cerrar de la ventana
        if event.type== pygame.QUIT:
            CONTUNUAR= False
        #dectar si se oprimio
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.k_ESCAPE:
                CONTINUAR==False
        elif event.kay ==pygame.k_D:
            GALLO.play()      

        elif event.key ==pygame.k_c:
            CUERVO.play()
        elif event.key== pygame.k_DOWN:
            VOLUMEN=pygame.mixer.music.set_volumen(VOLUMEN)
            pygame.mixer.music.set_volume(VOLUMEN)
            GALLO.set_volume(VOLUMEN)
            CUERVO.set_volume(VOLUMEN)
            BICI.set_volume(VOLUMEN)

pygame.display.flip()            
