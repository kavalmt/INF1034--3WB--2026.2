from pygame import *

init()
screen = display.set_mode((1280, 720))
running = True
clock = time.Clock()

fonte = font.Font("fontecoringa.otf", 40)
image = image.load("coringa.png")
image = transform.scale(image, (180, 180))
mixer.music.load("gotham.mp3")
mixer.music.play(-1)

sfx_manha = mixer.Sound("manha.mp3")
sfx_tarde = mixer.Sound("tarde.mp3")
sfx_noite = mixer.Sound("gotham.mp3")
canal_sfx = mixer.Channel(0)  

texto = "Why so serious ?"

sol_x = 130
sol_y = 130
sol_raio = 70
sol_vel = 250            
sol_limite = 110         

nuvem_x = 850
nuvem_y = 150
nuvem_vel = 120
nuvem_dir = 1             
nuvem_borda_esq = 45      
nuvem_borda_dir = 215  


casa_x = 500
casa_largura = 260
casa_altura = 200
casa_y = 600 - casa_altura
arvore_x = 980
arvore_tronco_altura = 120
arvore_y = 600 - 60 - arvore_tronco_altura
cor_manha = (255, 200, 150)   
cor_tarde = (135, 206, 235)   
cor_noite = (15, 15, 60)      

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEMOTION:
            sol_x, sol_y = ev.pos
        if ev.type == MOUSEBUTTONUP:
            faixa = (720 - 2 * sol_limite) / 3
            if sol_y < sol_limite + faixa:
                canal_sfx.play(sfx_manha)
            elif sol_y < sol_limite + 2 * faixa:
                canal_sfx.play(sfx_tarde)
            else:
                canal_sfx.play(sfx_noite)
    dt = clock.get_time() / 1000
    keys = key.get_pressed()

    if keys[K_a] or keys[K_LEFT]:
        sol_x = sol_x - sol_vel * dt
    if keys[K_d] or keys[K_RIGHT]:
        sol_x = sol_x + sol_vel * dt
    if keys[K_w] or keys[K_UP]:
        sol_y = sol_y - sol_vel * dt
    if keys[K_s] or keys[K_DOWN]:
        sol_y = sol_y + sol_vel * dt

    
    if sol_x < sol_limite:
        sol_x = sol_limite
    elif sol_x > 1280 - sol_limite:
        sol_x = 1280 - sol_limite
    if sol_y < sol_limite:
        sol_y = sol_limite
    elif sol_y > 720 - sol_limite:
        sol_y = 720 - sol_limite

    nuvem_x = nuvem_x + nuvem_vel * nuvem_dir * dt
    if nuvem_x + nuvem_borda_dir >= 1280:
        nuvem_x = 1280 - nuvem_borda_dir
        nuvem_dir = -1
    elif nuvem_x - nuvem_borda_esq <= 0:
        nuvem_x = nuvem_borda_esq
        nuvem_dir = 1

    meio_tela = 720 / 2
    if sol_y <= meio_tela:
        t = (sol_y - sol_limite) / (meio_tela - sol_limite)
        if t < 0:
            t = 0
        elif t > 1:
            t = 1
        r = cor_manha[0] + (cor_tarde[0] - cor_manha[0]) * t
        g = cor_manha[1] + (cor_tarde[1] - cor_manha[1]) * t
        b = cor_manha[2] + (cor_tarde[2] - cor_manha[2]) * t
    else:
        t = (sol_y - meio_tela) / (720 - sol_limite - meio_tela)
        if t < 0:
            t = 0
        elif t > 1:
            t = 1
        r = cor_tarde[0] + (cor_noite[0] - cor_tarde[0]) * t
        g = cor_tarde[1] + (cor_noite[1] - cor_tarde[1]) * t
        b = cor_tarde[2] + (cor_noite[2] - cor_tarde[2]) * t

    background_color = (int(r), int(g), int(b))

    ## Draw
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