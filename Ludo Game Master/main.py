from pygame.locals import *
from main_board import *
from Pawns import *
from Players import *
from States import *
import pygame

# Pygame Initialized
pygame.init()

# window dimension coordinates in pixels
winX = 800
winY = 800

# set and initialize the pygame display
win = pygame.display.set_mode((winX, winY))

#load the board background
bgBoard = pygame.image.load('img/LudoBoard-01.png')

# MainFunction
def main():
    # main Objects
    #Initialize statekeeper object
    Statekpr = Statekeep()    
    #Inititalize clock
    clock = pygame.time.Clock()   
    # for each player in the players list
    for player in Statekpr.players:
        #pass the statekeeper object to the players
        player.set_statekeeper(Statekpr)
    #Set while loop variable
    mainLoop = True
    #main game loop
    while mainLoop:
        #Draw board
        win.blit(bgBoard, (0,0))
        #Set clock Tick
        clock.tick(30)
        #update status keeper with every iteration of the main loop
        Statekpr.update()       
        #Set event logic
        for event in pygame.event.get():
            #set basic Quit
            if event.type == QUIT:
                mainLoop = False
            #check for key presses
            if event.type == KEYDOWN:
                #set Escape Key quit
                if event.key == K_ESCAPE:
                    mainLoop = False
                # set Space key press
                if event.key == K_SPACE:
                    #Check if game is started and set necessary variables if not
                    if not Statekpr.gamestart:
                        #modify necessary state variables to start game
                        Statekpr.start_game()
                    #attempt to move the active player (if a player is active) otherwise just roll dice to try to start
                    Statekpr.move_player()
            
            #I'm not sure what this is for but im not gonna mess with it.
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pass
       
        #draw everything and refresh the screen
        for entity in allSprites:
            win.blit(entity.surf, entity.rect)
        pygame.display.flip()

# if this is the main python script, run the main() function
if __name__ == '__main__':
    main()