from turtle import *

t = Turtle()
t.speed(0)

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

t.pu()
t.goto(200,150)

#primeiro quadrante
t.pd()
t.rt(90)

#COR ESPIRAL
var_color = textinput("Escolha a cor", "Digite a cor do contorno do espiral ")
t.color(var_color)

#ESPIRAL
tamanho = 100
for i in range(10):
    t.circle(tamanho,180)
    tamanho = tamanho - 10

#segundo quadrante
t.pu()
t.goto(-300,200)
t.pd()

#COR TRIANGULO 
var_color2 = textinput("Escolha a cor", "Digite a cor da proxima forma geometrica")
t.fillcolor(var_color2)
t.color(var_color2)
t.begin_fill()

#TRIANGULO

for i in range(3):
    t.fd(150)
    t.lt(120)

t.end_fill()

#3 QUADRANTE 
t.pu()
t.goto(-150,-200)
t.pd()

# COR LOSANGO
var_color3 = textinput("Escolha a cor", "Digite a cor da proxima forma geometrica")
t.fillcolor(var_color3)
t.color(var_color3)
t.begin_fill()

#LOSANGO 

t.lt(180)

for i in range(2):
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(120)

t.end_fill()

#QUARTO QUADRANTE 
t.pu()
t.goto(300,-200)
t.pd()

#COR HEXAGONO 
var_color4 = textinput("Escolha a cor", "Digite a cor da proxima forma geometrica")
t.fillcolor(var_color4)
t.color(var_color4)
t.begin_fill()

#HEXAGONO

t.pu()
t.goto(250,-200)
t.pd()

for i in range(6):
    t.fd(100)
    t.rt(60)

t.end_fill()
mainloop()


