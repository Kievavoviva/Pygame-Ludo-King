import pygame
from Pawns import *
from Players import *

# The Status Keeper object
class Statekeep:
    def __init__(self):
        #Set main player List
        self.players = []
        #Set Initial States
        self.gamestart = False
        self.firsturn = False
        #assign player Turn state variables
        self.redTurn = True
        self.blueTurn = False
        self.yellowTurn = False
        self.greenTurn = False
        # this list is useful for assigning the current players turn to a variable named currenturn
        self.turnlist = [self.redTurn, self.blueTurn, self.yellowTurn, self.greenTurn]              
        #assign player active state variables
        self.redActive = True
        self.blueActive = False
        self.yellowActive = False
        self.greenActive = False        
        # this list is useful for assigning the active player to a variable named activeplayer
        self.activelist = [self.redActive, self.blueActive, self.yellowActive, self.greenActive]        
        #set pawn groups to status keeper attributes
        self.redpawns = RedPawnList
        self.bluepawns = BluePawnList
        self.yellowpawns = YellowPawnList
        self.greenpawns = GreenPawnList
        #set counter lists
        self.redcounters = []
        self.bluecounters = []
        self.yellowcounters = []
        self.greencounters = []
        #set the counters lists with values upon initialization 
        self.set_counterlist_status()
        #Initialize Player Objects and append to main player list    
        self.players.append(Player('Player1', 'Red', self.redpawns))
        self.players.append(Player('Player2', 'Blue', self.bluepawns))
        self.players.append(Player('Player3', 'Yellow', self.yellowpawns))
        self.players.append(Player('Player4', 'Green', self.greenpawns))   
        #assign Player objects to attribute variables from the players list
        self.playerRed = self.players[0]
        self.playerBlue = self.players[1]
        self.playerYellow = self.players[2]
        self.playerGreen = self.players[3]
        # set initial active and next player
        self.activeplayer = self.playerRed
        self.nextplayer = self.playerBlue
        
    # set game initialization variables, this method may grow and become more useful later        
    def start_game(self):
        self.gamestart = True
        self.firstturn = True     
        
    # Initialize the lists and assign the current values. 
    def set_counterlist_status(self): 
        # there are 4 pawns per player so the range is 0 through 3 stopping at 4                
        for i in range(0,4):
            # assign a variable to the integer value of the counter of the pawn at the index of value i in the redplayer pawns list
            countervalue = self.redpawns[i].counter    
            # append the counter values to the red pawn counters list in the order of the pawns in the pawns list            
            self.redcounters.append(countervalue)
        for i in range(0,4):
            countervalue = self.bluepawns[i].counter                
            self.bluecounters.append(countervalue)
        for i in range(0,4):
            countervalue = self.yellowpawns[i].counter                
            self.yellowcounters.append(countervalue)
        for i in range(0,4):
            countervalue = self.greenpawns[i].counter                
            self.greencounters.append(countervalue)     
       
    # for clearing the lists containing the counter values as integers and calling the set counter status method to store the current counter values.      
    # this method is called with every iteration of the main loop by the status keeper update method.
    def reset_counterlist_status(self):
        self.redcounters.clear()
        self.bluecounters.clear()
        self.yellowcounters.clear()
        self.greencounters.clear()
        self.set_counterlist_status()  
            
    # set the activeplayer attribute value to represent the object of the current active player
    def update_active_player(self):
        ## there are 4 players so the range of i values needed is 0 through 3 stopping at 4 
        for i in range(0,4):
            # if the the active status of the player in the active players list at the index value of i is True
            if self.activelist[i]:
                # the activeplayer attribute is assigned to the equivalent value of the players list because the player status are appended in the same order
                self.activeplayer = self.players[i]            
            
    #set the current turn attribute to the player object whose turn it is.   
    def update_player_turn(self):
        ## there are 4 players so the range of i values needed is 0 through 3 stopping at 4 
        for i in range(0,4):
            # if the player in the turn list at index i is True, meaning that it is that players turn
            if self.turnlist[i]:
                # set the current turn attribute to refer to the player object whose turn  it is which is at the equivelant i index value because they are appended in the same order
                self.currentTurn = self.players[i]
            else:
                #else pass isnt really necessary but its harmless and I like it
                pass        
            
    def update_players(self):
        #updates player status of active player and current turn for all the player objects
        for player in self.players:
            player.update_self()    
    
    #update the statuskeeper with important statuses, this is called toward the beginning of every iteration of the main loop
    def update(self):
        self.reset_counterlist_status()
        self.update_active_player()
        self.update_player_turn()
        self.update_players()       
              
    # the main method for attempting to move a player if it is their turn by calling the player turn method. Also sets the turn status values
    # this is the method in the main loop that leads to the most change
    def move_player(self):      
        if self.redTurn:
            self.playerRed.Turn()
            self.redTurn = False
            self.blueTurn = True            
        elif self.blueTurn:
            self.playerBlue.Turn()
            self.blueTurn = False
            self.yellowTurn = True            
        elif self.yellowTurn:
            self.playerYellow.Turn()
            self.yellowTurn = False
            self.greenTurn = True            
        elif self.greenTurn:
            self.playerGreen.Turn()
            self.greenTurn = False
            self.redTurn = True
        
      

   
    