import pgzrun, random

"""
Project No. Balloon Fight 
When the game starts a hot air balloon appears in the middle of the screen. You need to use the mouse button 
to make the balloon rise or fall. THe challenge is to keep the balloon in the air without hitting any birds, houses, or
trees. Game is over if you hit one. 

"""

#CONSTANTS
WIDTH = 800
HEIGHT = 600

#Global vars
bird_up = True
up = False
game_over = False
score = 0
num_of_updates = 0
scores = []

balloon = Actor("balloon")
balloon.pos = 400,300

bird = Actor('bird-up')
bird.pos = random.randint(0,800), random.randint(10,200) #bird appears

house = Actor('house')
house.pos= random.randint(0,800), 460

tree = Actor('tree')
tree.pos = random.randint(0,800),450 #makes tree appear somehwere on the grass background

def draw():
    screen.blit("background",(0,0))

    if not game_over:
        balloon.draw()
        bird.draw()
        tree.draw()
        house.draw()
        screen.draw.text("Score: {}".format(score),(700,500),color="black")
    else:
        display_high_scores()

def update_high_scores():
    pass

def display_high_scores():
    pass


pgzrun.go()