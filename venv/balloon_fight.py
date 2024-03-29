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
house.pos= 390, 460

tree = Actor('tree')
tree.pos = 700,450 #makes tree appear somehwere on the grass background

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
    global score, scores
    filename = r'C:\Users\Tatiana\PycharmProjects\balloon_Fight\venv\high-scores.txt'
    scores = []
    with open(filename, 'r') as file:
        line = file.readline()
        high_scores = line.split()

    for num in high_scores: #binary swap? what type of swap is this
        if score > int(num):
            scores.append(str(score)+" ")
            score = int(num)
        else:
            scores.append(str(num)+ " ")

    with open(filename, "w") as file:
        for num in scores:
            file.write(num)
    file.close()
    print("High Scores: {}".format(scores))


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

def flap():
    global bird_up
    if bird_up:
        bird.image="bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up=True
def update():
    global game_over, score, num_of_updates

    if not game_over: #if the game is not over yet
        if not up: #if up is false
            balloon.y+=1 #move the balloon down by 1
        if bird.x>0:
            bird.x-=4
            if num_of_updates == 9:
                flap()
                num_of_updates = 0
            else:
                num_of_updates +=1
        else:
            bird.x=WIDTH
            bird.y=random.randint(0,HEIGHT/1.5)
            score+=1 #this means the balloon avoided getting hit by the bird which adds a point
            num_of_updates = 0
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
        if balloon.collidepoint(bird.x,bird.y) or balloon.collidepoint(house.x,house.y) or balloon.collidepoint(tree.x,tree.y):
            game_over = True
            update_high_scores()

pgzrun.go()