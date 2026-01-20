import pygame
import time
import random

pygame.init()

# Game Settings
white, yellow, black, red, green, blue = (255, 255, 255), (255, 255, 102), (0, 0, 0), (213, 50, 80), (0, 255, 0), (50, 153, 213)
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width, dis_height))

snake_block, snake_speed = 20, 15
font_style = pygame.font.SysFont("bahnschrift", 25)

def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP: x1_change, y1_change = 0, -snake_block
                elif event.key == pygame.K_DOWN: x1_change, y1_change = 0, snake_block

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: del snake_List[0]

        for x in snake_List:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
