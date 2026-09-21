from pygame import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

init()
screen = display.set_mode((1280, 720))
running = True
clock = time.Clock()

fonte = font.Font("fontecoringa.otf", 40)
image = image.load("coringa.png")
image = transform.scale(image, (180, 180))
mixer.music.load("gotham.mp3")
mixer.music.play(-1)

background_color = "#87CEEB"
texto = "Why so serious ?"
sol_x = 130
sol_y = 130
sol_raio = 70
nuvem_x = 420
nuvem_x_inicial = nuvem_x
nuvem_y = 150
nuvem_vel = 60
casa_x = 500
casa_largura = 260
casa_altura = 200
casa_y = 600 - casa_altura  
arvore_x = 980
arvore_tronco_altura = 120
arvore_y = 600 - 60 - arvore_tronco_altura  

while running:
    clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    dt = clock.get_time() / 1000
    nuvem_x = nuvem_x + nuvem_vel * dt
    if nuvem_x > 1280:
        nuvem_x = nuvem_x_inicial
    screen.fill(background_color)
    draw.rect(screen, "#4CAF50", (0, 600, 1280, 120))

    draw.circle(screen, "#FFD93D", (sol_x, sol_y), sol_raio)
    draw.line(screen, "#FFD93D", (sol_x, sol_y - 110), (sol_x, sol_y - 80), 6)
    draw.line(screen, "#FFD93D", (sol_x, sol_y + 110), (sol_x, sol_y + 80), 6)
    draw.line(screen, "#FFD93D", (sol_x - 110, sol_y), (sol_x - 80, sol_y), 6)
    draw.line(screen, "#FFD93D", (sol_x + 110, sol_y), (sol_x + 80, sol_y), 6)
    draw.line(screen, "#FFD93D", (sol_x - 78, sol_y - 78), (sol_x - 56, sol_y - 56), 6)
    draw.line(screen, "#FFD93D", (sol_x + 78, sol_y - 78), (sol_x + 56, sol_y - 56), 6)
    draw.line(screen, "#FFD93D", (sol_x - 78, sol_y + 78), (sol_x - 56, sol_y + 56), 6)
    draw.line(screen, "#FFD93D", (sol_x + 78, sol_y + 78), (sol_x + 56, sol_y + 56), 6)

    draw.circle(screen, "#FFFFFF", (nuvem_x, nuvem_y), 45)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 55, nuvem_y - 15), 55)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 120, nuvem_y), 50)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 175, nuvem_y + 10), 40)
    draw.rect(screen, "#5C3A21", (arvore_x, arvore_y + 60, 30, arvore_tronco_altura))
    draw.circle(screen, "#2E8B57", (arvore_x + 15, arvore_y), 80)
    draw.polygon(screen, "#6A0DAD", [
        (casa_x - 40, casa_y),
        (casa_x + casa_largura + 40, casa_y),
        (casa_x + casa_largura / 2, casa_y - 150)])
    draw.rect(screen, "#3B3B3B", (casa_x, casa_y, casa_largura, casa_altura))
    draw.rect(screen, "#1FA31F", (casa_x + 30, casa_y + 50, 60, 70))
    draw.rect(screen, "#4B2E13", (casa_x + 150, casa_y + 70, 80, 130))
    draw.circle(screen, "#000000", (casa_x + 220, casa_y + 135), 5)
    screen.blit(image, (200, 420))
    texto_render = fonte.render(texto, True, "#8A2BE2")
    screen.blit(texto_render, (150, 370))
    display.update()
quit()