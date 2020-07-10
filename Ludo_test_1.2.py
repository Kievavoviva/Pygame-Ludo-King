import pygame
import random


pygame.init()


win = pygame.display.set_mode((200,200))
pygame.display.set_caption('LudoTest12')


# just for making it clear and simple to understand.
class Player():
    def __init__(self, name, pawnlist):
        self.dice = 0
        self.name = name
        self.PAWNLIST = pawnlist


    def roll(self):
        r = random.randint(1,6)
        self.dice = r
        print(r)


        if self.dice == 6:
            # here it is checking the player Pawnlist if there is any inactive pawns it will activate.


            for i in self.PAWNLIST:
                if i.state == False:
                    i.state = True
                    print(str(i.number), ' is active')
                    break
                else:
                    # I guess here we can let the player decide which one to move now.
                    pass


class Object(pygame.sprite.Sprite):
    def __init__(self, number, state):
        super(Object, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((random.randint(100,255),random.randint(150,255),random.randint(150,200)))
        self.rect = self.surf.get_rect(center=(random.randint(0,200),random.randint(0,200)))
        self.dict = {1:(10,10),2:(20,20),3:(30,30),4:(40,40),5:(50,50),6:(60,60),7:(70,70),8:(80,80),9:(90,90),10:(100,100)
                     ,11:(110,110),12:(120,120),13:(130,130),14:(140,140),15:(150,150),16:(160,160),17:(170,170),18:(180,180)
                     ,19:(190,190),20:(200,200)}
        self.state = state
        self.count = 0
        self.number = number


    def update(self, key):


        # here the update function which keep the information about all of the keys for each pawns so it make it sense!


        if key[pygame.K_1]:
            if self.number == 1:
                if self.state == True:
                    print('move1')
                    self.count += 1
                    self.rect.center = self.dict[self.count]
                else:
                    print('1 Not active')


        elif key[pygame.K_2]:
            if self.number == 2:
                if self.state == True:
                    print('move2')
                    self.count += 1
                    self.rect.center = self.dict[self.count]
                else:
                    print('2 Not active')


        elif key[pygame.K_3]:
            if self.number == 3:
                if self.state == True:
                    print('move3')
                    self.count += 1
                    self.rect.center = self.dict[self.count]
                else:
                    print('3 Not active')


        elif key[pygame.K_4]:
            if self.number == 4:
                if self.state == True:
                    print('move4')
                    self.count += 1
                    self.rect.center = self.dict[self.count]
                else:
                    print('4 Not active')








class controller():
    # this the controller object which keeps the all the control functions for each player, we can add it later right?
    # we can call this objectControl function in MainLoop Function simplicity sake?
    def objectControl(self, key):
        object1.update(key)
        object2.update(key)
        object3.update(key)
        object4.update(key)






allobj = pygame.sprite.Group()


object1 = Object(1, False)
object2 = Object(2, False)
object3 = Object(3, False)
object4 = Object(4, False)






pawnlist = [object1,object2, object3, object4]


for i in pawnlist:
    allobj.add(i)


# initialized player
player1 = Player('red', pawnlist)


main = True
# Controller
control = controller()
while main:
    win.fill((20,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            # here it is will control all pawns
            control.objectControl(keys)
            if event.key == pygame.K_SPACE:
                player1.roll()


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pressed()




    for entity in allobj:
        win.blit(entity.surf, entity.rect)
    pygame.display.flip()