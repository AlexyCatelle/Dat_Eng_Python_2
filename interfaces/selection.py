
import pygame
import utils.settings as s


def run(available_lengths):
    if not available_lengths:
        return None

    pygame.init()

    screen = pygame.display.set_mode((s.widht, s.height))
    pygame.display.set_caption("Wordle : Sélection")

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(s.font, 42, bold=True)
    text_font = pygame.font.SysFont(s.font, 24)
    button_font = pygame.font.SysFont(s.font, 32, bold=True)
    value_font = pygame.font.SysFont(s.font, 36, bold=True)

    title = title_font.render("Wordle", True, s.white_color)

    instruction = text_font.render(
        "Choisir la longueur du mot",
        True,
        s.white_color
    )

    title_rect = title.get_rect(
        center=(s.widht // 2, 100)
    )

    instruction_rect = instruction.get_rect(
        center=(s.widht // 2, 210)
    )

    # Boutons du sélecteur
    button_size = 55

    minus_rect = pygame.Rect(
        s.widht // 2 - 100,
        310,
        button_size,
        button_size
    )

    plus_rect = pygame.Rect(
        s.widht // 2 + 45,
        310,
        button_size,
        button_size
    )

    # Première longueur disponible
    selected_length = available_lengths[0]

    running = True
    confirmed = False

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if minus_rect.collidepoint(event.pos):
                        current_index = available_lengths.index(
                            selected_length
                        )

                        if current_index > 0:
                            selected_length = available_lengths[
                                current_index - 1
                            ]

                    elif plus_rect.collidepoint(event.pos):
                        current_index = available_lengths.index(
                            selected_length
                        )

                        if current_index < len(available_lengths) - 1:
                            selected_length = available_lengths[
                                current_index + 1
                            ]

                    elif start_rect.collidepoint(event.pos):
                        confirmed = True
                        running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    current_index = available_lengths.index(
                        selected_length
                    )

                    if current_index > 0:
                        selected_length = available_lengths[
                            current_index - 1
                        ]

                elif event.key == pygame.K_RIGHT:
                    current_index = available_lengths.index(
                        selected_length
                    )

                    if current_index < len(available_lengths) - 1:
                        selected_length = available_lengths[
                            current_index + 1
                        ]

                elif event.key == pygame.K_RETURN:
                    confirmed = True
                    running = False

                elif event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(s.background_color)

        screen.blit(title, title_rect)
        screen.blit(instruction, instruction_rect)

        # Bouton moins
        pygame.draw.rect(
            screen,
            s.grey_color,
            minus_rect,
            border_radius=5
        )

        minus_text = button_font.render(
            "-",
            True,
            s.white_color
        )

        screen.blit(
            minus_text,
            minus_text.get_rect(center=minus_rect.center)
        )

        # Longueur sélectionnée
        value_text = value_font.render(
            str(selected_length),
            True,
            s.white_color
        )

        value_rect = value_text.get_rect(
            center=(s.widht // 2, 337)
        )

        screen.blit(value_text, value_rect)

        # Bouton plus
        pygame.draw.rect(
            screen,
            s.green_color,
            plus_rect,
            border_radius=5
        )

        plus_text = button_font.render(
            "+",
            True,
            s.white_color
        )
        # Bouton Commencer
        start_rect = pygame.Rect(
            s.widht // 2 - 110,
            490,
            220,
            60
        )

        screen.blit(
            plus_text,
            plus_text.get_rect(center=plus_rect.center)
        )
        
        # Bouton Commencer
        pygame.draw.rect(
            screen,
            s.green_color,
            start_rect,
            border_radius=10
        )

        start_text = button_font.render(
            "Commencer",
            True,
            s.white_color
        )

        screen.blit(
            start_text,
            start_text.get_rect(center=start_rect.center)
        )

        pygame.display.flip()
        clock.tick(s.fps)

    pygame.quit()

    if confirmed:
        return selected_length

    return None
