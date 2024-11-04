import pygame
import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Create the game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title of the game window
pygame.display.set_caption('Wormy')

# font for displaying the score
font = pygame.font.SysFont(None, 30)

# Set the colors for the game elements
BACKGROUND_COLOR = (139, 69, 19)
SNAKE_COLOR = (243, 207, 198)
FOOD_COLOR = (255, 0, 0)

# Set the size of the snake and the food
BLOCK_SIZE = 10

# Set the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Set the initial position of the food
food_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                 random.randrange(1, (SCREEN_HEIGHT//10)) * 10]

# Load in the sound effect
eat_sound = pygame.mixer.Sound("chomp.wav")

# Define a function to draw the snake and the food
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(window, SNAKE_COLOR, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_food(food_position):
    # Load the apple image
    apple_image = pygame.image.load("apple.png")
    apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))

    # load the apple image at the food position
    window.blit(apple_image, [food_position[0], food_position[1]])

# function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, [0, 0])

# defined main game loop
def game_loop():
    # Set the initial score to 0
    score = 0

    # Sets the initial position and direction of the snake
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = "RIGHT"

    # Set the initial position of the food
    food_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                     random.randrange(1, (SCREEN_HEIGHT//10)) * 10]

    # Create a clock object to control the game FPS
    fps_controller = pygame.time.Clock()

    # Run the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Move the snake
        if direction == "UP":
            snake_position[1] -= BLOCK_SIZE
        elif direction == "DOWN":
            snake_position[1] += BLOCK_SIZE
        elif direction == "LEFT":
            snake_position[0] -= BLOCK_SIZE
        elif direction == "RIGHT":
            snake_position[0] += BLOCK_SIZE

   # Check if the snake has hit a wall
        if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - BLOCK_SIZE or snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - BLOCK_SIZE:
            game_over()

        # Check if the snake has hit itself
        for block in snake_body[1:]:
            if snake_position == block:
                game_over()

        # Check if the snake has eaten the food
        if snake_position == food_position:
            # Play the sound effect
            eat_sound.play()

            food_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                             random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
            score += 1
        else:
            snake_body.pop(0)

        # Add the new block to the snake's body
        snake_body.append(snake_position[:])

        # Fill the background with white
        window.fill(BACKGROUND_COLOR)

        # Draw the game elements
        draw_snake(snake_body)
        draw_food(food_position)
        display_score(score)

        # Update the display
        pygame.display.update()

        # Control the game FPS
        fps_controller.tick(20)

# function to display the game over message and prompts the user to continue playing or quit
def game_over():
    # Display the game over message
    game_over_text = font.render("Game Over! Press 1 to try again or 2 to quit.", True, (0, 0, 0))
    window.blit(game_over_text, [SCREEN_WIDTH/2 - game_over_text.get_width()/2, SCREEN_HEIGHT/2 - game_over_text.get_height()/2])
    pygame.display.update()

    # Wait for the user to input a key
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Reset the game and continue playing
                    game_loop()
                elif event.key == pygame.K_2:
                    # Quit the game and exit
                    pygame.quit()
                    quit()

# Run the game loop
game_loop()
