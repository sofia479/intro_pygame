import pygame
import sys
import math 

rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
rosado = (255, 192, 203)
negro = (0, 0, 0)
amarllo = (255, 255, 0 )
blanco = (255, 255, 255)
naraja = (255, 165, 0)
cian = (0, 255, 255)
PI = math.pi

pygame.init()

ventana = pygame.display.set_mode((400, 400))

pygame.display.set_caption("dibujar formas con pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

##########################
# bucle pincipal del juego
##########################

while 1:
    clock.tick(40)

    # ciclo para la deteccion del juego
    for event in pygame.event.get():
        # si se hace click sobre boton de cerrar de le ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()
    # actualisa la ventana
    ventana.fill(negro)

    # dibujar formas con el modulo pygame.draw

    # dibujar una linea
    pygame.draw.line(ventana, rojo, (100, 100), (300, 300))
    pygame.draw.line(ventana, rojo, (100, 300), (300, 100))

    # dibujar una linea discontinua
    # True: crea un poligono 
    puntos1 = [(0, 0), (50, 100), (100, 50), (250,200), (400, 400)]
    puntos2 = [(200, 0), (400, 200), (200, 400), (0,200)]
    pygame.draw.lines(ventana, azul, True, puntos1)
    pygame.draw.lines(ventana, rojo, True, puntos2)

    # dibujar un rectangulo
    # rectanqulo relleno, ubicado en la coordenada sup. izq. (200, 200), y de ancho(200, 100) 
    pygame.draw.rect(ventana, rosado, (200, 200, 200, 100))
    # rectangulo sin relleno, esquina sup. izq: (100, 100), esquina inf. der: (150, 200)
    pygame.draw.rect(ventana, verde, ((100, 100), (150, 200)), 1)
    
    # dibujar un poligono
    puntos3 = [(200, 200), (250,300), (300, 325), (400, 350)]
    pygame.draw.polygon(ventana, amarllo, puntos3, 1)

    # dibujar un circulo
    # centro del circulo: (300, 100)
    # radio del circulo: 100
    # grosor del circulo: 1
    pygame.draw.circle(ventana, blanco, (300, 100), 100, 1)

    # dibujar un elipce
    pygame.draw.ellipse(ventana, naraja, (100, 150, 200, 100), 1)

    # arco de circunferencia

    pygame.draw.arc(ventana, cian, (300, 25, 180, 150), PI/2, PI, 1)

    #texto
    # fuente de tipo arial, tamaño 35, negrilla y curciva
    fuente_area = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_area.render("sistema guenenta", 1, blanco)
    ventana.blit(texto, (50, 50))

    # actualisa la visuizacion de la ventana
    pygame.display.flip()

#########################
# fin del bucle del juego
#########################


 