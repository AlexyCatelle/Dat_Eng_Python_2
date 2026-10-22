import pygame

pygame.init()

widht, height = 600, 700
screen = pygame.display.set_mode((widht, height))
pygame.display.set_caption("Wordle")

clock = pygame.time.Clock()
running = True

# Couleurs RGB
background_color = (18, 18, 19)
white_color = (255, 255, 255)
border_color = (80, 80, 80)

    # titre
title_font = pygame.font.SysFont("arial", 40, bold=True)
title = title_font.render("WORDLE", True, white_color)
title_box = title.get_rect(center=(widht //2, 55))

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)



    screen.blit(title, title_box)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()