import pygame
import random
from Pawns import *

# Player Constructor Class
class Player():
    def __init__(self, name, color, pawns):
        self.name = name
        self.color = color
        # not yet implemented kills attribute        
        #self.kills = 0
        # the list of pawns that belong to this player
        self.pawnlist = pawns
        # for tracking how many pawns are currently in play
        self.pawns = 0
        # self.active represents whether the player is on the board or not
        self.active = False
        # self.turn represents whether it is the player's turn
        self.turn = False
        #set player objects Boolean variables
        self.Player1 = False
        self.Player2 = False
        self.Player3 = False
        self.Player4 = False
        #set player number based on name upon object initialization
        self.set_player_number()
    
    #this may be more useful later for naming and referencing purposes
    def set_player_number(self):
         if self.name == 'Player1':
             # if we set an attribute named after the player number, and set it to true, we can simply write if self.Player1 to check if an object on a list in a for loop is this specific player
             # this is also useful to determine if this instance of a player object is the one we intend to work with
            self.Player1 = True
         elif self.name == 'Player2':
            self.Player2 = True
         elif self.name == 'Player3':
            self.Player3 = True
         elif self.name == 'Player4':
            self.Player4 = True
            
    # this method is called before the mainloop is initialized                
    def set_statekeeper(self, statekeeper):
        #set statekeeper object as an attribute        
        self.Statekpr = statekeeper
        #set the list of players as an attribute
        self.players = self.Statekpr.players      
        # set self.player attribute to refer to the specific object it is, this can be very useful, all you have to do is write self.Player to refer to this specific instance of player object.
        if self.Player1:
             self.Player = self.Statekpr.playerRed
        elif self.Player2:
             self.Player = self.Statekpr.playerBlue
        elif self.Player3:
             self.Player = self.Statekpr.playerYellow
        elif self.Player4:
             self.Player = self.Statekpr.playerGreen             
                
    #ensure player attributes are up to date and represent the current status
    def update_self(self):                  
        if self.Player1:
            # self.active is true if this player is active
            self.active = self.Statekpr.redActive
            # self.turn is true if it is currently this player's turn
            self.turn = self.Statekpr.redTurn
        elif self.Player2:
            self.active = self.Statekpr.blueActive
            self.turn = self.Statekpr.blueTurn
        elif self.Player3:
            self.active = self.Statekpr.yellowActive
            self.turn = self.Statekpr.yellowTurn
        elif self.Player4:
            self.active = self.Statekpr.greenActive
            self.turn = self.Statekpr.greenTurn      
            
    # ensure the statekeeper is updated with the latest attribute statuses        
    def update_statekeeper(self):        
        if self.Player1:
            self.Statekpr.redActive = self.active
            self.Statekpr.redTurn = self.turn
        elif self.Player2:
            self.Statekpr.blueActive = self.active
            self.Statekpr.blueTurn = self.turn
        elif self.Player3:
            self.Statekpr.yellowActive = self.active
            self.Statekpr.yellowTurn = self.turn
        elif self.Player4:
            self.Statekpr.greenActive = self.active
            self.Statekpr.greenTurn = self.turn       
        # self.activeplayer refers to the currently active player who's turn it is        
        self.Statekpr.activeplayer = self.activeplayer       
        # self.nextplayer refers to the player who's turn is next        
        self.Statekpr.nextplayer = self.nextplayer   
        
        # update the activeplayer attribute to the current active player
        # update the nextplayer attribute to player who will be active next
        # this method is called in the player Turn Method
    def update_active_and_next(self):       
        self.activeplayer = self.Statekpr.activeplayer
        self.nextplayer = self.set_next_player()    
        
    def set_next_player(self):
        # for each of the 4 players, 
        for i in range(0,4):
            # if the active player is indexed in the players list at the current value of i 
            if self.activeplayer == self.players[i]: 
                # take the current index of the players list that equals the activeplayer and add 1 to the value                
                nextnumber = i + 1
                # check if adding 1 exceeds the range of the index
                if nextnumber < 4:
                    # if it does not exceed, then the next player is the located at the next number of the index
                    nextplayer = self.players[nextnumber]
                else:
                    #if it does exceed the range of the list, then the next player is at index 0.
                    nextplayer = self.players[0]  
        # pass the next player object from this method to a variable
        return nextplayer

    def dice_roll(self): 
        # randomly determine a value from 1 through and including 6
        rand = random.randint(1, 6)
        print(rand) 
        #pass the value from this method to a variable
        return rand                      
        
    #attempt to move out of the starting location by rolling dice
    def move_out_onto_the_board(self):  
        # "roll the dice" and assign it to the roll variable
        roll = self.dice_roll()
        # if a 6 is rolled, then move out onto the board
        if roll == 6:
            #increment the value of active pawns belonging to the player
            self.pawns += 1     
            #player is now considered active
            self.active = True            
            #ensure the statekeeper is current
            self.update_statekeeper()
            #run the move active player pawn method
            self.move()   
            
    #The method that runs when it is a player's turn
    def Turn(self):
        #ensure the active and next player attributes reflect the current status
        self.update_active_and_next()
        # if the player has no active pawns then attempt to move one from the start area
        if self.pawns < 1:
            self.move_out_onto_the_board()
        else:
            # else just move the active player pawn
            self.move()  
    
    #the method for moving the active players active pawn
    def move(self):      
        #roll dice and assign the movement distance to a variable
        distance = self.dice_roll()
        #loop through pawns in the players group to check for active pawn
        for pawn in self.pawnlist:
             #check which pawn is active
            if pawn.activepawn:
                #move active pawn according to dice roll and pass distance integer variable and the statekeeper object
                pawn.move(distance, self.Statekpr)
                #update pawn states
                pawn.update_pawn_state(self.activeplayer, self.nextplayer)
                #active pawn found, moved and updated so loop can stop
                break
            #keep looping until active pawn found
            else:
                continue
        #ensure the statekeeper is kept current
        self.update_statekeeper()
              
        
                    


