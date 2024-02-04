import pygame
import random

# Constants
GRID_SIZE = 80
SQUARE_SIZE = 8
WHITE = (255, 255, 255)
BLACK = (170, 140, 0)
FALL_DELAY = 10  # Adjust the delay in milliseconds
fall=False
rain=False

# Create a window
window_size = (GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Grid Example')

# Initialize the grid with all white squares
grid = [[WHITE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

dragging = False

def direction(number):
    if number >= 0:
        return round(number + 0.5)
    else:
        return round(number - 0.5)

def move_down_right():
    for row in range(GRID_SIZE - 2, -1, -1):  # Start from the second-to-last row and move upwards
        for col in range(GRID_SIZE):  # Exclude the last column
            if grid[row][col] == BLACK:
                if grid[row+1][col] == WHITE:
                    # Move the black square to the right of the square below it
                    grid[row+1][col] = BLACK
                    grid[row][col] = WHITE
                elif col==GRID_SIZE-1:
                    if grid[row + 1][col-1]==WHITE:
                        grid[row + 1][col-1] = BLACK
                        grid[row][col] = WHITE
                elif col==0:
                    if grid[row + 1][col+1]==WHITE:
                        grid[row + 1][col+1] = BLACK
                        grid[row][col] = WHITE
                elif grid[row + 1][col + 1] == WHITE and grid[row + 1][col - 1] == WHITE:
                    # Move the black square to the right or left
                    # of the square below it
                    grid[row + 1][col+direction(random.uniform(-0.5, 0.5))] = BLACK
                    grid[row][col] = WHITE
                elif grid[row + 1][col + 1] == WHITE and col<GRID_SIZE:
                    grid[row + 1][col + 1] = BLACK
                    grid[row][col] = WHITE
                elif grid[row + 1][col - 1] == WHITE and col>0:
                    grid[row + 1][col - 1] = BLACK
                    grid[row][col] = WHITE

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                grid = [[WHITE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
            if event.key == pygame.K_SPACE:
                if fall:
                    fall=False
                    rain=False
                else: fall=True
            if event.key == pygame.K_r:
                if rain:
                    rain=False
                else:
                    rain=True
                    fall=True
    if dragging:
        # Get the mouse position
        x, y = pygame.mouse.get_pos()

        # Determine the dragged square
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        # Change the color of the dragged square to black if the mouse is inside the window
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            grid[row][col] = BLACK


    if rain:
        grid[0][random.randint(0, GRID_SIZE-1)]=BLACK

    if fall:
        move_down_right()  # Check and move squares down and to the right

    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[row][col], (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

    pygame.time.delay(FALL_DELAY)  # Introduce delay for falling

pygame.quit()
