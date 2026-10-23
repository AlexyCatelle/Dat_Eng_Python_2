import pygame
import utils.settings as s


def run(game_result, target):
    pygame.init()

    screen = pygame.display.set_mode((s.widht, s.height))
    pygame.display.set_caption("Wordle - Résultat")

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(s.font, 34, bold=True)
    text_font = pygame.font.SysFont(s.font, 24)
    button_font = pygame.font.SysFont(s.font, 22, bold=True)

    if game_result == "win":
        title_text = "Bravo, tu as gagné !"
        title_color = s.green_color
    else:
        title_text = "Dommage, tu as perdu."
        title_color = s.red_color

    title = title_font.render(title_text, True, title_color)
    title_rect = title.get_rect(
        center=(s.widht // 2, 170)
    )

    word_text = text_font.render(
        f"Le mot était : {target}",
        True,
        s.white_color
    )
    word_rect = word_text.get_rect(
        center=(s.widht // 2, 250)
    )

    button_width = 180
    button_height = 55

    replay_rect = pygame.Rect(
        (s.widht - button_width) // 2,
        350,
        button_width,
        button_height
    )

    quit_rect = pygame.Rect(
        (s.widht - button_width) // 2,
        430,
        button_width,
        button_height
    )

    running = True
    choice = "quit"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if replay_rect.collidepoint(event.pos):
                        choice = "replay"
                        running = False

                    elif quit_rect.collidepoint(event.pos):
                        running = False

        screen.fill(s.background_color)

        screen.blit(title, title_rect)
        screen.blit(word_text, word_rect)

        pygame.draw.rect(
            screen, s.green_color, replay_rect,
            border_radius=5
        )
        pygame.draw.rect(
            screen, s.grey_color, quit_rect,
            border_radius=5
        )

        replay_text = button_font.render(
            "Rejouer", True, s.white_color
        )
        quit_text = button_font.render(
            "Quitter", True, s.white_color
        )

        screen.blit(
            replay_text,
            replay_text.get_rect(center=replay_rect.center)
        )
        screen.blit(
            quit_text,
            quit_text.get_rect(center=quit_rect.center)
        )

        pygame.display.flip()
        clock.tick(s.fps)

    pygame.quit()
    return choice
