# This script will create a simple PONG game using classes

import pygame as py

py.init()
py.mixer.init()
py.mixer.init()

# Set up the game screen
screen_width = 1800
screen_height = 1000
screen_colour = (3,37,126)

bat_hit = py.mixer.Sound("ball_hit.wav")
py.mixer.music.load("ace_ventura.wav")
py.mixer.music.play(-1)

pong_width = 20
pong_height =200

ball_radius = 10

ball_move = [-1, -1]
ball_2_move = [1,1]

pressed_keys = []
line_colour = (120,120,120)
ball_colour = (160,160,160)
ball_colour_2 = (255,0,0)

p1_count = 0
p2_count = 0
winner_text = None

font = py.font.SysFont('Arial',30)
font_pong = py.font.SysFont('Arial',40)
font_big = py.font.SysFont('Arial',50)
title = font_pong.render('PONG', True, (255,255,255),screen_colour)

font_p1_score = py.font.SysFont('Arial',20)
font_p2_score = py.font.SysFont('Arial',20)
screen = py.display.set_mode([screen_width, screen_height])

class Bat:
    def __init__(self,height,width,colour,x,y):
        self.height = height
        self.width = width
        self.colour = colour
        self.x = x
        self.y = y
    
    def set_restriction(self,x,y,height,width):
        self.rest_x = x
        self.rest_y = y
        self.rest_height = height
        self.rest_width = width
    
    def move_by(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
        if self.x <= self.rest_x:
            self.x = self.rest_x
        if self.x + self.width >= self.rest_x + self.rest_width:
            self.x = self.rest_x + self.rest_width - self.width
        if self.y <= self.rest_y:
            self.y = self.rest_y
        if self.y + self.height >= self.rest_y + self.rest_height:
            self.y = self.rest_y + self.rest_height - self.height
    
    def hit(self,ball):
        if ball.get_bat_hit() != self:
            if ball.x <= self.x+self.width and ball.x>self.x and ball.y>=self.y and ball.y<=self.y +self.height:
                py.mixer.Sound.play(bat_hit)
                if ball.y<self.y+self.height/3:
                    return 1
                elif ball.y<self.y+(2*(self.height/3)):
                    return 2
                elif ball.y < self.y+self.height:
                    return 3
        return 0
    
    def reset_pos(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        py.draw.rect(screen,self.colour,py.Rect(self.x,self.y,self.width,self.height))
        py.draw.rect(screen,self.colour,py.Rect(self.x,self.y,self.width,self.height))

    def update_last_pos(self):
        self.last_x = self.x
        self.last_y = self.y
    
    def direction(self):
        vec = [self.last_x - self.x, self.last_y - self.y]
        return vec

class Ball:
    def __init__(self,x,y,radius,colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.last_hit = None
    
    def draw(self):
        py.draw.circle(screen,(self.colour),(self.x,self.y),self.radius)
    
    def move(self, vec):
        self.x = self.x + vec[0]
        self.y = self.y + vec[1]
        if self.x <= 0:
            self.x = 0
            vec[0] = -vec[0]
        if self.x >= screen_width - 1:
            self.x = screen_width - 1
            vec[0] = -vec[0]
        if self.y <= 0:
            self.y = 0
            vec[1] = -vec[1]
        if self.y >= screen_height - 1:
            self.y = screen_height - 1
            vec[1] = -vec[1]
        return vec
     
    def score(self):
        if self.x >= screen_width - 1:
            return 1
        if self.x <= 0:
            return 2
        return 0
    
    def reset_pos(self,x,y):
        self.x = x
        self.y = y
        self.last_hit = None
    
    # Tell the ball which bat hit it 
    def set_bat_hit(self,which_bat):
        self.last_hit = which_bat
    
    # Ask the ball which bat hit it
    def get_bat_hit(self):           
        return self.last_hit

bat_1 = Bat(pong_height,pong_width,(255,255,255),0,(screen_height/2)-(pong_height/2))
bat_1.set_restriction(0,0,screen_height,screen_width/4)
bat_2 = Bat(pong_height,pong_width,(255,255,255),(screen_width-pong_width),(screen_height/2)-(pong_height/2))
bat_2.set_restriction(screen_width/4*3,0,screen_height,screen_width/4)
ball = Ball(screen_width/2,screen_height/2,ball_radius,ball_colour)
ball_2 = Ball(screen_width/2,screen_height/2,ball_radius,ball_colour_2)

pause = False
running = True

while running:
    p1_title = font.render('Player 1', True, (255,255,255), screen_colour)
    p2_title = font.render('Player 2', True, (255,255,255), screen_colour)
    p1_score = font_big.render(str(p1_count), True, (255,255,255), screen_colour)
    p2_score = font_big.render(str(p2_count), True, (255,255,255), screen_colour)

    screen.fill(screen_colour)
    py.draw.line(screen,line_colour,(screen_width//2,0),(screen_width//2,screen_height),2)
    screen.blit(title,((screen_width//2)-title.get_rect().width//2,20))
    screen.blit(p1_title,((50,50)))
    screen.blit(p2_title,((screen_width-50- p2_title.get_rect().width,50)))
    screen.blit(p1_score,((50+p1_title.get_rect().width/2 - p1_score.get_rect().width/2, 50 + p1_title.get_rect().height)))
    screen.blit(p2_score,((screen_width-50 - p2_title.get_rect().width/2 - p2_score.get_rect().width/2, 50 + p2_title.get_rect().height)))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            pressed_keys.append(event.key)
        elif event.type == py.KEYUP and event.key in pressed_keys:
            pressed_keys.remove(event.key)

# Define the movement of object 1 (player bat 1)
    bat_1.update_last_pos()
    if py.K_UP in pressed_keys:
        bat_1.move_by(0,-2)
    if py.K_DOWN in pressed_keys:
        bat_1.move_by(0,2)
    if py.K_LEFT in pressed_keys:
        bat_1.move_by(-2,0)
    if py.K_RIGHT in pressed_keys:
        bat_1.move_by(2,0)        

# Define the movement of object 2 (player bat 2)
    bat_2.update_last_pos()
    if py.K_w in pressed_keys:
        bat_2.move_by(0,-2)
    if py.K_s in pressed_keys:
        bat_2.move_by(0,2)
    if py.K_a in pressed_keys: 
        bat_2.move_by(-2,0)
    if py.K_d in pressed_keys:
        bat_2.move_by(2,0)

# Define the movement of the ball
    ball_move = ball.move(ball_move)
    if ball.score() != 0:
        if ball.score() == 1:
            p1_count = p1_count + 1
        if ball.score() == 2:
            p2_count = p2_count + 1
        ball.reset_pos(screen_width/2,screen_height/2)
        if (p1_count+p2_count)%2 == 0:
            ball_move[0] = -1
        else:
            ball_move[0] = 1

    if bat_1.hit(ball) != 0:
        if ball_move[1] < 0:
            if bat_1.hit(ball) == 1:
                ball_move[1] = -2
            elif bat_1.hit(ball) == 2:
                ball_move[1] = -1
            elif bat_1.hit(ball) == 3:
                ball_move[1] = -ball_move[1]
        else:
            if bat_1.hit(ball) == 1:
                ball_move[1] = -ball_move[1]
            elif bat_1.hit(ball) == 2:
                ball_move[1] = 1
            elif bat_1.hit(ball) == 3:
                ball_move[1] = 2
        ball.set_bat_hit(bat_1)
        if bat_1.direction()[0] > 0:
            ball_move[0] = ball_move[0] - 1
        elif bat_1.direction()[0] < 0:
            ball_move[0] = ball_move[0] + 1
        if ball_move[0] == 0:
            ball_move[0] = -1
        ball_move[0] = -ball_move[0]
    if bat_2.hit(ball) != 0:
        if ball_move[1] < 0:
            if bat_2.hit(ball) == 1:
                ball_move[1] = -2
            elif bat_2.hit(ball) == 2:
                ball_move[1] = -1
            elif bat_2.hit(ball) == 3:
                ball_move[1] = -ball_move[1]
        else:
            if bat_2.hit(ball) == 1:
                ball_move[1] = -ball_move[1]
            elif bat_2.hit(ball) == 2:
                ball_move[1] = 1
            elif bat_2.hit(ball) == 3:
                ball_move[1] = 2
        ball.set_bat_hit(bat_2)
        if bat_2.direction()[0] > 0:
            ball_move[0] = ball_move[0] + 1
        elif bat_2.direction()[0] < 0:
            ball_move[0] = ball_move[0] - 1
        if ball_move[0] == 0:
            ball_move[0] = 1
        ball_move[0] = -ball_move[0]
    
    #ball_2_move = ball_2.move(ball_2_move)
    if ball_2.score() == 1:
        p1_count = p1_count + 1
    if ball_2.score() == 2:
        p2_count = p2_count + 1
        
    if bat_1.hit(ball_2) != 0:
        ball_2.set_bat_hit(bat_1)
        ball_2_move[0] = -ball_2_move[0]
    if bat_2.hit(ball_2) != 0:
        ball_2.set_bat_hit(bat_2)
        ball_2_move[0] = -ball_2_move[0]
    
    bat_1.draw() 
    bat_2.draw()
    ball.draw()
    #ball_2.draw()
    
# Quit the game if the score exceeds 10
    if p1_count >= 7:
        pause = True
        winner_text = font_big.render('Player 1 Wins!', True, (0,255,0), screen_colour)
    
    if p2_count >= 7:
        pause = True
        winner_text = font_big.render('Player 2 Wins!', True, (0,255,0), screen_colour)
                    
    py.display.flip()

    while pause:
        space_continue=font.render('Press Space to restart', True, (255,255,255), screen_colour)
        q_quit= font.render('Press Q to quit', True, (255,255,255), screen_colour)
        screen.blit(winner_text,((screen_width/2 - winner_text.get_rect().width/2,screen_height/2 - winner_text.get_rect().height/2 )))
        screen.blit(space_continue,((screen_width/2 - space_continue.get_rect().width/2,screen_height/2 + winner_text.get_rect().height/2 )))
        screen.blit(q_quit,((screen_width/2 - q_quit.get_rect().width/2,screen_height/2 + winner_text.get_rect().height/2 + space_continue.get_rect().height)))
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                pause=False
            elif event.type == py.KEYDOWN:
                if py.K_SPACE == event.key:
                    pressed_keys.clear()
                    # Starting position of bat 1 and bat 2
                    bat_1.reset_pos(0,(screen_height/2)-(pong_height/2))
                    bat_2.reset_pos(screen_width-pong_width,(screen_height/2)-(pong_height/2))
                    # Starting position of the ball
                    ball.reset_pos(screen_width/2,screen_height/2)
                    ball_2.reset_pos(screen_width/2,screen_height/2)
                    # Move the ball
                    ball_move = [-1,-1]
                    ball_2_move = [1,1]
                    p1_count = 0
                    p2_count= 0
                    pause = False
                elif py.K_q == event.key:
                    running = False
                    pause = False
        
        py.display.flip()

py.quit()