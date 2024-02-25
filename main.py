import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
CROSS_SPACE = SQUARE_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (255, 255, 255)
CROSS_COLOR = (66, 66, 66)
FONT_COLOR = (255, 255, 255)
QUESTION_FONT_SIZE = 30

# Create Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Fonts
question_font = pygame.font.Font(None, QUESTION_FONT_SIZE)

# Draw board lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X and O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + CROSS_SPACE, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE, row * SQUARE_SIZE + CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + CROSS_SPACE, row * SQUARE_SIZE + CROSS_SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, LINE_WIDTH)

# Draw question
def draw_question(question):
    question_text = question_font.render(question, True, FONT_COLOR)
    screen.blit(question_text, ((WIDTH - question_text.get_width()) // 2, HEIGHT // 2 - QUESTION_FONT_SIZE // 2))

# Check if there's a winner
def is_winner():
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '':
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True
    return False

# Check if the board is full
def is_board_full():
    for row in board:
        if '' in row:
            return False
    return True


def generate_question():
    # This is just a sample question generation function, you can replace it with your own question generator
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operator} {num2}?"
    answer = eval(f'{num1} {operator} {num2}')
    return question, answer

def main():
    turn = 'X'
    question, answer = generate_question()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not is_winner() and not is_board_full():
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if board[clicked_row][clicked_col] == '':
                    if turn == 'X':
                        if question:
                            draw_question(question)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT // 2 - QUESTION_FONT_SIZE // 2, WIDTH, QUESTION_FONT_SIZE))
                            pygame.display.update()
                            try:
                                user_answer = int(input("Your answer: "))
                            except ValueError:
                                user_answer = None
                            if user_answer == answer:
                                board[clicked_row][clicked_col] = 'X'
                                turn = 'O'
                                question, answer = generate_question()
                            else:
                                print("Wrong answer! You lose your turn.")
                                question, answer = generate_question()
                        else:
                            print("No question available. It's a draw.")
                    else:
                        if question:
                            draw_question(question)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT // 2 - QUESTION_FONT_SIZE // 2, WIDTH, QUESTION_FONT_SIZE))
                            pygame.display.update()
                            try:
                                user_answer = int(input("Your answer: "))
                            except ValueError:
                                user_answer = None
                            if user_answer == answer:
                                board[clicked_row][clicked_col] = 'O'
                                turn = 'X'
                                question, answer = generate_question()
                            else:
                                print("Wrong answer! You lose your turn.")
                                question, answer = generate_question()
                        else:
                            print("No question available. It's a draw.")
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        pygame.display.update()

        if is_winner():
            print(turn + " wins!")
            break
        if is_board_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
