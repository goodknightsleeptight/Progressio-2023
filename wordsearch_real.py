import pygame
import random
import string

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = (600,600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# List of words to include in the word search
words = ["GREEN", "EARTH", "POLLUTION", "REDUCE", "RECYCLE", "REUSE", "FOSSILFUELS", "SUSTAINABILITY", "OCEAN",
         "DEFORESTATION", "ECOLOGY", "WILDLIFE", "CLIMATECHANGE", "CARBONDIOXIDE"]

# Initialize an empty grid filled with random letters
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

found_words=[]

# Function to check if a word can be placed at a given location
def can_place_word(word, row, col, direction):
    if direction == "horizontal":
        return all(grid[row][col + i] == '' or grid[row][col + i] == word[i] for i in range(len(word)))
    else:
        return all(grid[row + i][col] == '' or grid[row + i][col] == word[i] for i in range(len(word)))

# Place the words in the grid
for word in words:
    direction = random.choice(["horizontal", "vertical"])
    if direction == "horizontal":
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - len(word))
    else:
        row = random.randint(0, GRID_SIZE - len(word))
        col = random.randint(0, GRID_SIZE - 1)

    while not can_place_word(word, row, col, direction):
        direction = random.choice(["horizontal", "vertical"])
        if direction == "horizontal":
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - len(word))
        else:
            row = random.randint(0, GRID_SIZE - len(word))
            col = random.randint(0, GRID_SIZE - 1)

    for i, letter in enumerate(word):
        if direction == "horizontal":
            grid[row][col + i] = letter
        else:
            grid[row + i][col] = letter

# Fill the remaining empty cells with random letters
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == '':
            grid[i][j] = random.choice(string.ascii_uppercase)

# Initialize the Pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Word Search")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the word search grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            font = pygame.font.Font(None, 36)
            text = font.render(grid[i][j], True, BLACK)
            text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(text, text_rect)



    pygame.display.flip()


    x=input("Enter a word or press 'Q' to quit: ").upper()
    if x in words:
        print("That's a correct word")
    else:
        print("That's an incorrect word")



# Quit Pygame
pygame.quit()
