import pygame
import time
import random
import asyncio # Required for web browsers

pygame.init()

# Colors and Screen (800x600 is better for web)
white, yellow, black, red, green, blue = (255, 255, 255), (255, 255, 102), (0, 0, 0), (213, 50, 80), (0, 255, 0), (50, 153, 213)
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width, dis_height))

snake_block, snake_speed = 20, 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_score(score):
    dis.blit(score_font.render("Score: " + str(score), True, yellow), [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# The main function must be 'async' for the website to work
async def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            mesg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, red)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
            our_score(Length_of_snake - 1)
            pygame.display.update()
            await asyncio.sleep(0) # IMPORTANT: Stops browser from freezing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: game_over, game_close = True, False
                    if event.key == pygame.K_c: await gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP: y1_change, y1_change = -snake_block, 0 # Error fix here
                elif event.key == pygame.K_DOWN: y1_change, x1_change = snake_block, 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_List.append([x1, y1])
        if len(snake_List) > Length_of_snake: del snake_List[0]
        our_snake(snake_block, snake_List)
        our_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        await asyncio.sleep(0) # IMPORTANT: Required for web
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

# This starts the game
asyncio.run(gameLoop())
