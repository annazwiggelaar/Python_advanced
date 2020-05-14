import pygame


def draw_board(the_board):
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]

    n = len(the_board)
    surface_size = 1000
    square_size = surface_size // n
    surface_size = n * square_size

    surface = pygame.display.set_mode((surface_size, surface_size))

    ball = pygame.image.load("ball.jpg")
    ball_offset = (square_size - ball.get_width()) // 2

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        for row in range(n):
            color_index = row % 2
            for col in range(n):
                the_square = (col * square_size, row * square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                color_index = (color_index + 1) % 2

        for (col, row) in enumerate(the_board):
            surface.blit(ball, (col * square_size + ball_offset, row * square_size + ball_offset))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2]) # 7 x 7 to test window size


