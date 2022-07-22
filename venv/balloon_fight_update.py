import pgzrun, random, pygame

"""
Project No. Balloon Fight 
When the game starts a hot air balloon appears in the middle of the screen. You need to use the mouse button 
to make the balloon rise or fall. THe challenge is to keep the balloon in the air without hitting any birds, houses, or
trees. Game is over if you hit one. 

HACKS AND TWEAKS 

file handling - write now you write to the high-scores.txt every time the program exits. Add efficiency to the code 
by write to the file only if the high scores have changed hint use a boolean

use a list of bird actors 

add a heart image that represents the lives 

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
update_highscores = False
birds = []
lives_counter = 5
previous_actor = Actor('tree')

balloon = Actor("balloon")
balloon.pos = 400,300

for index in range(3):
    birds.append(Actor('bird-up'))
    birds[index].pos = random.randint(0,800), random.randint(10,200) #bird appears

house = Actor('house')
house.pos= 390, 460

tree = Actor('tree')
tree.pos = 700,450 #makes tree appear somehwere on the grass background

lives= Actor('heart5') #actors have all the same attributes as rect so
lives.pos = 930, 70
lives._surf = pygame.transform.scale(lives._surf, (200,30))
lives._update_pos()


def draw():
    screen.blit("background",(0,0))
    if not game_over:
        balloon.draw()
        for bird in birds:
            bird.draw()
        lives.draw()
        tree.draw()
        house.draw()
        screen.draw.text("Score: {}".format(score),(700,500),color="black")
    else:
        display_high_scores()

def update_high_scores():
    global score, scores, update_highscores
    filename = r'C:\Users\Tatiana\PycharmProjects\balloon_Fight\venv\high-scores.txt'
    scores = []
    with open(filename, 'r') as file:
        line = file.readline()
        high_scores = line.split()

    for num in high_scores: #binary swap? what type of swap is this
        if score > int(num):
            scores.append(str(score)+" ")
            score = int(num)
            update_highscores = True
        else:
            scores.append(str(num)+ " ")
    if update_highscores:
        with open(filename, "w") as file:
            for num in scores:
                file.write(num)
        update_highscores = False
    file.close()
   # print("High Scores: {}".format(scores))

def display_high_scores():
    screen.draw.text("HIGH SCORES:",(350,150),color='black')
    y = 175
    position = 1
    for num in scores:
        screen.draw.text('{}. {}'.format(position,num), (305,y),color = "black")
        y+=20
        position +=1

def on_mouse_down(): #when the player clicks on the mouse
    global up
    up = True
    balloon.y -= 50

def on_mouse_up(): #when the player lets go of the mouse
    global up
    up = False

def flap(bird):
    global bird_up

    if bird_up:
        bird.image = 'bird-down'
        bird_up = False
    else:
        bird.image = 'bird-up'
        bird_up = True

def update():
    global game_over, score, num_of_updates, birds, lives_counter, flag


    if not game_over: #if the game is not over yet
        if not up: #if up is false
            balloon.y+=1 #move the balloon down by 1

        for bird in birds:
            if bird.x>0:
                bird.x-=4
                if num_of_updates == 9:
                    flap(bird)
                    num_of_updates = 0
                else:
                    num_of_updates +=1
            else:
                bird.x=random.randint(WIDTH, 1600)
                bird.y=random.randint(0,HEIGHT)
                score+=1 #this means the balloon avoided getting hit by the bird which adds a point
                num_of_updates = 0

            if balloon.collidepoint(bird.x,bird.y):
                actor = bird
                update_lives(bird)

        if balloon.collidepoint(house.x,house.y):
            actor = house
            update_lives(actor)
        if balloon.collidepoint(tree.x,tree.y):
            actor=tree
            update_lives(tree)


        if house.x>0:
            house.x -=2
        else:
            house.x = random.randint(WIDTH, 1600)
            score+=1
        if tree.x>0:
            tree.x -=2
        else:
            tree.x=random.randint(WIDTH,1600)
        if balloon.top < 0 or balloon.bottom > HEIGHT-40:
            game_over = True
            update_high_scores()

def update_lives(actor):
    global lives, previous_actor, lives_counter, game_over

    if actor!=previous_actor:
        lives_counter-=1
        if lives_counter ==4:
            lives.image = 'heart4'
            lives.pos = 930, 70
            lives._surf = pygame.transform.scale(lives._surf, (200, 30))
            lives._update_pos()

        if lives_counter ==3:
            lives.image = 'heart3'
            lives.pos = 930, 70
            lives._surf = pygame.transform.scale(lives._surf, (200, 30))
            lives._update_pos()
        if lives_counter == 2:
            lives.image = 'heart2'
            lives.pos = 930, 70
            lives._surf = pygame.transform.scale(lives._surf, (200, 30))
            lives._update_pos()
        if lives_counter == 1:
            lives.image = 'heart1'
            lives.pos = 930, 70
            lives._surf = pygame.transform.scale(lives._surf, (200, 30))
            lives._update_pos()
        if lives_counter == 0:
            game_over = True
            update_high_scores()
        previous_actor = actor
        print(lives_counter)


pgzrun.go()