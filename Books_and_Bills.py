import pygame
import time
import random
import numpy as np

pygame.init()

display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0) 
yellow = (255,255,0)
blue = (0,0,255)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Books & Bills')
clock = pygame.time.Clock()

Img1 = pygame.image.load('student1_copy.png') # Dimensions 100 x 100
Img2 = pygame.image.load('books1_copy.png') # Dimensions 100 x 100
Img3 = pygame.image.load('bills1_copy.png') # Dimensions 100 x 100
Img4 = pygame.image.load('impact1.png') # Dimensions 75 x 75
Img5 = pygame.image.load('bulb1.png') # Dimensions 125 x 75
Img6 = pygame.image.load('dragon2.png') # Dimensions 125 x 175
Img7 = pygame.image.load('student2.png') # Dimensions 100 x 100

gameIcon = pygame.image.load('student2.png')
pygame.display.set_icon(gameIcon)

dim1x = 120 # Object (Student) width
dim1y = 90

dim2x = 120
dim2y = 120

dim3x = 120
dim3y = 120

pause = False

def text_objects1(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def text_objects3(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def books_collide(x,y):
    
    gameDisplay.blit(Img5,(x,y))

def button(msg,x,y,w,h,ic,ac,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("chalkduster",25)
    textSurf, textRect = text_objects1(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def bills_collide(x,y):

    
    largeText = pygame.font.SysFont("chalkduster",115)
    TextSurf, TextRect = text_objects3("Game Over!!!", largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    
    gameDisplay.blit(Img4,(x,y))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again?",280,350,200,100,green,bright_green,game_loop)
        button("Quit",780,350,200,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def books_read(count):
    font = pygame.font.SysFont("chalkduster", 28)
    text = font.render("Books Read: "+str(count), True, green)
    gameDisplay.blit(text,(40,0))

def bills_dodged(count):
    font = pygame.font.SysFont("chalkduster", 28)
    text = font.render("Bills Dodged: "+str(count), True, green)
    gameDisplay.blit(text,(315,0))


def books_missed(count):
    font = pygame.font.SysFont("chalkduster", 28)
    text = font.render("Books Missed: "+str(count), True, green)
    gameDisplay.blit(text,(615,0))


def net_score(count):
    font = pygame.font.SysFont("chalkduster", 75)
    text = font.render("Net score: "+str(count), True, yellow)
    gameDisplay.blit(text,(355,50))    


def chances_left(count):
    font = pygame.font.SysFont("chalkduster", 28)
    text = font.render("Chances Left: "+str(3-count), True, red)
    gameDisplay.blit(text,(915,0))
    

def student(x,y):
    gameDisplay.blit(Img1,(x,y))

def books(x,y):
    gameDisplay.blit(Img2,(x,y))

def bills(x,y):
    gameDisplay.blit(Img3,(x,y))

def background():
    gameDisplay.blit(bg,(0,0))


def boundary_warning():

    largeText = pygame.font.SysFont('chalkduster',55)
    TextSurf, TextRect = text_objects3("Beyond here be dragons", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    gameDisplay.blit(Img6,((display_width/2),(display_height/2)))

    pygame.display.update()
    clock.tick(15)
    
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    
    largeText = pygame.font.SysFont("chalkduster",115)
    TextSurf, TextRect = text_objects1("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",280,350,200,100,green,bright_green,unpause)
        button("Quit",780,350,200,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)    




def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        largeText = pygame.font.SysFont("chalkduster",115)
        smallText = pygame.font.SysFont("chalkduster",25)
        TextSurf, TextRect = text_objects2("Books & Bills", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf2, TextRect2 = text_objects1("As a poor grad student, your needs are simple.",smallText)
        TextRect2.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf2,TextRect2)

        TextSurf3, TextRect3 = text_objects1("Avoid the bills, but don't miss out on the knowledge!",smallText)
        TextRect3.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf3,TextRect3)

        TextSurf4, TextRect4 = text_objects3("P.S. Stay away from the edges. Things might get strange!",smallText)
        TextRect4.center = ((display_width/2),(display_height-100))
        gameDisplay.blit(TextSurf4,TextRect4)

        button("Play!",280,350,200,100,green,bright_green,game_loop)
        button("Quit",780,350,200,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

    
def game_loop():
        
    global pause
  
    x_1 = (display_width * 0.45)
    y_1 = (display_height * 0.75)

    x_2 = random.randrange(300,display_width-300)
    y_2 = -200

    x1_change = 0

    x_3 = x_2 + dim2x  # Make sure bills and books don't overlap
    if x_3 < 0:
        x_3 = x_3 + display_width
    elif x_3 > display_width:
        x_3 = x_3 - display_width
    y_3 = -100
 
    
    y2_change = 5 # Speed of the books
    y3_change = 5 # Speed of the bills
 
    read_books = 0
    dodged_bills = 0
    missed_books = 0
    total_score = 0
    hit_count = 0
    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -20
                if event.key == pygame.K_RIGHT:
                    x1_change = 20
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x1_change = 0

        x_1 += x1_change
        y_2 += y2_change
        y_3 += y3_change


        gameDisplay.fill(black)
         
        student(x_1,y_1)
        
        books_missed(missed_books)

        bills_dodged(dodged_bills)

        chances_left(hit_count)

        books(x_2,y_2)

        bills(x_3,y_3)
    
        
        
        if x_1 > display_width - dim1x or x_1 < 0:
            boundary_warning()
            
            

        if y_2 > display_height:
           y_2 = 0-dim2y
           x_2 = random.randrange(0,display_width)

           missed_books +=1 

           y2_change = y2_change + 0.2*missed_books # Increase the speed of books


        if y_3 > display_height:
           y_3 = 0-dim3y
           x_3 = random.randrange(0,display_width)

           dodged_bills += 1

           y3_change = y3_change + 0.05*dodged_bills # Increase the speed of bills

           
       

     # For collision with books

        if y_1 < y_2 + dim2y:
 

            if (x_1 >= x_2 and x_1 < x_2 + dim2x) or (x_1 + dim1x >= x_2 and x_1 + dim1x < x_2 + dim2x):

                 gameDisplay.blit(Img5,(x_2,y_2))
                 y_2 = 0-dim2y
                 x_2 = random.randrange(0,display_width)
                 read_books += 1
                 
                 books_collide(x_2,y_2)

                 
        books_read(read_books)

        total_score = dodged_bills + read_books - missed_books

        net_score(total_score)
      

     # For collision with bills

        if y_1 < y_3+dim3y-5:

            if (x_1 > x_3 and x_1 < x_3 + dim3x - 5) or (x_1 + dim1x > x_3 and x_1 + dim1x < x_3 + dim3x - 5):

                hit_count += 1
                if hit_count < 3:
                    gameDisplay.blit(Img4,(x_3,y_3))
                    y_3 = 0-dim3y
                    x_3 = random.randrange(0,display_width)
                     
                else:                   
                     bills_collide(x_3,y_3)

        
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
