import pygame
import time
import random
import asyncio

pygame.init()

white, yellow, black, red, green = (255, 255, 255), (255, 255, 102), (0, 0, 0), (213, 50, 80), (0, 255, 0)
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

async def gameLoop():
    game_over = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - 20) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - 20) / 20.0) * 20.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -20, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = 20, 0
                elif event.key == pygame.K_UP: x1_change, y1_change = 0, -20
                elif event.key == pygame.K_DOWN: x1_change, y1_change = 0, 20

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, 20, 20])
        
        snake_List.append([x1, y1])
        if len(snake_List) > Length_of_snake: del snake_List[0]
        for x in snake_List:
            pygame.draw.rect(dis, green, [x[0], x[1], 20, 20])

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - 20) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - 20) / 20.0) * 20.0
            Length_of_snake += 1

        pygame.display.update()
        # THIS IS THE MOST IMPORTANT LINE FOR THE WEB:
        await asyncio.sleep(0) 
        clock.tick(15)

    pygame.quit()

# Run the game
asyncio.run(gameLoop())
