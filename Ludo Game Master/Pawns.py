import pygame
from pygame.locals import *
from Players import *
import time

# Pawn Constructor
class Pawn(pygame.sprite.Sprite):
    def __init__(self, surf, dict, startpos, number):
        super(Pawn, self).__init__()
        self.surf = surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # counter attribute
        self.counter = 1
        self.dict = dict
        # represents which pawn this is
        self.number = number
        self.startpos = startpos
        self.rect = self.surf.get_rect(center=self.startpos)
        # represents the pawns active status
        self.activepawn = False
        # is the pawn a king? not fully implemented yet
        self.king = False
        self.kingPawn = 0
        #if this object is the first pawn of the player it belongs to, then it is set to be the active pawn upon object initialization
        if self.number == 1:
            self.activepawn = True

    #pawn movement method
    def move(self, dice, statekeeper):   
        StateKpr = statekeeper
        # add the dice roll value to the pawn's counter
        self.counter += dice
        if self.counter == 52:
            print('PawnKing')
            self.kingPawn += 1
            #pawn state is set to inactive
            self.activepawn = False
            #this attribute is not fully implemented
            self.king = True
        elif self.counter > 52:
            self.counter -= dice
        self.rect.center = self.dict[self.counter]  
        #ensure the statuskeeper is current
        StateKpr.reset_counterlist_status()
        
    #update the pawn status variables to represent the current status of the pawns.
    def update_pawn_state(self, activeplayer, nextplayer):        
        ActPlayer = activeplayer
        NxtPlayer = nextplayer      
        #check which pawn this object instance refers to because it is made active by the player move method by calling this method
        if self.number == 1:
            #change the next pawn to active (Note: the index starts at 0 so index 1 is the second pawn)
            ActPlayer.pawnlist[1].activepawn = True
            # set the pawn of the next player to active 
            self.set_next_player_pawn(NxtPlayer)
        elif self.number == 2:
            ActPlayer.pawnlist[2].activepawn = True
            self.set_next_player_pawn(NxtPlayer)
        elif self.number == 3:
            ActPlayer.pawnlist[3].activepawn = True
            self.set_next_player_pawn(NxtPlayer)
        elif self.number == 4:
            ActPlayer.pawnlist[0].activepawn = True
            self.set_next_player_pawn(NxtPlayer)
            
    #determine and set the pawn status of the next player in preperation for their turn           
    def set_next_player_pawn(self, nextplayer):
        # for the pawns belonging to the next player
        for pawn in nextplayer.pawnlist:            
            #find active Pawn            
            if pawn.activepawn:
                #deactivate it
                pawn.activepawn = False
                #identify pawn that was deactivated
                if pawn.number == 1:                 
                    #activate the next pawn to be active
                    nextplayer.pawnlist[1].activepawn = True
                elif pawn.number == 2:               
                    nextplayer.pawnlist[2].activepawn = True
                elif pawn.number == 3:
                    nextplayer.pawnlist[3].activepawn = True
                elif pawn.number == 4:              
                    nextplayer.pawnlist[0].activepawn = True
                #loop can stop because the next player pawn is set because the active pawn was found
                break
            #else keep looping until active pawn is found
            else:
                continue
            
    

# ALL GROUPS OF SPRITES
redPawn = pygame.sprite.Group()
bluePawn = pygame.sprite.Group()
yellowPawn = pygame.sprite.Group()
greenPawn = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

# RED PAWNS
redDICT = {1: (124, 346), 2: (177, 346), 3: (230, 346), 4: (283, 346), 5: (335, 334), 6: (346, 283),
           7: (346, 230), 8: (346, 177), 9: (346, 124), 10: (346, 71), 11: (400, 71), 12: (453, 71), 13: (453, 124),
           14: (453, 177), 15: (453, 230), 16: (453, 283), 17: (467, 333), 18: (516, 346), 19: (570, 346),
           20: (622, 346), 21: (675, 346), 22: (728, 346), 23: (728, 400), 24: (728, 453), 25: (675, 453),
           26: (622, 453), 27: (570, 453), 28: (516, 453), 29: (467, 466), 30: (453, 516), 31: (453, 570),
           32: (453, 622), 33: (453, 675), 34: (453, 728), 35: (400, 728), 36: (346, 728), 37: (346, 675),
           38: (346, 622), 39: (346, 570), 40: (346, 516), 41: (333, 466), 42: (283, 453), 43: (230, 453),
           44: (177, 453), 45: (124, 453), 46: (71, 453), 47: (71, 400), 48: (124, 400), 49: (177, 400),
           50: (230, 400), 51: (283, 400), 52: (333, 400), }
# PNG
redpng = pygame.image.load('img/RedPawn.png')

redp1 = Pawn(redpng, redDICT, (142, 219), 1)
redp2 = Pawn(redpng, redDICT, (143, 142), 2)
redp3 = Pawn(redpng, redDICT, (219, 142), 3)
redp4 = Pawn(redpng, redDICT, (219, 219), 4)

RedPawnList = [redp1, redp2, redp3, redp4]
for rp in RedPawnList:
    allSprites.add(rp)
    redPawn.add(rp)
print(len(redPawn))

# BLUE PAWNS
blueDICT = {1: (453, 124),
            2: (453, 177), 3: (453, 230), 4: (453, 283), 5: (467, 333), 6: (516, 346), 7: (570, 346),
            8: (622, 346), 9: (675, 346), 10: (728, 346), 11: (728, 400), 12: (728, 453), 13: (675, 453),
            14: (622, 453), 15: (570, 453), 16: (516, 453), 17: (467, 466), 18: (453, 516), 19: (453, 570),
            20: (453, 622), 21: (453, 675), 22: (453, 728), 23: (400, 728), 24: (346, 728), 25: (346, 675),
            26: (346, 622), 27: (346, 570), 28: (346, 516), 29: (333, 466), 30: (283, 453), 31: (230, 453),
            32: (177, 453), 33: (124, 453), 34: (71, 453), 35: (71, 400), 36: (71, 346), 37: (124, 346),
            38: (177, 346), 39: (230, 346), 40: (283, 346), 41: (335, 334), 42: (346, 283), 43: (346, 230),
            44: (346, 177), 45: (346, 124), 46: (346, 71), 47: (400, 71), 48: (400, 124), 49: (400, 177),
            50: (400, 230), 51: (400, 283), 52: (400, 330), }

# PNG
bluepng = pygame.image.load('img/bluePawn.png')

bluep1 = Pawn(bluepng, blueDICT, (576, 142), 1)
bluep2 = Pawn(bluepng, blueDICT, (652, 142), 2)
bluep3 = Pawn(bluepng, blueDICT, (652, 219), 3)
bluep4 = Pawn(bluepng, blueDICT, (576, 219), 4)

BluePawnList = [bluep1, bluep2, bluep3, bluep4]
for rp in BluePawnList:
    allSprites.add(rp)
    bluePawn.add(rp)
print(len(bluePawn))

# YELLOW PAWNS
yellowDICT = {1: (675, 453), 2: (622, 453), 3: (570, 453), 4: (516, 453), 5: (467, 466), 6: (453, 516), 7: (453, 570),
              8: (453, 622), 9: (453, 675),10: (453, 728), 11: (400, 728), 12: (346, 728), 13: (346, 675),
              14: (346, 622), 15: (346, 570), 16: (346, 516), 17: (333, 466), 18: (283, 453), 19: (230, 453),
              20: (177, 453), 21: (124, 453), 22: (71, 453), 23: (71, 400), 24: (71, 346), 25: (124, 346),
              26: (177, 346), 27: (230, 346), 28: (283, 346), 29: (335, 334), 30: (346, 283), 31: (346, 230),
              32: (346, 177), 33: (346, 124), 34: (346, 71), 35: (400, 71), 36: (453, 71), 37: (453, 124), 38: (453, 177),
              39: (453, 230), 40: (453, 283), 41: (467, 333), 42: (516, 346), 43: (570, 346), 44: (622, 346),45: (675, 346),
              46: (728, 340), 47: (728, 400), 48: (675, 400), 49: (622, 400), 50: (570, 400), 51: (516, 400), 52: (466, 400)}

# PNG
yellowpng = pygame.image.load('img/yellowPawn.png')

yellowp1 = Pawn(yellowpng, yellowDICT, (652, 578), 1)
yellowp2 = Pawn(yellowpng, yellowDICT, (652, 655), 2)
yellowp3 = Pawn(yellowpng, yellowDICT, (577, 655), 3)
yellowp4 = Pawn(yellowpng, yellowDICT, (576, 578), 4)

YellowPawnList = [yellowp1, yellowp2, yellowp3, yellowp4]
for rp in YellowPawnList:
    allSprites.add(rp)
    yellowPawn.add(rp)
print(len(yellowPawn))

# GREEN PAWNS
greenDICT = { 1: (346, 675), 2: (346, 622), 3: (346, 570), 4: (346, 516), 5: (333, 466), 6: (283, 453), 7: (230, 453),
              8: (177, 453), 9: (124, 453), 10: (71, 453), 11: (71, 400), 12: (71, 346), 13: (124, 346),
              14: (177, 346), 15: (230, 346), 16: (283, 346), 17: (335, 334), 18: (346, 283), 19: (346, 230),
              20: (346, 177), 21: (346, 124), 22: (346, 71), 23: (400, 71), 24: (453, 71), 25: (453, 124), 26: (453, 177),
              27: (453, 230), 28: (453, 283), 29: (467, 333), 30: (516, 346), 31: (570, 346), 32: (622, 346), 33: (675, 346),
              34: (728, 346), 35: (728, 400), 36: (728, 453), 37: (675, 453), 38: (622, 453), 39: (570, 453), 40: (516, 453),
              41: (467, 466), 42: (453, 516), 43: (453, 570), 44: (453, 622), 45: (453, 675), 46: (453, 728), 47: (400, 728),
              48: (346, 728), }

'''
1: (675, 453), 2: (622, 453), 3: (570, 453), 4: (516, 453), 5: (467, 466), 6: (453, 516), 7: (453, 570),
8: (453, 622), 9: (453, 675),10: (453, 728), 11: (400, 728), 12: (346, 728), 48: (675, 400), 49: (622, 400), 50: (570, 400), 51: (516, 400), 52: (466, 400)
'''
# PNG
greenpng = pygame.image.load('img/greenPawn.png')

greenp1 = Pawn(greenpng, greenDICT, (219, 655), 1)
greenp2 = Pawn(greenpng, greenDICT, (143, 655), 2)
greenp3 = Pawn(greenpng, greenDICT, (143, 578), 3)
greenp4 = Pawn(greenpng, greenDICT, (219, 578), 4)

GreenPawnList = [greenp1, greenp2, greenp3, greenp4]
for rp in GreenPawnList:
    allSprites.add(rp)
    greenPawn.add(rp)
print(len(greenPawn))
