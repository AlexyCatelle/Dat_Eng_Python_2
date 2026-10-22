import pygame
import settings as s

def draw_grid(screen, word_length) :

    cell_SIZE = min(
        s.cell_size,
        (s.widht - 80 - s.gap * (word_length - 1)) // word_length
    )

    grid_width = word_length * s.cell_size + (word_length - 1) * s.gap
    start_x = (s.widht - grid_width) // 2

    for row in range(s.rows):
        for col in range(word_length):
            x = start_x + col * (s.cell_size + s.gap)
            y = s.grid_top + row * (s.cell_size + s.gap)

            pygame.draw.rect(
                screen,
                s.border_color,
                (x, y, s.cell_size, s.cell_size),
                width=2
            )


def run(word_length, target):
    pygame.init()
    # Conserve les lignes déjà validées
    attempts = [""] * 6
    # Lettres en train d'être tapées
    current_attempt = ""
    # Ligne active
    current_row = 0

    # titre
    title_font = pygame.font.SysFont("arial", 40, bold=True)
    title = title_font.render("WORDLE", True, s.white_color)
    title_box = title.get_rect(center=(s.widht //2, 55))
    
    screen = pygame.display.set_mode((s.widht, s.height))
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