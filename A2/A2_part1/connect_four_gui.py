import pygame
import sys
import math
import random
import argparse
import numpy as np

# Import the solver functions and constants
from src.connect_four_solver import (
    ROW_COUNT,
    COLUMN_COUNT,
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    winning_move,
    minimax,
    is_terminal_node,
    get_valid_locations
)

# Constants for visual display
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 75)

def draw_board(board):
    """
    Draws the Connect Four board on the Pygame screen.
    """
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(
                screen, BLACK,
                (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)),
                RADIUS
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen, RED,
                    (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)),
                    RADIUS
                )
            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen, YELLOW,
                    (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)),
                    RADIUS
                )
    pygame.display.update()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "game_type",
        help="Type of game: 'human' or 'ai'",
        choices=["human", "ai"]
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=7,
        help="Depth for the minimax AI (default: 7)"
    )
    args = parser.parse_args()

    board = create_board()
    game_over = False
    turn = 0

    draw_board(board)
    pygame.display.update()

    # Human vs Human
    if args.game_type == "human":
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

                    # Player 1
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(posx / SQUARESIZE)

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                label = myfont.render("Player 1 wins!", 1, RED)
                                screen.blit(label, (40, 10))
                                game_over = True

                    # Player 2
                    else:
                        posx = event.pos[0]
                        col = int(posx / SQUARESIZE)

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 2)

                            if winning_move(board, 2):
                                label = myfont.render("Player 2 wins!", 1, YELLOW)
                                screen.blit(label, (40, 10))
                                game_over = True

                    draw_board(board)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(3000)

    else:
        # Human vs AI
        minimax_depth = args.depth

        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:  # Player 1's turn
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    col = int(posx / SQUARESIZE)

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        draw_board(board)

            # AI's turn
            if turn == 1 and not game_over:
                col, _ = minimax(board, minimax_depth, -math.inf, math.inf, True)
                if is_valid_location(board, col):
                    pygame.time.wait(500)
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                    draw_board(board)

                    turn += 1
                    turn = turn % 2

            if game_over:
                pygame.time.wait(3000)

if __name__ == "__main__":
    main()
