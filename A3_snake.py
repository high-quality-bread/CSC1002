"""
This is a snake game written in python.

Created by 122090644
"""
import turtle
import random
from functools import partial

g_screen = None  # The screen.
g_snake = None  # The turtle Snake.
g_monster = None  # The turtle Monster.
g_snake_sz = 5  # Length of the Snake.
g_intro = None  # The turtle that writes the introduction of the game.
g_keypressed = None  # Keyboard key hit.
g_status = None  # The turtle that writes the direction of movement of the snake.
g_time = None  # The turtle that writes time.
g_loc_disappear = None  # The label of food turtle that disappeared.
g_last_pressed = None  # The last none-space pressed key.

g_head = (0, -40)  # The coordinates of the snake head.

g_monster_x = 0  # Monster's current x-coordinate.
g_monster_y = 0  # Monster's current y-coordinate.
g_x = 0  # Snake's current x-coordinate.
g_y = -40  # Snake's current x-coordinate.
g_total_time = 0  # Play time after the game starts.
g_contact_time = 0  # The number of times the Monster has come into contact with the snake's tail.

g_food_list = []  # The coordinates of the food.
g_whether_eat = [1, 1, 1, 1, 1]  # Whether the foods are eaten, 1 means no, 0 means yes.
g_hide = [1, 1, 1, 1, 1]  # Whether the food is hidden, 1 means no, 0 means yes.
g_food = []  # List of the food turtle created.
g_food_cor = []  # List of the (x-cor, y-cor) of the 5 food turtles.
g_tailList = []  # The (x-cor, y-cor) of each stamp of the snake tail.

g_touch = False  # Whether the snake head has touched the boundary, False means no, True means yes.
g_mTouch = False  # Whether the Monster has touched the tail of the snake, False means no, True means yes.
g_start = False  # Whether the game start, False means no, True means yes.
g_win = False  # Whether the game win, False means no, True means yes.
g_lose = False  # Whether the game lose, False means no, True means yes.

g_snake_status = "Pause"  # The status of the snake.


"""
Set the color of snakes and monsters, set fonts and keys.
"""
COLOR_BODY = ("blue", "black")
COLOR_HEAD = "red"
COLOR_MONSTER = "purple"
FONT = ("Arial", 16, "normal")

KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE = \
       "Up", "Down", "Left", "Right", "space"

HEADING_BY_KEY = {KEY_UP: 90, KEY_DOWN: 270, KEY_LEFT: 180, KEY_RIGHT: 0}


def configScreen():
    """
    Returns a screen with a height of 660 and a width of 580 and a title.

    Also disable auto screen refresh.
    """
    s = turtle.Screen()
    s.tracer(0)
    s.title("Snake by 122090644")
    s.setup(500+80, 500+80+80)
    s.mode("standard")
    return s


def configurePlayArea():
    """
    Configure play area

    Return a 500 * 80 upper status area and a 500 * 500 lower motion area.
        The area have a 40 pixels margin.

    Return the intro of the game displays on the lower area.
        Create three turtles to write: Contact, Time and Motion.
    """
    m = createTurtle(0, 0, "", "black")
    m.shapesize(25, 25, 5)
    m.goto(0, -40) 

    s = createTurtle(0, 0, "", "black")
    s.shapesize(4, 25, 5)
    s.goto(0, 250)

    intro = createTurtle(-200, 60)
    intro.hideturtle()
    intro.write("Welcome to xxx's version of snake. \
                \n\nYou are going to use the 4 arrow keys to move the snake \
                \naround the screen, trying to consume all the food items \
                \nbefore the monster catches you! \
                \n\nClick anywhere on the screen to start the game",
                font=("Arial", 12, "normal"))
    
    # statuses
    status = createTurtle(0, 0, "", "black")
    status.hideturtle()
    status.goto(-200, s.ycor())

    time = createTurtle(-50, 235, "", "black")
    time.hideturtle()

    contact = createTurtle(-200, 235, "", "black")
    contact.hideturtle()

    return intro, status, time, contact


def createTurtle(x, y, color="red", border="black"):
    """
    Return the snake head turtle at the (x, y) with red color and black margin.
    """
    t = turtle.Turtle("square")
    t.color(border, color)
    t.up()
    t.goto(x, y)
    return t


def updateStatus():
    """
    Return to write the motion direction at the upper status area.

        e.g. Motion: Right
    """
    g_status.clear() 
    g_status.goto(80, 235)
    g_status.write("Motion: {}".format(g_keypressed), font=('arial', 16, 'bold'))
    g_screen.update()


def totalTime():
    """
    Return to write the total time at the upper status area.

    Will be returned every one second.

        e.g. Time: 2
    """
    global g_total_time

    if g_win is True:
        return
    elif g_lose is True:
        return
    
    g_time.clear() 
    g_time.write("Time: {}".format(g_total_time), font=('arial', 16, 'bold'))
    g_screen.update()
    if g_start is True:
        g_total_time += 1
    turtle.ontimer(totalTime, 1000)


def totalContact():
    """
    Return to write The number of contacts between the snake tail and the monster at the upper status area.

        e.g. Contact: 2
    """
    g_contact.clear()
    g_contact.write("Contact: {}".format(g_contact_time), font=('arial', 16, 'bold'))
    g_screen.update()
    turtle.ontimer(totalContact, 500)


def food():
    """
    Return randomly spawned food at five different locations on the screen.

    Each food is represented by a non-repeating number from 1-5.

        e.g.
         ____________________
        |     1           4  |
        |                    |
        |          3         |
        |                    |
        |   2                |
        |               5    |
        |____________________|
    """
    global g_food_list
    global g_food_cor
    global g_food

    for i in range(1, 6):
        x = random.randint(-12, 12) * 20
        y = random.randint(-14, 10) * 20
        while (x, y) in g_food_list:
            x = random.randint(-12, 12) * 20
            y = random.randint(-14, 10) * 20
        g_food_list.append((x, y))

        t = createTurtle(0, 0, "", "black")
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.goto(x, y - 10)
        t.write(str(i), align="center", font=("Arial", 12, "normal"))
        t.goto(x, y)

        g_food.append(t)
        g_food_cor.append((x, y))
        g_screen.update()


def foodDisappear():
    """
    Return to randomly hide one food on the screen.

    Return to appear the hide one last time when hide the next one.

        e.g. before                        after
             ____________________           ____________________
            |     1           4  |         |     1           4  |
            |                    |         |                    |
            |          3         |         |                    |
            |                    |         |                    |
            |                    |         |    2               |
            |               5    |         |               5    |
            |____________________|         |____________________|
    """
    global g_food
    global random_food
    global g_loc_disappear
    global g_hide

    random_food = random.choice(g_food)
    g_loc_disappear = g_food.index(random_food)
    random_food.clear()
    g_hide[g_loc_disappear] = 0
    g_screen.update()
    turtle.ontimer(foodAppear, 6000)
    turtle.ontimer(foodDisappear, 6000)
    

def foodAppear():
    """
    Return to appear the hide food on the screen.

        e.g. before appear (food 2)        after appear (food 2)
             ____________________           ____________________
            |     1           4  |         |     1           4  |
            |                    |         |                    |
            |          3         |         |                    |
            |                    |         |                    |
            |                    |         |    2               |
            |               5    |         |               5    |
            |____________________|         |____________________|
    """
    global random_food
    global g_hide

    g_hide[g_loc_disappear] = 1

    if g_whether_eat[g_loc_disappear] == 1:
        (x, y) = g_food_cor[g_loc_disappear]
        random_food.goto(x, y - 10)
        random_food.write(g_loc_disappear + 1, align="center", font=("Arial", 12, "normal"))
        random_food.goto(x, y)
    g_screen.update()


def checkEat():
    """
    Check whether the snake eat the food

    Return the snake to add the length of the tail by the food number.

        e.g. If the snake eat the food with number 5, its tail will add length 100 pixels.
    """
    global g_food
    global g_snake_sz
    global g_whether_eat

    if g_head in g_food_cor:
        loc = g_food_cor.index(g_head)
        if g_hide[loc] == 1:
            if g_whether_eat[loc] == 1:
                g_whether_eat[loc] = 0
                g_food[loc].clear()
                g_screen.update()
                food_number = loc + 1
                g_snake_sz += food_number
    g_screen.update()


def createRandomMonster():
    """
    Randomly create the Monster on the screen (but not that "random").

    Return the monster turtle on the screen.
    Both the x and y coordinates of the monster center from the snake are greater than or equal to 90 pixels

    Will be returned if the monster's position does not meet the requirements

        e.g.           motion screen
         _________________________________________
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |            _________________            |
        |           |                 |           |
        |           |      don't      |           |
        |           |      meet       |           |
        |           |    requirment   |           |
        |           |                 |           |
        |           |_________________|           |
        |                                         |
        |                                         |
        |           meet the requirment           |
        |                                         |
        |_________________________________________|
    """
    global g_monster

    x = random.randint(-12, 11) * 20 + 10
    y = random.randint(-14, 9) * 20 + 10

    while not (-230 <= x <= -90 or 90 <= x <= 230 or -270 <= y <= -110 or 50 <= y <= 190):
        x = random.randint(-12, 12) * 20 + 10
        y = random.randint(-14, 10) * 20 + 10

    g_monster = createTurtle(-110, -110, "purple", "purple")
    g_monster.goto(x, y)
    return g_monster


def setSnakeHeading(key):
    """
    Return the direction of the snake head.
    """
    if key in HEADING_BY_KEY.keys():
        g_snake.setheading(HEADING_BY_KEY[key])


def onArrowKeyPressed(key):
    """
    Return to set the snake heading by the key pressed.
    """
    global g_keypressed
    g_keypressed = key
    setSnakeHeading(key)
    updateStatus()


def snakeTail(x, y, z):
    """
    Collect the coordinates of all the tail stamps.

    Returns a list containing the coordinates of the center point of each stamp of the snake's tail.
    """
    global g_tailList
    g_tailList.append((x, y))
    if len(g_tailList) > z:
        g_tailList.pop(0)


def touchTail(x, y):
    """
    Check whether the snake head touch the tail.

    Return True if touched, False if not.
    """
    global g_touch
    global g_keypressed
    global g_tailList

    if g_keypressed == "Up":
        if (x, y+20) in g_tailList:
            g_touch = True
        else:
            g_touch = False    
    elif g_keypressed == "Down":
        if (x, y-20) in g_tailList:
            g_touch = True
        else:
            g_touch = False
    elif g_keypressed == "Left":
        if (x-20, y) in g_tailList:
            g_touch = True
        else:
            g_touch = False    
    elif g_keypressed == "Right":
        if (x+20, y) in g_tailList:
            g_touch = True
        else:
            g_touch = False    
    elif g_keypressed is None:
        g_touch = False        
    else:
        g_touch = False    


def monsterTouch():
    """
    Check whether the monster touches the tail of the snake.

    Return True if touch the snake.

    Else return false.
    """
    global g_mTouch
    if (g_monster_x + 10, g_monster_y - 10) in g_tailList:
        g_mTouch = True
    elif (g_monster_x + 10, g_monster_y + 10) in g_tailList:
        g_mTouch = True
    elif (g_monster_x - 10, g_monster_y + 10) in g_tailList:
        g_mTouch = True
    elif (g_monster_x - 10, g_monster_y - 10) in g_tailList:
        g_mTouch = True
    else:
        g_mTouch = False


def checkWin():
    """
    Check whether the game win.

    Return true if the game win.
    """
    global g_win

    if len(g_snake.stampItems) == 20:
        if g_snake_sz == 20 and g_lose == False:
            g_win = True


def checkLose():
    """
    Check whether the game lose.

    Return true if the game lose.
    """
    global g_lose

    g_monster_x, g_monster_y = g_monster.pos()

    g_monster_x = int(g_monster_x)
    g_monster_y = int(g_monster_y)
    g_monster_x = round(g_monster_x, -1)
    g_monster_y = round(g_monster_y, -1)

    if (g_monster_x + 10, g_monster_y - 10) == g_head:
        g_lose = True
    elif (g_monster_x + 10, g_monster_y + 10) == g_head:
        g_lose = True
    elif (g_monster_x - 10, g_monster_y + 10) == g_head:
        g_lose = True
    elif (g_monster_x - 10, g_monster_y - 10) == g_head:
        g_lose = True


def checkMove():
    """
    Check whether the snake head touch the "wall".

    Return True if touched.
    """
    global g_touch

    if g_keypressed == 'Up':
        if g_snake.ycor()+10 >= 210:
            g_touch = True
    if g_keypressed == 'Right':
        if g_snake.xcor()+10 >= 250:
            g_touch = True
    if g_keypressed == 'Down':
        if g_snake.ycor()-10 <= -290:
            g_touch = True
    if g_keypressed == 'Left':
        if g_snake.xcor()-10 <= -250:
            g_touch = True


def checkSnake():
    """
    Check the status of the snake.

    Return nothing if the game win or lose or the snake is pause.

    Return to move the snake in other situations.
    """
    global g_x
    global g_y
    global g_head
    global g_snake_status
    global g_keypressed

    checkLose()
    checkWin()
    
    if g_lose is True:
        return
    
    elif g_win is True:
        g_snake.write("win", font=('arial', 16, 'bold'))
        return

    elif g_keypressed == KEY_SPACE and g_snake_status == "Move":
        g_keypressed = None
        g_snake_status = "Pause"
        g_screen.ontimer(checkSnake, 200 + (g_snake_sz-5)*20)
        return
    
    elif g_keypressed == KEY_SPACE and g_snake_status == "Pause":
        g_keypressed = g_last_pressed
        g_snake_status = "Move"
        g_status.clear()
        g_status.write("Motion: {}".format(g_last_pressed), font=('arial', 16, 'bold'))
        snakeMove()

    elif g_keypressed is None:
        g_screen.ontimer(checkSnake, 200 + (g_snake_sz-5)*20)
        return
    
    else:
        snakeMove()


def snakeMove():
    """
    Return to move the snake forward 20 pixels if the snake head doesn't touch its tail.

    Return nothing if snake head touch its tail.

    In all cases checkSnake() will be returned, the interval is 200 + (length of tail-5)*20 ms.
    This means the snake will move slower if it becomes longer.
    """
    global g_x
    global g_y
    global g_head
    global g_snake_status
    global g_keypressed
    global g_last_pressed

    g_snake_status = "Move"

    i, j = g_snake.pos()
    i = int(i)
    j = int(j)
    i = round(i, -1)
    j = round(j, -1)

    touchTail(i, j)
    checkMove()

    g_last_pressed = g_keypressed

    if g_touch is False:
        snakeTail(i, j, g_snake_sz)
        # Advance snake
        g_snake.color(*COLOR_BODY)
        g_snake.stamp()
        g_snake.color(COLOR_HEAD)

        if g_lose is True:
            return

        g_snake.forward(20)
        x, y = g_snake.pos()
        x = int(x)
        y = int(y)
        x = round(x, -1)
        y = round(y, -1)
        g_head = (x, y)

        g_x = g_snake.xcor()
        g_y = g_snake.ycor()

        checkEat()

        if len(g_snake.stampItems) > g_snake_sz:
            g_snake.clearstamps(1)
        
        g_screen.update()
        g_screen.ontimer(checkSnake, 200 + (g_snake_sz-5)*20)

    elif g_touch is True:
        g_screen.ontimer(checkSnake, 200 + (g_snake_sz-5)*20)    


def onTimerMonster():
    """
    Move the monster according to the coordinates of the monster and snake head.

    Return to move the monster forward 20 pixels.
    Return checkSnake(), the interval is random.randint(800, 1000),
        which means the monster will move at a random speed.

    Return nothing if the game win or lose.
    """
    global g_monster
    global g_monster_x
    global g_monster_y
    global g_contact_time

    g_monster_x, g_monster_y = g_monster.pos()

    g_monster_x = int(g_monster_x)
    g_monster_y = int(g_monster_y)
    g_monster_x = round(g_monster_x, -1)
    g_monster_y = round(g_monster_y, -1)

    # calculate the distance to the target point
    dx, dy = g_x - g_monster_x, g_y - g_monster_y

    # calculate the movement direction
    if abs(dx) > abs(dy):
        if dx > 0:
            direction = 'right'
        else:
            direction = 'left'
    else:
        if dy > 0:
            direction = 'up'
        else:
            direction = 'down'

    # move the monster one step in the direction
    if direction == 'up':
        g_monster.setheading(90)
    elif direction == 'down':
        g_monster.setheading(270)
    elif direction == 'right':
        g_monster.setheading(0)
    elif direction == 'left':
        g_monster.setheading(180)

    checkWin()
    checkLose()
    monsterTouch()

    if g_win is True:
        return
    if g_lose is True:
        g_monster.write("Game over!", font=('arial', 16, 'bold'))
        return

    g_monster.forward(20)

    if g_mTouch is True:
        g_contact_time += 1
    
    g_screen.update()
    g_screen.ontimer(onTimerMonster, random.randint(300, 500))


def startGame(x, y):
    """
    Will be returned after the mouse click.

    Return to start timer, create food on screen check eat move the monster and bind key.

    Return to ignore the mouse click.
    """
    global g_start
    g_start = True
    g_screen.onscreenclick(None)
    g_intro.clear()
    totalTime()
    food()
    checkEat()

    g_screen.onkey(partial(onArrowKeyPressed, KEY_UP), KEY_UP)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_DOWN), KEY_DOWN)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_LEFT), KEY_LEFT)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_RIGHT), KEY_RIGHT)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_SPACE), KEY_SPACE)

    g_screen.ontimer(checkSnake, 100)
    g_screen.ontimer(onTimerMonster, 1000)

    turtle.ontimer(foodDisappear, 3000)


if __name__ == "__main__":

    g_screen = configScreen()
    g_intro, g_status, g_time, g_contact = configurePlayArea()

    updateStatus()
    totalContact()
    g_time.write("Time: 0", font=('arial', 16, 'bold'))

    g_snake = createTurtle(0, -40, "red", "black")
    createRandomMonster()

    g_screen.onscreenclick(startGame)

    g_screen.update()
    g_screen.listen()
    g_screen.mainloop()
