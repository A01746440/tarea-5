#encoding: UFT-8
#David Arnaiz
#Realizamos varios dibujos

import pygame

import math

import random


Ancho = 800
Alto = 800   #dimensiones de la pantalla

Blanco = (255,255,255)
Negro = (0,0,0) #colores  R,G,B

def Dibujarespiral():

    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto)) #ventana de dibujo
    reloj = pygame.time.Clock()  #limita los fps
    termina = False

    while not termina
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco) #borrar

        for a in range(0,400,10):

            pygame.draw.line(ventana,Negro,(Ancho-a,Alto-a),(0+a,Alto-a),1) #lineas horizontales abajo

            pygame.draw.line(ventana,Negro,(0+a,Alto-a),(0+a,10+a)) #verticales

            pygame.draw.line(ventana,Negro,(0+a,10+a),(Ancho -(a+10), 10 + a),1)  # horizontales arriba

            pygame.draw.line(ventana,Negro,(Ancho- a,Alto-a), (Ancho-a, 10 + a-10),1)  # verticales

        pygame.display.flip()  #actualiza los trazos
        reloj.tick(30)         # 40fps

    pygame.quit() #termina pygame

def DibujarParabola():
    pygame.init()  #inicia
    ventana = pygame.display.set_mode((Ancho,Alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(Blanco)

        RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))  #cambio de color

        for p in range(0,400,10):
            RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255)

            pygame.draw.line(ventana,RANDOM,(Ancho // 2 + p , Alto // 2), (Alto // 2, p), 1)# cuadrante 1

            pygame.draw.line(ventana,RANDOM,(Ancho // 2 - p, Alto - p),(Alto // 2), 1) # 2

            pygame.draw.line(ventana,RANDOM,(Ancho // 2, Alto -p), (Ancho // 2 - p, Alto//2 ), 1)  # 3

            pygame.draw.line(ventana,RANDOM,(Ancho // 2, Alto - p), (Ancho // 2+p, Alto //2), 1) #4

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

def Dibujarcirculosentrelazados():
    pygame.init()  # Inicia
    ventana = pygame.display.set_mode((ANCHO, ALTO))  
    reloj = pygame.time.Clock()  
    termina = False  

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        
        ventana.fill(BLANCO)

        # Dibujar patrón de círculos.
        for r in range(1, 13,
                       1):  # El ángulo máximo es 330. 360 ya está contado en el (0,0). Queremos 12 círculos: 360/11= 32.72
            pygame.draw.circle(ventana, NEGRO, (
            int((math.cos(r * math.pi / 6) * 150) + ANCHO // 2), int((math.sin(r * math.pi / 6) * 150) + ALTO // 2)),
                               (150), 1)
            # Se multiplica por pi con el fin de pasar los radianes a grados

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps

    pygame.quit()  # termina pygame


def dibujarCirculoCuadrado():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((Ancho, Alto))  
    reloj = pygame.time.Clock()  
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(Blanco)

        for y in range(1, 400, 10):
            # DibujarCírculo
            pygame.draw.circle(ventana, Negro, (Ancho // 2, Alto // 2), y, 1)
            # DibujarCuadrado
            pygame.draw.rect(ventana, Negro, (y, y, Ancho - y * 2, Alto - y * 2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps

    pygame.quit()  # termina pygame


def imprimirPiramide():
    # Para columna del 8:
    incremento = 1
    for x in range(1, 10, 1):
        resultado = incremento * 8 + x  # Primer resultado.
        print(incremento, "* 8 +", x, "=", resultado)  # Imprime el primer resultado.

        incremento = (incremento * 10) + (x + 1)  # El valor del incremento cambia. Multiplicando la variable inicial X10 y sumando el facto más x para agregar el valor pasado.
    print("---------------------------------")

    # Para columna del 8:
    incremento2 = 1

    for y in range(1, 10, 1):
        resultado2 = incremento2 * incremento2  # Primer resultado.
        print(incremento2, "*", incremento2, "=", resultado2)  # Imprime el primer resultado.

        incremento2 = (incremento2 * 10) + (1)  

def calcularNumerosDivisibles():
    d = 0
    for x in range(1000, 10000, 1):  

        if x % 29 == 0:
            d += 1

    return d


def aproximarPI(valor):
    incremento = 0  # Contador

    for x in range(1, valor + 1):
        incremento = incremento + (1 / x ** 2)  

    pi = (incremento * 6) ** (1 / 2)

    return pi


def main():
    print("Tarea 5. Seleccione qué quiere hacer:")

    print("""
       1. Dibujar cuadros y círculos
       2. Dibujar espiral
       3. Dibujar círculos
       4. Dibujar parábolas
       5. Aproximar PI
       6. Contar divisibles entre 29
       7. Imprimir pirámides de números
       0. Salir""")

    print("")
    seleccion = int(input("¿Qué desea hacer?:"))
    print("---------------------------------")

    while seleccion >= 0:
        if seleccion == 1:
            dibujarCirculoCuadrado()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 2:
            dibujarEspiral()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 3:
            dibujarCirculosEntrelazados()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 4:
            dibujarParabola()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 7:
            imprimirPiramide()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 6:
            print("Número de divisibles entre 29 es:", calcularNumerosDivisibles())
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 5:
            pi = int(input("Ingresa el rango de pi:"))
            print("PI vale:", aproximarPI(pi))
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion >= 8:
            print("Selecciones un número del 1 al 7.")
            print("")
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 0:
            print("¡Hasta luego!")
            break


main()