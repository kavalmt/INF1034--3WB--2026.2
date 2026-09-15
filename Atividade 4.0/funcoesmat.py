from turtle import *
import math
import time
from random import randint

t = Turtle()
t.speed(0)
escala = 20

def desenha_plano():
    t.color("black")
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()

    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()
    t.setheading(0)

def raiz(x):
    return math.sqrt(x)

def inverso(x):
    return 1 / x

def potencia(x):
    return 2 ** x

def parab1(x):
    return 5 - x ** 2

def parab2(x):
    return x ** 2 - 5 * x + 6

def cubica(x):
    return x ** 3 - x ** 2 - x + 1


def desenha_raiz():
    t.color("blue")
    t.pu()
    t.goto(0, raiz(0) * escala)
    t.pd()
    for i in range(1, 300):
        x = i / 10  
        y = raiz(x)
        t.goto(x * escala, y * escala)

def desenha_inverso():
    t.color("red")
    t.pu()
    t.goto(0.1 * escala, inverso(0.1) * escala)
    t.pd()
    for i in range(2, 300):
        x = i / 10
        y = inverso(x)
        t.goto(x * escala, y * escala)
    t.pu()
    t.goto(-0.1 * escala, inverso(-0.1) * escala)
    t.pd()
    for i in range(2, 300):
        x = -i / 10
        y = inverso(x)
        t.goto(x * escala, y * escala)



def desenha_potencia():
    t.color("green")
    t.pu()
    t.goto(-10 * escala, potencia(-10) * escala)
    t.pd()
    for i in range(-99, 41): 
        x = i / 10
        y = potencia(x)
        t.goto(x * escala, y * escala)

def desenha_parab1():
    t.color("purple")
    t.pu()
    t.goto(-4 * escala, parab1(-4) * escala)
    t.pd()
    for i in range(-39, 41):
        x = i / 10
        y = parab1(x)
        t.goto(x * escala, y * escala)

def desenha_parab2():
    t.color("orange")
    t.pu()
    t.goto(-2 * escala, parab2(-2) * escala)
    t.pd()
    for i in range(-19, 71):
        x = i / 10
        y = parab2(x)
        t.goto(x * escala, y * escala)

def desenha_cubica():
    t.color("brown")
    t.pu()
    t.goto(-2 * escala, cubica(-2) * escala)
    t.pd()
    for i in range(-19, 26):
        x = i / 10
        y = cubica(x)
        t.goto(x * escala, y * escala)

desenha_plano()
desenha_raiz()

time.sleep(2)
t.clear()

desenha_plano()
desenha_inverso()

time.sleep(2)
t.clear()

desenha_plano()
desenha_potencia()

time.sleep(2)
t.clear()

desenha_plano()
desenha_parab1()

time.sleep(2)
t.clear()

desenha_plano()
desenha_parab2()

time.sleep(2)
t.clear()

desenha_plano()
desenha_cubica()

time.sleep(2)
t.clear()


cores = ["red", "blue", "green", "orange", "purple", "black", "brown", "pink"]
def corrida(n):
    tartarugas = []
    for i in range(n):
        nova = Turtle()
        nova.shape("turtle")
        nova.speed(1)
        nova.pu()
        nova.color(cores[i % len(cores)])
        nova.goto(-200, 100 - i * 30)
        tartarugas.append(nova)
    for num in range(60):
        for tartaruga in tartarugas:
            tartaruga.fd(randint(5, 10))
corrida(5)


mainloop()