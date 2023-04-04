# This script will create a simple PONG game

# Import and initialize the pygame library
import pygame
import random

pygame.init()
pygame.font.get_fonts()
pygame.mixer.init()


# Global variable
pressed_keys = []
bat_hit = pygame.mixer.Sound("ball_hit.wav")
pygame.mixer.music.load("The_Matrix.wav")
pygame.mixer.music.play(-1)


# Set up the game screen
screen_width = 1000
screen_height = 1000
screen_colour = (0,0,0)
line_colour = (120,120,120)
ball_colour = (160,160,160)

# Dimensions of the pong
pong_width = 10
pong_height = 100

# Fixed rectangle restrictions for player 1
maximum_square_y = ((screen_height) - pong_height)
maximum_square_x = ((screen_width/4)- pong_width)
minimum_square_x = 0
minimum_square_y = 0
# Fixed rectangle restrictions for player 2
maximum_square2_y = ((screen_height) - pong_height)
maximum_square2_x = (screen_width- pong_width)
minimum_square2_x = (screen_width/4*3)
minimum_square2_y = 0

# Starting position of pong 1
square_x = minimum_square_x
square_y = (screen_height/2)-(pong_height/2)

# Starting position of pong 2
square2_x = maximum_square2_x
square2_y = (screen_height/2)-(pong_height/2)

# Starting position of the ball
ball_x = screen_width/2
ball_y = screen_height/2
ballsize = 10

# Move the ball. These two variables control the angle and the speed of the ball. 
move_x = -1
move_y = -1
move_speed = 4
speed_counter = 0

player1_count= 0
player2_count = 0
winner_text=None

font = pygame.font.SysFont('Arial',30)
font_pong = pygame.font.SysFont('Arial',40)
font_big = pygame.font.SysFont('Arial',50)
title = font_pong.render('PONG', True, (255,255,255),screen_colour)

font_p1_score = pygame.font.SysFont('Arial',20)
font_p2_score = pygame.font.SysFont('Arial',20)
screen = pygame.display.set_mode([screen_width, screen_height])

# Run until the user asks to quit
# -> Create a game loop that controls when the game ends
pause = False
running = True
while running:
    p1_title = font.render('Player 1', True, (255,255,255), screen_colour)
    p2_title = font.render('Player 2', True, (255,255,255), screen_colour)
    p1_score = font_big.render(str(player1_count), True, (255,255,255), screen_colour)
    p2_score = font_big.render(str(player2_count), True, (255,255,255), screen_colour)

    screen.fill(screen_colour)
    pygame.draw.line(screen,line_colour,(screen_width//2,0),(screen_width//2,screen_height),2)
    screen.blit(title,((screen_width//2)-title.get_rect().width//2,20))
    screen.blit(p1_title,((50,50)))
    screen.blit(p2_title,((screen_width-50- p2_title.get_rect().width,50)))
    screen.blit(p1_score,((50+p1_title.get_rect().width/2 - p1_score.get_rect().width/2, 50 + p1_title.get_rect().height)))
    screen.blit(p2_score,((screen_width-50 - p2_title.get_rect().width/2 - p2_score.get_rect().width/2, 50 + p2_title.get_rect().height)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pressed_keys.append(event.key)
            if pygame.K_v == event.key:
                move_speed = move_speed-1
                if move_speed <= 0:
                    move_speed = 1
            if pygame.K_b == event.key:
                move_speed = move_speed+1
        elif event.type == pygame.KEYUP and event.key in pressed_keys:
            pressed_keys.remove(event.key)

# Define the movement of object 1 (player bat 1)
    if pygame.K_UP in pressed_keys:
        square_y = square_y-1
        if square_y<=minimum_square_y:
            square_y=minimum_square_y     
    if pygame.K_DOWN in pressed_keys:
        square_y = square_y+1
        if square_y>maximum_square_y:
            square_y=maximum_square_y
    if pygame.K_LEFT in pressed_keys:
        square_x = square_x-1
        if square_x<=minimum_square_x:
            square_x=minimum_square_x
    if pygame.K_RIGHT in pressed_keys:
        square_x=square_x+1                      
        if square_x > maximum_square_x:
            square_x=maximum_square_x            

# Define the movement of object 2 (player bat 2)
    if pygame.K_w in pressed_keys:
        square2_y = square2_y-1
        if square2_y<=minimum_square2_y:
            square2_y=minimum_square2_y
    if pygame.K_s in pressed_keys:
        square2_y=square2_y+1
        if square2_y>maximum_square2_y:
            square2_y=maximum_square2_y
    if pygame.K_a in pressed_keys: 
        square2_x=square2_x-1               
        if square2_x <= minimum_square2_x: 
            square2_x=minimum_square2_x
    if pygame.K_d in pressed_keys:
        square2_x=square2_x+1
        if square2_x>maximum_square2_x:
            square2_x=maximum_square2_x

# Dedicate two keys (v,b) to changing the speed of the ball (move_speed)
    if square2_x<0:
        square2_x=screen_width
    elif square2_x>screen_width:
        square2_x=0
    elif square2_y<0:
        square2_y=screen_height  
    elif square2_y>screen_height:
        square2_y=0    

# Define the movement of the ball
    speed_counter = speed_counter+1
    if speed_counter >= move_speed:
        ball_x=ball_x+move_x
        ball_y=ball_y+move_y
        speed_counter = 0

        if ball_y <=0:
            ball_y=0
            move_y=-move_y
        if ball_y >= screen_height-1:
            ball_y=screen_height-1
            move_y=-move_y     # the new value of move_y will be reflected in ball_y+ball_y+move_y. This is how the ball knows where to go. 
        if ball_x <=0:
            ball_x=screen_width/2
            ball_y=screen_height/2
            move_x=-move_x 
            player2_count = player2_count+1
        if ball_x>= screen_width-1:
            ball_x=screen_width/2
            ball_y=screen_height/2
            move_x=-move_x
            player1_count = player1_count +1

# Change the direction of the ball if it hits a bat
        if ball_x <= square_x+pong_width and ball_x > square_x and ball_y >= square_y and ball_y <= square_y+pong_height:
            if ball_y > square_y + (pong_height/3):
              if move_y < 0:
                move_y = -2
              else:
                move_y = -move_y
            elif ball_y > square_y + (2* (pong_height/3)):
              move_y = move_x
            elif ball_y > square_y + pong_height:
                if move_y < 0:
                  move_y = -move_y
                else:
                  move_y = 2
            move_x = -move_x
            pygame.mixer.Sound.play(bat_hit)
        if ball_x >= square2_x and ball_x < square2_x + pong_width and ball_y >= square2_y and ball_y <= square2_y+pong_height:
            if ball_y > square2_y + (pong_height/3):
              if move_y < 0:
                move_y = -2
              else:
                move_y = -move_y
            elif ball_y > square2_y + (2* (pong_height/3)):
              move_y = move_x
            elif ball_y > square2_y + pong_height:
                if move_y < 0:
                  move_y = -move_y
                else:
                  move_y = 2
            move_x = -move_x
            pygame.mixer.Sound.play(bat_hit)

# Quit the game if the score exceeds 10
        if player1_count>=10:
            pause=True
            winner_text = font_big.render('Player 1 Wins!', True, (0,255,0), screen_colour)
            
        if player2_count>=10:
            pause=True
            winner_text = font_big.render('Player 2 Wins!', True, (255,0,0), screen_colour)
            
    # Draw a solid red rectangle 
    pygame.draw.rect(screen,(0,255,0),pygame.Rect(square_x,square_y,pong_width,pong_height))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(square2_x,square2_y,pong_width,pong_height))
 
    # Draw a ball
    pygame.draw.circle(screen,(ball_colour), (ball_x,ball_y),ballsize)
   
    # Flip the display
    # Update all of the content so far to the screen
    pygame.display.flip()
    
    # Create a pause in the game
    while pause:
        space_continue=font.render('Press Space to restart', True, (255,255,255), screen_colour)
        q_quit= font.render('Press Q to quit', True, (255,255,255), screen_colour)
        screen.blit(winner_text,((screen_width/2 - winner_text.get_rect().width/2,screen_height/2 - winner_text.get_rect().height/2 )))
        screen.blit(space_continue,((screen_width/2 - space_continue.get_rect().width/2,screen_height/2 + winner_text.get_rect().height/2 )))
        screen.blit(q_quit,((screen_width/2 - q_quit.get_rect().width/2,screen_height/2 + winner_text.get_rect().height/2 + space_continue.get_rect().height)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pause=False
            elif event.type == pygame.KEYDOWN:
                if pygame.K_SPACE == event.key:
                    # Starting position of pong 1
                    square_x = minimum_square_x
                    square_y = (screen_height/2)-(pong_height/2)

                    # Starting position of pong 2
                    square2_x = maximum_square2_x
                    square2_y = (screen_height/2)-(pong_height/2)

                    # Starting position of the ball
                    ball_x = screen_width/2
                    ball_y = screen_height/2

                    # Move the ball. These two variables control the angle and the speed of the ball. 
                    move_x = -1
                    move_y = -1
                    move_speed = 4
                    speed_counter = 0
                    player1_count= 0
                    player2_count = 0
                    pause=False
                    
                elif pygame.K_q == event.key:
                    running=False
                    pause=False
        
        pygame.display.flip()
            
# This will quit the game
pygame.quit()
