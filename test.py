import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Progressio Game")

# Fonts
font = pygame.font.Font(None, 48)
menu_font = pygame.font.Font(None, 36)

# Cube attributes
cube_size = 50
cube_x, cube_y = 500, 450  # Specify the starting location here
cube_speed = 7

# Falling cube attributes
falling_cube_size = 20
falling_cubes = []
red_cubes = []

# Score and Lives
score = 0
lives = 3

# Game state
is_playing = False

def show_menu():
    screen.fill(BLACK)
    title_text = font.render("Progressio Game", True, WHITE)
    play_text = menu_font.render("Play", True, WHITE)
    quit_text = menu_font.render("Quit", True, WHITE)

    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Add game instructions
    instructions_text = menu_font.render("How to Play:", True, WHITE)
    instructions_rect = instructions_text.get_rect(topleft=(10, HEIGHT - 130))

    arrow_keys_text = menu_font.render("Use arrow keys to move", True, WHITE)
    collect_green_text = menu_font.render("Collect Green. These mitigate climate change", True, GREEN)
    avoid_red_text = menu_font.render("Avoid Red. These exacerbate climate change", True, RED)


    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(quit_text, quit_rect)
    screen.blit(instructions_text, instructions_rect)

    # Draw additional instructions
    instructions_y = instructions_rect.bottom
    screen.blit(arrow_keys_text, (20, instructions_y))
    instructions_y += 40
    screen.blit(collect_green_text, (20, instructions_y))
    instructions_y += 40
    screen.blit(avoid_red_text, (20, instructions_y))

    return play_rect, quit_rect

def initialize_game():
    global cube_x, score, lives, falling_cubes, red_cubes
    cube_x, cube_y = 200, 300
    score = 0
    lives = 3
    falling_cubes = []
    red_cubes = []

initialize_game()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not is_playing:
            if play_rect.collidepoint(event.pos):
                is_playing = True
                initialize_game()
            elif quit_rect.collidepoint(event.pos):
                running = False

    if is_playing:
        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cube_x -= cube_speed
        if keys[pygame.K_RIGHT]:
            cube_x += cube_speed

        # Boundary checking for the main cube
        cube_x = max(0, min(cube_x, WIDTH - cube_size))

        # Create random falling cubes
        if random.randint(1, 100) < 3:  # Adjust this probability as needed
            cube_type = random.choice([GREEN, RED])
            cube_list = red_cubes if cube_type == RED else falling_cubes
            cube_list.append([random.randint(0, WIDTH - falling_cube_size), 0, cube_type])

        # Update falling cube positions
        for cube_list in [falling_cubes, red_cubes]:
            for cube in cube_list:
                cube[1] += 5  # Adjust the falling speed as needed
                if cube[1] > HEIGHT:
                    cube_list.remove(cube)
                if cube_x < cube[0] < cube_x + cube_size and cube_y < cube[1] < cube_y + cube_size:
                    cube_list.remove(cube)
                    if cube[2] == GREEN:
                        score += 1
                    elif cube[2] == RED:
                        lives -= 1

        # Clear the screen
        screen.fill(WHITE)

        # Draw the main cube
        pygame.draw.rect(screen, RED, (cube_x, cube_y, cube_size, cube_size))

        # Draw falling cubes
        for cube in falling_cubes:
            pygame.draw.rect(screen, GREEN, (cube[0], cube[1], falling_cube_size, falling_cube_size))

        # Draw red cubes
        for cube in red_cubes:
            pygame.draw.rect(screen, RED, (cube[0], cube[1], falling_cube_size, falling_cube_size))

        # Draw the score
        score_text = font.render(f"Score: {score}", True, GREEN)  # Change the color to GREEN
        screen.blit(score_text, (10, 10))

        # Draw lives
        lives_text = font.render(f"Lives: {lives}", True, RED)
        screen.blit(lives_text, (10, 60))

        # Check for game over
        if lives <= 0:
            is_playing = False
            show_menu()

    else:
        play_rect, quit_rect = show_menu()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()