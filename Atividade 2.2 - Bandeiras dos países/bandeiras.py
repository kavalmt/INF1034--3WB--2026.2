from turtle import *
from time import sleep

t = Turtle()
t.speed(0)

#Site: ColorZilla Extensão

#2 bandeiras fáceis
#Japão
#Irlanda


#6 bandeiras médias 
# Botswana
# Costa Rica
# Chile
# Panama
# Cuba
# Siria

#2 difíceis
# Georgia
# Grécia

# DESAFIO
# Cambodia

# Cada bandeira intervalo #
# sleep(3)
# t.clear()


#JAPÃO 
t.pu()
t.goto(-125, 100)
t.pd()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(200)
    t.right(90)

t.pu()
t.goto(0, -60)
t.pd()
t.fillcolor("#BC002C")
t.begin_fill()
t.circle(60)
t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#IRLANDA
def partes(x, cor):
    t.pu()
    t.goto(x, 100)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()

    for i in range(2):
        t.forward(83.3)
        t.right(90)
        t.forward(200)
        t.right(90)

    t.end_fill()

partes(-125, "#179B62")
partes(-41.7, "white")
partes(41.6, "#FF883D")

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#BOTSWANA
cores = ["#75AADB", "white", "black", "white", "#75AADB"]
alturas = [66, 22, 24, 22, 66]
y = 100

for i in range(5):
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#COSTA RICA
cores = ["#1F255E", "white", "#CE4652", "white", "#1F255E"]
alturas = [33.3, 33.3, 66.6, 33.3, 33.3]
y = 100

for i in range(5):
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#CHILE
cores = ["white", "#D52B1E"]
alturas = [100, 100]
y = 100

for i in range(2):
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

t.pu()
t.goto(-125, 100)
t.pd()
t.fillcolor("#0039A6")
t.begin_fill()
for i in range(2):
    t.forward(83)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

t.pu()
t.goto(-95, 65)
t.setheading(0)
t.pd()
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#PANAMA
cores = ["white", "#DA121A", "#0033A0", "white"]
xs = [-125, 0, -125, 0]
ys = [100, 100, 0, 0]

for i in range(4):
    t.pu()
    t.goto(xs[i], ys[i])
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(125)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

estrela_cores = ["#0033A0", "#DA121A"]
estrela_xs = [-72, 52]
estrela_ys = [45, -55]

for i in range(2):
    t.pu()
    t.goto(estrela_xs[i], estrela_ys[i])
    t.setheading(0)
    t.pd()
    t.fillcolor(estrela_cores[i])
    t.begin_fill()
    for j in range(5):
        t.forward(18)
        t.right(144)
    t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#CUBA
cores = ["#002A8F", "white", "#002A8F", "white", "#002A8F"]
alturas = [40, 40, 40, 40, 40]
y = 100

for i in range(5):
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

t.pu()
t.goto(-125, 100)
t.pd()
t.fillcolor("#CE1126")
t.begin_fill()
t.goto(-125, -100)
t.goto(-45, 0)
t.goto(-125, 100)
t.end_fill()

t.pu()
t.goto(-105, 8)
t.setheading(0)
t.pd()
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.forward(15)
    t.right(144)
t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#SIRIA
cores = ["#CE1126", "white", "black"]
alturas = [66.6, 66.6, 66.6]
y = 100

for i in range(3):
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cores[i])
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

estrela_xs = [-30, 10]

for i in range(2):
    t.pu()
    t.goto(estrela_xs[i], 10)
    t.setheading(0)
    t.pd()
    t.fillcolor("#007A3D")
    t.begin_fill()
    for j in range(5):
        t.forward(18)
        t.right(144)
    t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#GEORGIA
t.pu()
t.goto(-125, 100)
t.pd()
t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

barras = [(-12.5, 100, 25, 200), (-125, 12.5, 250, 25)]

for x, y, larg, alt in barras:
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor("#FF0000")
    t.begin_fill()
    for j in range(2):
        t.forward(larg)
        t.right(90)
        t.forward(alt)
        t.right(90)
    t.end_fill()

centros = [(-62.5, 50), (62.5, 50), (-62.5, -50), (62.5, -50)]

for cx, cy in centros:
    barrinhas = [(cx-4, cy+15, 8, 30), (cx-15, cy+4, 30, 8)]
    for x, y, larg, alt in barrinhas:
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fillcolor("#FF0000")
        t.begin_fill()
        for j in range(2):
            t.forward(larg)
            t.right(90)
            t.forward(alt)
            t.right(90)
        t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#GRÉCIA
alturas = [200/9] * 9
y = 100

for i in range(9):
    if i % 2 == 0:
        cor = "#0D5EAF"
    else:
        cor = "white"
    t.pu()
    t.goto(-125, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for j in range(2):
        t.forward(250)
        t.right(90)
        t.forward(alturas[i])
        t.right(90)
    t.end_fill()
    y -= alturas[i]

canto = alturas[0] * 5

t.pu()
t.goto(-125, 100)
t.pd()
t.fillcolor("#0D5EAF")
t.begin_fill()
for i in range(2):
    t.forward(canto)
    t.right(90)
    t.forward(canto)
    t.right(90)
t.end_fill()

barras = [(-125 + canto/2 - canto/10, 100, canto/5, canto), (-125, 100 - canto/2 - canto/10, canto, canto/5)]

for x, y, larg, alt in barras:
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for j in range(2):
        t.forward(larg)
        t.right(90)
        t.forward(alt)
        t.right(90)
    t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()

#DESAFIO (bandeira cambodia)
t.pu()
t.goto(-125, 100)
t.pd()
t.fillcolor("#032EA1")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

t.pu()
t.goto(-125, 50)
t.pd()
t.fillcolor("#E00025")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

t.pu()
t.goto(-125, -50)
t.pd()
t.fillcolor("#032EA1")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

esquerda = [(-45, -30), (-45, -15), (-35, -15), (-35, -5),(-25, -5), (-25, 5), (-20, 20), (-15, 5),(-9, 5), (-9, 15), (-5, 25)]

topo = (0, 32)

direita = []
for x, y in reversed(esquerda):
    direita.append((-x, y))

templo = esquerda + [topo] + direita

t.pu()
t.goto(templo[0])
t.pd()
t.fillcolor("#E5E5E5")
t.begin_fill()
for ponto in templo:
    t.goto(ponto)
t.goto(templo[0])
t.end_fill()

#INTERVALO e CENTRALIZAÇÃO
t.pu()
t.goto(0,0)
sleep(2)
t.clear()
t.pd()