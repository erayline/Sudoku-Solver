import pygame
import sys
import time

sudoku_start_map = [
    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0],


    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    

    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0],
    [0, 0, 0,       0, 0, 0,        0, 0, 0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            
            bo[row][col] = 0
    return False
    


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None







SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SUDOKU_MAP_WIDTH = 720
SUDOKU_MAP_HEIGHT = 720

SUDOKU_MAP_STARTİNG_X = 500
SUDOKU_MAP_STARTİNG_Y = SCREEN_HEIGHT/2 - SUDOKU_MAP_HEIGHT/2

CELL_SIZE = SUDOKU_MAP_WIDTH // 9

WHITE = (225, 205, 205)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (200,50,100)

pygame.init()

# Ekran oluştur
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Team 1 Sudoku Solver")

clicked_solve = 0

def draw_board():
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X,SUDOKU_MAP_STARTİNG_Y),(i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, SUDOKU_MAP_HEIGHT + SUDOKU_MAP_STARTİNG_Y), 5)
            pygame.draw.line(screen, BLACK, (SUDOKU_MAP_STARTİNG_X,i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), (SUDOKU_MAP_WIDTH + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), 5)

        else:
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X,SUDOKU_MAP_STARTİNG_Y),(i * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, SUDOKU_MAP_HEIGHT + SUDOKU_MAP_STARTİNG_Y), 2)
            pygame.draw.line(screen, BLACK, (SUDOKU_MAP_STARTİNG_X,i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), (SUDOKU_MAP_WIDTH + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y), 2)
    pygame.draw.rect(screen,BLACK,(200,930,400,100),10,10)
    
    font = pygame.font.Font(None, 56)
    text = font.render("Click 'k' to solve", False, GREEN)
    screen.blit(text, (255,960))


def draw_numbers(board):
    font = pygame.font.Font(None, 46)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), False, BLACK)
                screen.blit(text, (j * CELL_SIZE + CELL_SIZE/2 - 10 + SUDOKU_MAP_STARTİNG_X, i * CELL_SIZE + CELL_SIZE/2 -10 + SUDOKU_MAP_STARTİNG_Y))

    text_game = font.render("Game", False, BLUE)
    screen.blit(text_game, (370,100))
    text_solutions = font.render("Solution", False, BLUE)
    screen.blit(text_solutions, (1270,100))





def main():

    clock = pygame.time.Clock()
    selected = None
    clicked_solve = 0


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
                    elif event.key == pygame.K_k:
                        clicked_solve = 1

        

        screen.fill(WHITE)
        draw_board()
        draw_numbers(sudoku_start_map)

        if (clicked_solve):
            solve(sudoku_start_map)
            clicked_solve = 0
        

        if selected:
            pygame.draw.rect(screen, GREEN, (selected[0] * CELL_SIZE + SUDOKU_MAP_STARTİNG_X, selected[1] * CELL_SIZE + SUDOKU_MAP_STARTİNG_Y, CELL_SIZE, CELL_SIZE), 5)

            print(sudoku_start_map[selected[1]][selected[0]]) # selected1 x selected0 y gibi davranıyor.
            if NumberEnter != 0:
                sudoku_start_map[selected[1]][selected[0]] = NumberEnter
                NumberEnter = 0
        


        pygame.display.flip()
        clock.tick(1000)
NumberEnter = 0
main()


