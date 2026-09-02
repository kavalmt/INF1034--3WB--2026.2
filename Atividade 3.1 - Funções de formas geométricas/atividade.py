from turtle import *
import random
t = Turtle()
t.speed(0)

#(x,y,tam,cor,qtd_lados)

#FUNÇÃO RANDOM LOCAL
def func_random(LimitNX,LimitX,LimitNY,LimitY):
    x = random.randint(LimitNX,LimitX)
    y = random.randint(LimitNY,LimitY) 
    t.pu()
    t.goto(x, y)
    t.pd()

#FUNÇÃO QUADRANTES
def quadrantes(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

#FUNÇÃO COR
def cor_forma():
    var_color4 = textinput("Escolha a cor", "Digite a cor da proxima forma geometrica")
    t.fillcolor(var_color4)
    t.color(var_color4)
    t.begin_fill()
    return

#FUNÇÃO ESPIRAL
def espiral(tamanho):
    for i in range(10):
        t.circle(tamanho,180)
        tamanho = tamanho - 10

#FUNÇÃO TRIANGULO
def triangulo():
    for i in range(3):
        t.fd(150)
        t.lt(120)

#FUNÇÃO LOSANGO
def losango():
    t.lt(180)
    for i in range(2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)

#HEXAGONO
def hexagono():
    t.pu()
    t.goto(250,-200)
    t.pd()
    for i in range(6):
        t.fd(100)
        t.rt(60)

#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

#PLANO CARTESIANO
t.pu()
t.goto(-400,0) # PEGUEI A POSIÇÃO
t.pd() # ABAIXEI A CANETA
t.goto(400,0) #FEZ A LINHA ATE A OUTRA POSIÇÃO 
t.stamp()
t.pu()
t.goto(0,400)
t.lt(90)
t.stamp()
t.pd()
t.goto(0,-400)


# PRIMEIRO QUADRANTE (X = 0 - > 400  ; Y = 0 - > 400 )
quadrantes(200,150)
t.rt(90)


#COR ESPIRAL
cor_forma()
#RANDOM
func_random(100,250,100,200)
#ESPIRAL
print(espiral(100))

#-------------------------------------------------------------------------------------------------------#

# SEGUNDO QUADRANTE (X = -400 - > 0  ; Y = 0 - > 400 )
quadrantes(-300,200)

#COR TRIANGULO 
cor_forma()
#RANDOM
func_random(-350,-200,100,200)
#TRIANGULO
triangulo()

t.end_fill()

#-------------------------------------------------------------------------------------------------------#

# #TERCEIRO QUADRANTE (X = -400 - > 0 ; Y = -400 - > 0)
quadrantes(-150,-200) 

# COR LOSANGO
cor_forma()
#RANDOM
func_random(-350,-200,-400,-100)
#LOSANGO 
losango()

t.end_fill()

#-------------------------------------------------------------------------------------------------------#

# #QUARTO QUADRANTE ( X = 0 - > 400 ; Y = -400 -> 0)
quadrantes(300,-200)

#COR HEXAGONO 
cor_forma()
#RANDOM
func_random(-350,-200,-400,-100)
#HEXAGONO
hexagono()

# t.end_fill()



mainloop()


