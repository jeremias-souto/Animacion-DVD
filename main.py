import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animacion DVD")

# Configuración del logo DVD
dvd_logo = pygame.image.load("Imagenes\DVD.png")
logo_rect = dvd_logo.get_rect()
speed = [4, 4] # Velocidad inicial

# Bucle Principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Mover el logo
    logo_rect.x += speed[0]
    logo_rect.y += speed[1]

    # Rebotar en los bordes
    if logo_rect.left < 0 or logo_rect.right > width:
        speed[0] = -speed[0]
    if logo_rect.top < 0 or logo_rect.bottom > height:
        speed[1] = -speed[1]

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar el logo en la nueva posicion
    screen.blit(dvd_logo, logo_rect)

    # Actulizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la animacion
    pygame.time.Clock().tick(60)