import pygame
import random

# Define the game window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Define the maze size and block size
MAZE_WIDTH = 20
MAZE_HEIGHT = 20
BLOCK_SIZE = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Choose mode
print('Normal/Classic = 1')
print('Hard = 2 (Bug)')
mode = input('Choose Mode >>> ')
Norm = True
try:
    mode = int(mode)
except:
    Norm = False
while Norm == False:
    mode = input('Error (Input type)! Choose Mode >>> ')
    try:
        mode = int(mode)
    except:
        Norm = False
    Norm = True

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Escape the Maze (by. ChatGPT)")

# Define the maze generation function
def generate_maze(width, height):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            if i == 0 or i == height-1 or j == 0 or j == width-1:
                row.append(mode)
            else:
                row.append(random.randint(0, 1))
        maze.append(row)
    return maze

# Define the function to draw the maze
def draw_maze(maze):
    for i in range(MAZE_HEIGHT):
        for j in range(MAZE_WIDTH):
            if maze[i][j] == 1:
                pygame.draw.rect(window, BLACK, (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Define the main game function
def play_game():
    # Generate the maze
    maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)

    # Define the player position and direction
    player_x = 1
    player_y = 1
    player_dir = "right"

    # Define the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_dir = "up"
                elif event.key == pygame.K_DOWN:
                    player_dir = "down"
                elif event.key == pygame.K_LEFT:
                    player_dir = "left"
                elif event.key == pygame.K_RIGHT:
                    player_dir = "right"

        # Move the player
        if player_dir == "up" and maze[player_y-1][player_x] == 0:
            player_y -= 1
        elif player_dir == "down" and maze[player_y+1][player_x] == 0:
            player_y += 1
        elif player_dir == "left" and maze[player_y][player_x-1] == 0:
            player_x -= 1
        elif player_dir == "right" and maze[player_y][player_x+1] == 0:
            player_x += 1

        # Check if the player has reached the end of the maze
        if player_x == MAZE_WIDTH-2 and player_y == MAZE_HEIGHT-2:
            running = False

        # Clear the screen and draw the maze and player
        window.fill(WHITE)
        draw_maze(maze)
        pygame.draw.rect(window, RED, (player_x*BLOCK_SIZE, player_y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Update the display
        pygame.display.update()

    # End the game
    pygame.quit()

# Start the game
play_game()
