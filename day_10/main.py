import pygame


# Inicilizar Pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800,600))


# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)



# Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368 # Se calcula del tamaño 800 / 2 = 400 y hay que restar el tamaño en pixel de la imagen que se descargo
jugador_y = 536

def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))



# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB
    pantalla.fill((205, 144, 228))
    jugador_x += 0.1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False


    jugador(jugador_x, jugador_y)

    pygame.display.update()