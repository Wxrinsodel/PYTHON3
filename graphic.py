import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BACKGROUND_COLOR = (30, 30, 30)
CHARACTER_COLOR = (255, 100, 100)
FOOD_COLOR = (100, 255, 100)
TEXT_COLOR = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game Graphics")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 36)

# Character
character_radius = 15
character_pos = [WIDTH // 2, HEIGHT // 2]

# Food
food_radius = 10
food_pos = [random.randint(food_radius, WIDTH - food_radius),
            random.randint(food_radius, HEIGHT - food_radius)]

# Score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input for character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_pos[0] - character_radius > 0:
        character_pos[0] -= 5
    if keys[pygame.K_RIGHT] and character_pos[0] + character_radius < WIDTH:
        character_pos[0] += 5
    if keys[pygame.K_UP] and character_pos[1] - character_radius > 0:
        character_pos[1] -= 5
    if keys[pygame.K_DOWN] and character_pos[1] + character_radius < HEIGHT:
        character_pos[1] += 5

    # Check collision with food
    distance = ((character_pos[0] - food_pos[0]) ** 2 + (character_pos[1] - food_pos[1]) ** 2) ** 0.5
    if distance < character_radius + food_radius:
        score += 1
        food_pos = [random.randint(food_radius, WIDTH - food_radius),
                    random.randint(food_radius, HEIGHT - food_radius)]

    # Draw everything
    screen.fill(BACKGROUND_COLOR)  # Background color
    pygame.draw.circle(screen, CHARACTER_COLOR, character_pos, character_radius)  # Character
    pygame.draw.circle(screen, FOOD_COLOR, food_pos, food_radius)  # Food

    # Display score
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
