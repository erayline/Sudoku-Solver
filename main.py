import pygame
import sys
import os

sudoku_start_map = [
    [5, 3, 0,       0, 7, 0,        0, 0, 0],
    [6, 0, 0,       1, 9, 5,        0, 0, 0],
    [0, 9, 8,       0, 0, 0,        0, 6, 0],

    [8, 0, 0,       0, 6, 0,        0, 0, 3],
    [4, 0, 0,       8, 0, 3,        0, 0, 1],
    [7, 0, 0,       0, 2, 0,        0, 0, 6],

    [0, 6, 0,       0, 0, 0,        2, 8, 0],
    [0, 0, 0,       4, 1, 9,        0, 0, 5],
    [0, 0, 0,       0, 8, 0,        0, 7, 9]
]

sudoku_solution_map = [
    [5, 3, 4,       6, 7, 8,        9, 1, 2],
    [6, 7, 2,       1, 9, 5,        3, 4, 8],
    [1, 9, 8,       3, 4, 2,        5, 6, 7],
    
    
    [8, 5, 9,       7, 6, 1,        4, 2, 3],
    [4, 2, 6,       8, 5, 3,        7, 9, 1],
    [7, 1, 3,       9, 2, 4,        8, 5, 6],
    
    
    [9, 6, 1,       5, 3, 7,        2, 8, 4],
    [2, 8, 7,       4, 1, 9,        6, 3, 5],
    [3, 4, 5,       2, 8, 6,        1, 7, 9]
]
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SUDOKU_MAP_WIDTH = 720
SUDOKU_MAP_HEIGHT = 720

SUDOKU_MAP_STARTİNG_X = 50
SUDOKU_MAP_STARTİNG_Y = SCREEN_HEIGHT/2 - SUDOKU_MAP_HEIGHT/2

CELL_SIZE = SUDOKU_MAP_WIDTH // 9

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,240,20)

pygame.init()

# Ekran oluştur
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Team 1 Sudoku Solver")


def draw_board():
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X,SUDOKU_MAP_STARTİNG_Y),(i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, SUDOKU_MAP_HEIGHT + SUDOKU_MAP_STARTİNG_Y), 5)
            pygame.draw.line(screen, BLACK, (SUDOKU_MAP_STARTİNG_X,i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), (SUDOKU_MAP_WIDTH + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), 5)

        else:
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X,SUDOKU_MAP_STARTİNG_Y),(i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, SUDOKU_MAP_HEIGHT + SUDOKU_MAP_STARTİNG_Y), 2)
            pygame.draw.line(screen, BLACK, (SUDOKU_MAP_STARTİNG_X,i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), (SUDOKU_MAP_WIDTH + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), 2)


def draw_numbers(board):
    font = pygame.font.Font(None, 46)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), False, BLACK)
                screen.blit(text, (j * CELL_SIZE + CELL_SIZE/2 - 10 + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + CELL_SIZE/2 -10 + SUDOKU_MAP_STARTİNG_Y))
    text_game = font.render("Game", False, BLUE)
    screen.blit(text_game, (370,100))
    text_solutions = font.render("Solutions", False, BLUE)
    screen.blit(text_solutions, (1270,100))

# def solve_the_thing_please(board_game,board_solution):
#     for str_o in range(9): #o as in out
#         for stn_o in range(9):
#             if board_game[str_o][stn_o] == 0:
#                 for str_i in range():
                    
                


def main():

    clock = pygame.time.Clock()
    selected = None


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (SUDOKU_MAP_STARTİNG_X<x and SUDOKU_MAP_STARTİNG_X + SUDOKU_MAP_WIDTH>x)and (SUDOKU_MAP_STARTİNG_Y<y and SUDOKU_MAP_STARTİNG_Y +SUDOKU_MAP_HEIGHT > y):
                    selected = (
                        int((x - SUDOKU_MAP_STARTİNG_X)// CELL_SIZE),
                        int((y - SUDOKU_MAP_STARTİNG_Y)// CELL_SIZE)
                    )

            elif event.type == pygame.KEYDOWN:
                global NumberEnter
                if(event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if NumberEnter == 0:
                    if event.key == pygame.K_1:
                        NumberEnter = 1
                    elif event.key == pygame.K_2:
                        NumberEnter = 2
                    elif event.key == pygame.K_3:
                        NumberEnter = 3
                    elif event.key == pygame.K_4:
                        NumberEnter = 4
                    elif event.key == pygame.K_5:
                        NumberEnter = 5
                    elif event.key == pygame.K_6:
                        NumberEnter = 6
                    elif event.key == pygame.K_7:
                        NumberEnter = 7
                    elif event.key == pygame.K_8:
                        NumberEnter = 8
                    elif event.key == pygame.K_9:
                        NumberEnter = 9

                

        screen.fill(WHITE)
        draw_board()
        draw_numbers(sudoku_start_map)



        if selected:
            pygame.draw.rect(screen, GREEN, (selected[0] * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, selected[1] * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y, CELL_SIZE, CELL_SIZE), 5)

            print(sudoku_start_map[selected[1]][selected[0]]) # selected1 x selected0 y gibi davranıyor.
            if NumberEnter != 0:
                sudoku_start_map[selected[1]][selected[0]] = NumberEnter
                NumberEnter = 0
        


        pygame.display.flip()
        clock.tick(30)
NumberEnter = 0
main()
