
import pygame
import app.game as game
import utils.settings as s



def draw_grid(screen, word_length, attempts, current_attempt):
    cell_size = min(
        s.cell_size,
        (s.widht - 40 - s.gap * (word_length - 1))
        // word_length
    )

    grid_width = (
        word_length * cell_size
        + (word_length - 1) * s.gap
    )
    start_x = (s.widht - grid_width) // 2

    letter_font = pygame.font.SysFont(
        s.font, max(18, int(cell_size * 0.55)), bold=True
    )

    for row in range(s.rows):
        for col in range(word_length):
            x = start_x + col * (cell_size + s.gap)
            y = s.grid_top + row * (cell_size + s.gap)

            rect = pygame.Rect(x, y, cell_size, cell_size)

            letter = ""
            color = s.background_color

            if row < len(attempts):
                letter, color_name = attempts[row][col]

                if color_name == "green":
                    color = s.green_color
                elif color_name == "yellow":
                    color = s.yellow_color
                else:
                    color = s.grey_color

            elif row == len(attempts) and col < len(current_attempt):
                letter = current_attempt[col]

            pygame.draw.rect(screen, color, rect, border_radius=3)

            pygame.draw.rect(
                screen,
                s.grey_color,
                rect,
                width=2,
                border_radius=3
            )

            if letter:
                rendered = letter_font.render(
                    letter, True, s.white_color
                )
                screen.blit(
                    rendered,
                    rendered.get_rect(center=rect.center)
                )


def run(word_length, target):
    pygame.init()

    screen = pygame.display.set_mode((s.widht, s.height))
    pygame.display.set_caption("Wordle - Partie")

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(s.font, 36, bold=True)
    message_font = pygame.font.SysFont(s.font, 20)

    title = title_font.render("WORDLE", True, s.white_color)
    title_rect = title.get_rect(center=(s.widht // 2, 55))

    attempts = []
    current_attempt = ""
    message = ""

    game_result = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_result = "quit"
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_result = "quit"
                    running = False

                elif event.key == pygame.K_BACKSPACE:
                    current_attempt = current_attempt[:-1]
                    message = ""

                elif event.key == pygame.K_RETURN:
                    if len(current_attempt) != word_length:
                        message = (
                            f"Il faut {word_length} lettres."
                        )

                    elif not current_attempt.isalpha():
                        message = "Utilise uniquement des lettres."

                    else:
                        feedback = game.check_letters(
                            current_attempt, target
                        )
                        attempts.append(feedback)

                        if game.is_winner(current_attempt, target):
                            game_result = "win"
                            running = False

                        elif len(attempts) >= s.rows:
                            game_result = "lose"
                            running = False

                        current_attempt = ""
                        message = ""

                elif event.unicode.isalpha():
                    if len(current_attempt) < word_length:
                        current_attempt += event.unicode.upper()
                        message = ""

        screen.fill(s.background_color)
        screen.blit(title, title_rect)

        draw_grid(
            screen,
            word_length,
            attempts,
            current_attempt
        )

        if message:
            message_surface = message_font.render(
                message, True, s.white_color
            )
            screen.blit(
                message_surface,
                message_surface.get_rect(
                    center=(s.widht // 2, s.height - 45)
                )
            )

        pygame.display.flip()
        clock.tick(s.fps)

    pygame.quit()
    return game_result
