import pygame
import random
import time

# --- 1. Initialization ---
pygame.init()

# --- 2. Window and Color Settings ---
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python Snake Game')  # Window Title

# Define Colors (R, G, B)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game Parameters
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

# Font Settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    """Display current score"""
    value = score_font.render("Score: " + str(score), True, yellow)  # English text
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    """Draw the snake's body"""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Display messages (like Game Over)"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    """Main Game Loop"""
    game_over = False
    game_close = False

    # Snake initial position and direction
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_List = []
    Length_of_snake = 1

    # Food random position
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # --- 3. Main Loop ---
    while not game_over:

        # Game Over Screen
        while game_close == True:
            dis.fill(blue)
            # English text for Game Over message
            message("Game Over! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart game

        # --- 4. Event Handling (Movement Control) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # --- 5. Collision and Movement ---

        # Boundary Collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update snake head position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # Fill background

        # Draw food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Build new snake head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove snake tail (maintain movement)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self-collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake and score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # --- 6. Eating Food ---
        if x1 == foodx and y1 == foody:
            # Re-spawn food randomly
            while True:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                # Ensure new food is not on the snake
                if [foodx, foody] not in snake_List:
                    break

            Length_of_snake += 1  # Increase snake length

        clock.tick(snake_speed)  # Control game speed

    # --- 7. Quit Pygame ---
    pygame.quit()
    quit()


# Start Game
gameLoop()
