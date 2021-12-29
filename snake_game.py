import pygame
import time
import random
import datetime
import time
def gameStart(speed):
    print(speed)
    pygame.init()
    bgsongs=["sgs1.mp3","sgs2.mp3","sgs3.mp3","sgs4.mp3","sgs5.mp3","sgs6.mp3","sgs7.mp3","sgs8.mp3","sgs10.mp3"]
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dis_width = 1200
    dis_height = 700
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by IPA')
    clock = pygame.time.Clock()
    snake_block = 25
    snake_speed = speed
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("arial", 35)
    with open("highestscore.txt", "r") as f:
        hiscore = f.read()
    pygame.mixer.music.load(random.choice(bgsongs))
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    def Your_score(score,hiscore):
        value = score_font.render("Your Score: " + str(score)+"  Highest score : "+ str(hiscore), True, yellow)
        dis.blit(value, [0, 0])
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
    def gameLoop():
        with open("highestscore.txt", "r") as f:
            hiscore = f.read()
        game_over = False
        game_close = False
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_List = []
        Length_of_snake = 1
        foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
        foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
        while not game_over:
            while game_close == True:
                dis.fill(black)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                pygame.mixer.music.stop()
                score=(Length_of_snake - 1)*10
                if score > int(hiscore):
                    hiscore = score
                    with open("highestscore.txt", "w") as f:
                        f.write(str(hiscore))
                Your_score((Length_of_snake - 1)*10,hiscore)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            pygame.mixer.music.load(random.choice(bgsongs))
                            pygame.mixer.music.set_volume(0.8)
                            pygame.mixer.music.play(-1)
                            gameLoop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(black)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block, snake_List)
            score = (Length_of_snake - 1) * 10
            if score > int(hiscore):
                hiscore = score
                with open("highestscore.txt","w") as f:
                  f.write(str(hiscore))
            Your_score((Length_of_snake - 1)*10,hiscore)


            pygame.display.update()
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
                foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
                Length_of_snake += 1
            clock.tick(snake_speed+10)
        pygame.quit()
        f.close()
        f = open("scorecard.txt", "a")
        f.write(f"\nYOUR LAST SCORE IS : {(Length_of_snake - 1) * 10} , AT {datetime.datetime.now()}\n")
        f.close()
        quit()
    gameLoop()
    time.sleep(30)