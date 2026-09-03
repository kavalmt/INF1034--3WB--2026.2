from turtle import *
import random
t = Turtle()
t.speed(0)

#(x,y,tam,cor)

 
#FUNÇÃO PLANO CARTESIANO
def desenha_plano():
    t.pu()
    t.goto(-400,0)
    t.pd()
    t.goto(400,0)
    t.stamp()
    t.pu()
    t.goto(0,400)
    t.lt(90)
    t.stamp()
    t.pd()
    t.goto(0,-400)
 
#FUNÇÃO RANDOM POR QUADRANTE
def func_random(quadrante, tam):
    if quadrante == 1:
        x = random.randint(20+tam, 400-tam)
        y = random.randint(20+tam, 400-tam)
    elif quadrante == 2:
        x = random.randint(-400+tam, -20-tam)
        y = random.randint(20+tam, 400-tam)
    elif quadrante == 3:
        x = random.randint(-400+tam, -20-tam)
        y = random.randint(-400+tam, -20-tam)
    elif quadrante == 4:
        x = random.randint(20+tam, 400-tam)
        y = random.randint(-400+tam, -20-tam)
    return x, y
 
#FUNÇÃO COR
def cor_forma():
    cor = textinput("Escolha a cor", "Digite a cor da proxima forma geometrica")
    return cor
 
#FUNÇÃO ESPIRAL
def desenha_espiral(x, y, tam, cor):
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.color(cor)
    for i in range(10):
        t.circle(tam, 180)
        tam = tam - 10
 
#FUNÇÃO POLIGONO GENERICO (EXTRA)
def desenha_poligono(x, y, lados, tam, cor):
    angulo = 360 / lados
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(lados):
        t.fd(tam)
        t.lt(angulo)
    t.end_fill()
 
#FUNÇÃO QUADRADO
def desenha_quadrado(x, y, lado, cor):
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(4):
        t.fd(lado)
        t.lt(90)
    t.end_fill()
 
#FUNÇÃO TRIANGULO
def desenha_triangulo(x, y, lado, cor):
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(3):
        t.fd(lado)
        t.lt(120)
    t.end_fill()
 
#FUNÇÃO LOSANGO
def desenha_losango(x, y, lado, cor):
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    t.lt(180)
    for cont in range(2):
        t.fd(lado)
        t.rt(60)
        t.fd(lado)
        t.rt(120)
    t.end_fill()
 
#FUNÇÃO HEXAGONO
def desenha_hexagono(x, y, lado, cor):
    t.pu()
    t.seth(0)
    t.goto(x, y)
    t.pd()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(6):
        t.fd(lado)
        t.rt(60)
    t.end_fill()
 
#-------------------------------------------------------------------------------------------------------#
 
desenha_plano()
 
# PRIMEIRO QUADRANTE - ESPIRAL
x, y = func_random(1, 100)
cor = cor_forma()
desenha_espiral(x, y, 100, cor)
 
# SEGUNDO QUADRANTE - TRIANGULO
x, y = func_random(2, 100)
cor = cor_forma()
desenha_triangulo(x, y, 100, cor)
 
# TERCEIRO QUADRANTE - LOSANGO
x, y = func_random(3, 80)
cor = cor_forma()
desenha_losango(x, y, 80, cor)
 
# QUARTO QUADRANTE - HEXAGONO
x, y = func_random(4, 60)
cor = cor_forma()
desenha_hexagono(x, y, 60, cor)
 
# EXTRA pentagono
x, y = func_random(1, 60)
cor = cor_forma()
desenha_poligono(x, y, 5, 60, cor)
 
mainloop()