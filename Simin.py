import pygame
import random
import math
import winsound

pygame.init()
pygame.display.set_caption("Simon")
screen = pygame.display.set_mode((800, 800))

ypos = 0
xpos = 0
mousePos = (xpos, ypos)
hasClocked = False
pattern = []
playerPattern = []
playerTurn = True
pi = math.pi
ded = False
playerPattern = [0, 0, 0, 0]

def collision(xpos, ypos):
        if math.sqrt((xpos - 400)**2 + (ypos - 400)**2) < 200 or math.sqrt((xpos - 400)**2 + (ypos - 400)**2 )> 100:
      
            if xpos < 400 and ypos < 400:
                #print("over red button")
                pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), pi / 2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
                
                return 0
            elif xpos < 400 and ypos > 400:
                #print ( "over green button")
                pygame.draw.arc(screen, (0,255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
                pygame.display.flip()
                winsound.Beep(500, 500)
                return 1
            elif xpos > 400 and ypos < 400:
                #print("over blue button")
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 0, (pi / 2),  100)
                pygame.display.flip()
                winsound.Beep(700, 500)
                return 2
            elif xpos > 400 and ypos > 400:
                #print ( "over yellow button")
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3* pi /2),0,  100)
                pygame.display.flip()
                winsound.Beep(650, 500)
                return 3
        else:
            print("outside of ring")

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            hasClicked = True
            print("Click")
        if event.type == pygame.MOUSEBUTTONUP:
            hasClicked = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos



    #physics
    collision(mousePos[0], mousePos[1])

    playerPattern.append(collision(mousePos[0], mousePos[1]))
    print(playerPattern)

        #update section
    print("Starting players turn")
    if playerTurn == True:
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
        else:
            playerTurn = False
            pygame.time.wait(800)
    if playerTurn == False:
        print("Starting Machines turn")
        pattern.append(random.randrange(0, 2))

    #play computer pattern
        for i in range(len(pattern)):
            if pattern[i] == 0: #RED
                #briefly draws brighter color
                pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), pi / 2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
            if pattern[i] == 1: #GREEN
                #briefly draws brighter color
                pygame.draw.arc(screen, (0,255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
                pygame.display.flip()
                winsound.Beep(500, 500)
            if pattern[i] == 0: #YELLOW
                #briefly draws brighter color
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3* pi /2),0,  100)
                pygame.display.flip()
                winsound.Beep(650, 500)
            if pattern[i] == 0: #BLUE
                #briefly draws brighter color
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 0, (pi / 2),  100)
                pygame.display.flip()
                winsound.Beep(700, 500)


        pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), pi / 2, pi, 100)
        pygame.draw.arc(screen, (0,155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
        pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3* pi /2),0,  100)
        pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 0, (pi / 2),  100)
        pygame.display.flip()
        playerTurn = True
        playerPattern.clear
    

pygame.quit()