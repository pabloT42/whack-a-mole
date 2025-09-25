import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Whack-a-mole")
clock = pygame.time.Clock() 

font = pygame.font.SysFont(None, 48) #default font

#game variables------------------------------
circx = random.randrange(100,700)
circy = random.randrange(100,700)
red = random.randrange(20, 250)
green = random.randrange(20, 250)
blue = random.randrange(20, 250)
ticker = 0
drawn = True
score = 0
outline = False

hit = pygame.mixer.Sound("hit.wav")
miss = pygame.mixer.Sound("miss.mp3")
pygame.mixer.music.load("backgroundmus.mp3") #background music
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


running = True
while running: #game loop--------------------
    
    #input section---------------------------
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if event.type == pygame.MOUSEBUTTONDOWN and drawn: #check if mouse has been clicked and the circle has been drawn
        mx, my = pygame.mouse.get_pos() #get and store mouse position
        #use distance formula to check if weve clicked inside the circle:
        if(mx-circx)**2 + (my-circy)**2 <=50**2:
            if outline == False: #only add score once
                score += 1 #increment score
                print(score) #print score to console for testing
                hit.play()
            ticker = 0 #reset ticker to 0 so circle stays put for a second
            outline = True #set outline to true to show player has scored
        else:
            miss.play()
                
            
            
            
    #update section--------------------------
    ticker+=1 #increase ticker
    print(ticker) #temporary delete later
    if drawn and ticker > 50: #if circle is drawn and ticker runs out, stop drawing
        drawn = False
        outline = False
        ticker = 0
        circx = random.randrange(0,800)#new position for circx
        circy = random.randrange(0,800)#new position for circy
        red = random.randrange(20,250)#new color
        green = random.randrange(20,250)#new color
        blue = random.randrange(20,250)#new color
        
       
         
    elif drawn == False and ticker > 10: #if circle isnt there and ticker runs out, draw it
        drawn = True #drawn variable = true
        ticker = 0 #reset ticker to 0
        
        
        
            
    #draw section----------------------------
    screen.fill((20,20,20))
    
    if drawn == True:
        pygame.draw.circle(screen, (red,green,blue), (circx, circy), 50)
    if outline:
        pygame.draw.circle(screen, (255,255,255), (circx, circy), 50, 3)
        
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, (20,20))
        
    pygame.display.flip()
    
    
pygame.quit()
