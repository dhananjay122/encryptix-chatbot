import sys
import pygame
import numpy as np


pygame.init()

WHITE=(255,255,255)
GRAY=(160,160,160)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)


WIDTH=700
HEIGHT=700
LINE_WIDTH=5
ROWS=3
COLS=3
CELL_SIZE=WIDTH//COLS
CIRCLE_RADIUS=CELL_SIZE//3
CIRCLE_WIDTH=15
CROSS_WIDTH=25

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')


board=np.zeros((ROWS,COLS))
screen.fill(BLACK)



def draw_lines(color=WHITE):
    for i in range(1,ROWS):
        pygame.draw.line(screen,color,(0,CELL_SIZE*i),(WIDTH,CELL_SIZE*i),LINE_WIDTH)
        pygame.draw.line(screen,color,(CELL_SIZE*i,0),(CELL_SIZE*i,HEIGHT),LINE_WIDTH)

def draw_pawns(color=WHITE):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,color,(int(col*CELL_SIZE+CELL_SIZE//2),int(row*CELL_SIZE+CELL_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen,color,(col*CELL_SIZE+CELL_SIZE//4,row*CELL_SIZE+CELL_SIZE//4),(col*CELL_SIZE+3*CELL_SIZE//4,row*CELL_SIZE+3*CELL_SIZE//4),CROSS_WIDTH)
                pygame.draw.line(screen,color,(col*CELL_SIZE+CELL_SIZE//4,row*CELL_SIZE+3*CELL_SIZE//4),(col*CELL_SIZE+3*CELL_SIZE//4,row*CELL_SIZE+CELL_SIZE//4),CROSS_WIDTH)

def mark_square(row,col,player):
    board[row][col]=player

def available_square(row,col):
    return board[row][col]==0


def is_board_full(check_board=board):
    for row in range(ROWS):
        for col in range(COLS):
            if check_board[row][col]==0:
                return False
    return True

def check_win(player,check_board=board):
    for col in range(COLS):
        if check_board[0][col]==player and check_board[1][col]==player and check_board[2][col]==player:
            return True
    for row in range(ROWS):
        if check_board[row][0]==player and check_board[row][1]==player and check_board[row][2]==player:
            return True
    if check_board[0][0]==player and check_board[1][1]==player and check_board[2][2]==player:
        return True
    if check_board[0][2]==player and check_board[1][1]==player and check_board[2][0]==player:
        return True
    return False

def minimax(minimax_board,depth,maximizing):
    if check_win(2,minimax_board):
        return float('inf')
    elif check_win(1,minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0
    if maximizing:
        best_score=-100
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col]==0:
                    minimax_board[row][col]=2
                    score=minimax(minimax_board,depth+1,maximizing=False)
                    minimax_board[row][col]=0
                    best_score=max(score,best_score)
        return best_score
    else:
        best_score=100
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col]==0:
                    minimax_board[row][col]=1
                    score=minimax(minimax_board,depth+1,maximizing=True)
                    minimax_board[row][col]=0
                    best_score=min(score,best_score)
        return best_score

def best_move(board=board):
    best_score=-1000
    move=(-1,-1)
    for row in range(COLS):
        for col in range(COLS):
            if board[row][col]==0:
                board[row][col]=2
                score=minimax(board,depth=0,maximizing=False)
                board[row][col]=0
                if score>best_score:
                    best_score=score
                    move=(row,col)
    if move!=(-1,-1):
        mark_square(move[0],move[1],2)
        return True
    return False

def restart_game():
    screen.fill(BLACK)
    draw_lines()
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col]=0
def main():
    draw_lines()
    player=1
    game_over=False

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX=event.pos[0]//CELL_SIZE
                mouseY=event.pos[1]//CELL_SIZE
                if available_square(mouseY,mouseX):
                    mark_square(mouseY,mouseX,player)
                    if check_win(player):
                        game_over=True
                    player=player%2 + 1
                    if not game_over:
                        if best_move():
                            if check_win(2):
                                game_over=True
                        player=player%2+1
                    if not game_over:
                        if is_board_full():
                            game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    restart_game()
                    game_over=False
                    player=1

        if not game_over:
            draw_pawns()

        else:
            if check_win(1):
                draw_pawns(GREEN)
                draw_lines(GREEN)

            elif check_win(2):
                draw_pawns(RED)
                draw_lines(RED)

            else:
                draw_pawns(GRAY)
                draw_lines(GRAY)
                
                

    
        pygame.display.update()

if __name__=="__main__":
    main()

