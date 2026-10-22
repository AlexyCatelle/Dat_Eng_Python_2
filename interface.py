import pygame

widht, height = 600, 700

# Couleurs RGB
background_color = (18, 18, 19)
white_color = (255, 255, 255)
border_color = (80, 80, 80)

# Grille
rows = 6
cell_size = 52
gap = 8
grid_top = 110


def draw_grid(screen, word_length) :

    cell_SIZE = min(
        cell_size,
        (widht - 80 - gap * (word_length - 1)) // word_length
    )

    grid_width = word_length * cell_size + (word_length - 1) * gap
    start_x = (widht - grid_width) // 2

    for row in range(rows):
        for col in range(word_length):
            x = start_x + col * (cell_size + gap)
            y = grid_top + row * (cell_size + gap)

            pygame.draw.rect(
                screen,
                border_color,
                (x, y, cell_size, cell_size),
                width=2
            )


def run(word_length):
    pygame.init()

    # titre
    title_font = pygame.font.SysFont("arial", 40, bold=True)
    title = title_font.render("WORDLE", True, white_color)
    title_box = title.get_rect(center=(widht //2, 55))
    
    screen = pygame.display.set_mode((widht, height))
    pygame.display.set_caption("Wordle")

    clock = pygame.time.Clock()
    running = True
    
    while running:
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(background_color)

        screen.blit(title, title_box)

        draw_grid(screen, word_length)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()