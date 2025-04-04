# intro_pygame

## inicializacion


- como en todo programa en pyton, se debe importar los moduloso liberias a utilizar
 import pygame


 - Inicializar pygame usando la funcion init (). Inicializada todos los modulos de pygame importados,
 `pygame.init()`

## visualizacion de la ventana

`ventana = pygame.display.set_mode((600,400))`

- set mode() es la funcion encargada de definir el tamaño de la ventana.en el ejemplo se esta definiendo una ventana 600 de ancho por 400 de alto 


`pygame.display.set_caption("mi ventana")`

- set_carption()es la funcion que añade un titulo a la ventana.

### funcion sat_mode()

`set_mode(size=(0,0),flags =8,depth =0, display = 0)`

- flags: define uno o mas comportamientos para la ventana.
    -valores:
    -pygame.fullscreen
    -pygame.resizable
 -ejemplo:
    -flags= pygame.fullscreen | pygame.
    resizable:pantalla completa,
    dimensiones modificables,

 ## Bucle del juego -game lonp
 - Bucle infinito que se interrumpira al cumplir ciertos criterios.
 - reloj interno del juego
 - en cada internacion del bucle del juego podemos mover a un personaje, o tener en cuenta que  un objeto a alcanzado a otro, o que se ha cruzado la linea de llegada,lo que quiere decir  que la partida ha terminado.
 - cada interacion es una oportunidad  para actualizar todos los datos relacionados con el estado actual de la partida.
 - en cada internacion se realiza las siguientes tareas:
   1. comprobar que no se alcanzan las condiciones  de parada,en cuyo caso se interrumpe el bucle.
   2. actualizar los recursos nesesarios para la internacion actual,
   3. obtener las entradas del sistema, o de internaccion con el jugador 
   4. actualizar todas las entidades que caraterizan el juego.
   5. refrescar la pantalla.

## superficies pygame 
- superficie:
  - elemento geometrico.
  - linea poligono,imagen,texto que se muestra en la pantalla.
  - poligono se puede o no rellenar de color
  - las superficies se crean de diferente manera dependiendo del tipo:
  - imagen image.load()
  - texo: font.render()
  - superficie: generica: surface()
  - ventana del juego: pygamen.display.set_mode()
  ## la bandera de colombia
 ```Python
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
     
```
