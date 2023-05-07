"""
This is a connect4 game written in python use vscode.
Two players click the screen in sequence to play the game.

This game use the logic that divides the screen into 64 location to judge the ball and the color.
The logic like this:

screen
__________________________________
|                                |
| 8  16  24  32  40  48  56  64  |
| 7  15  23  31  39  47  55  63  |
| 6  14  22  30  38  46  54  62  |
| 5  13  21  29  37  45  53  61  |
| 4  12  20  28  36  44  52  60  |
| 3  11  19  27  35  43  51  59  |
| 2  10  18  26  34  42  50  58  |
| 1   9  17  25  33  41  49  57  |
|TR1 TR2 TR3 TR4 TR5 TR6 TR7 TR8 |
|________________________________|
"""
import turtle


g_last_x = 0  # The x-coordinate of the position where the mouse now. 
g_x_pos = 55  # The x-coordinate of the center point of the sphere.
g_color = "blue"  # The color represented by the player currently taking the turn.
g_turn = 1  # The current number of turns.
g_x_coordinate = ""  # The x coordinate where the next ball will fall.
g_blue_list = []  # The position of the red/purple ball among 64 positions.
g_purple_list = []
g_tracker_number = ""  # The tracker where the next ball will fall.
ball_on_tracker1 = 0  # The number of balls already on tracker X.
ball_on_tracker2 = 0
ball_on_tracker3 = 0
ball_on_tracker4 = 0
ball_on_tracker5 = 0
ball_on_tracker6 = 0
ball_on_tracker7 = 0
ball_on_tracker8 = 0


"""
Spawn screen, create trackers and balls.
"""
scn = turtle.Screen()
scn.setup(625, 620)
scn.setworldcoordinates(10, 10, 625, 620)
turtle.title("Welcome to Connect4!")
tracker1 = turtle.Turtle()
tracker2 = turtle.Turtle()
tracker3 = turtle.Turtle()
tracker4 = turtle.Turtle()
tracker5 = turtle.Turtle()
tracker6 = turtle.Turtle()
tracker7 = turtle.Turtle()
tracker8 = turtle.Turtle()
ball_list = [turtle.Turtle() for _ in range(64)]


def eight_trackers():
    """
    Return to place eight trackers on the screen.
    """

    global g_x_pos
    for i in [tracker1, tracker2, tracker3, tracker4, tracker5, tracker6, tracker7, tracker8]:
        i.penup()
        i.shape("square")
        i.fillcolor("black")
        i.pencolor("")
        i.shapesize(1.00, 3.00, 5)
        i.setposition(g_x_pos, 25.00)
        g_x_pos += 75.00


def tracker_frame(x):
    """
    Generates the border of the tracker.

    Return to show the border of the tracker based on the mouse position and the player.

        eg: If the player is blue, then the border of the tracker below the mouse will turn blue.
    """

    global g_color
    global g_turn
    if g_turn % 2 == 1:
        g_color = 'blue'
    else:
        g_color = 'purple'
        
    if x <= 92:
        tracker1.pencolor(g_color)
        init(1)
    elif (x > 92) and (x <= 167):
        tracker2.pencolor(g_color)
        init(2)
    elif (x > 167) and (x <= 242):
        tracker3.pencolor(g_color)
        init(3)
    elif (x > 242) and (x <= 315):
        tracker4.pencolor(g_color)
        init(4)
    elif (x > 315) and (x <= 387):
        tracker5.pencolor(g_color)
        init(5)
    elif (x > 387) and (x <= 462):
        tracker6.pencolor(g_color)
        init(6)
    elif (x > 462) and (x <= 535):
        tracker7.pencolor(g_color)
        init(7)
    elif x > 535:
        tracker8.pencolor(g_color)
        init(8)


def init(i):
    """
    Makes the border of the tracker that not under the mouse to be black.

    Return the black tracker border for the trackers not under the mouse.
    """

    tracker_list = [tracker1, tracker2, tracker3, tracker4, tracker5, tracker6, tracker7, tracker8]
    if i in [1, 2, 3, 4, 5, 6, 7, 8]:
        del tracker_list[i-1]
        for x in tracker_list:
            x.pencolor("")
    else:
        for x in tracker_list:
            x.pencolor("")


def land_which_tracker(x, y):
    """
    Find which tracker to land the ball.

    Return the ball landing function sphere() and the tracker_frame() function by the x coordinate of the mouse click,

    Return add one number to the ball_on_trackerX.

        eg: If you click between 15 <= x <= 92, will return the function sphere() to land the ball on the first tracker, and the 
            ball_on_tracker1 will plus one.

    Return: "Invalid tracker, each column holds up to eight balls.",
    if there are already 8 balls on tracker1, and you click above tracker1,
    """

    global g_x_coordinate
    global ball_on_tracker1
    global ball_on_tracker2
    global ball_on_tracker3
    global ball_on_tracker4
    global ball_on_tracker5
    global ball_on_tracker6
    global ball_on_tracker7
    global ball_on_tracker8
    global g_turn
    global g_tracker_number
    if (x >= 0) and (x <= 90):
        if ball_on_tracker1 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:
            g_tracker_number = 1
            g_x_coordinate = 55
            ball_on_tracker1 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker1)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 90) and (x <= 166):
        if ball_on_tracker2 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 2
            g_x_coordinate = 130
            ball_on_tracker2 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker2)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 166) and (x <= 242):
        if ball_on_tracker3 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 3
            g_x_coordinate = 205
            ball_on_tracker3 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker3)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 242) and (x <= 317):
        if ball_on_tracker4 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 4
            g_x_coordinate = 280
            ball_on_tracker4 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker4)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 317) and (x <= 390):
        if ball_on_tracker5 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 5
            g_x_coordinate = 355
            ball_on_tracker5 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker5)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 390) and (x <= 466):
        if ball_on_tracker6 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 6
            g_x_coordinate = 430
            ball_on_tracker6 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker6)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 466) and (x <= 540):
        if ball_on_tracker7 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 7
            g_x_coordinate = 505
            ball_on_tracker7 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker7)
            g_turn += 1
            tracker_frame(g_last_x)
    elif (x > 540) and (x <= 628):
        if ball_on_tracker8 >= 8:
            print("Invalid tracker, each column holds up to eight balls.\n")
        else:  
            g_tracker_number = 8
            g_x_coordinate = 580
            ball_on_tracker8 += 1
            sphere(g_x_coordinate, 15 + 70 * ball_on_tracker8)
            g_turn += 1
            tracker_frame(g_last_x)


def sphere(tracker, height):
    """
    Land the ball to the tracker.

    Return the ball landing to the tracker after the player click, the color of the ball determines by which player click.

    Return to check whether blue wins, purple wins or tie.
    """

    global g_color
    global g_blue_list
    global g_purple_list
    scn.onclick(None)
    
    if g_tracker_number == 1:
        num = ball_on_tracker1
        key = ball_on_tracker1 - 1
    elif g_tracker_number == 2:
        num = ball_on_tracker2
        key = 8 + ball_on_tracker2 - 1
    elif g_tracker_number == 3:
        num = ball_on_tracker3
        key = 16 + ball_on_tracker3 - 1
    elif g_tracker_number == 4:
        num = ball_on_tracker4
        key = 24 + ball_on_tracker4 - 1
    elif g_tracker_number == 5:
        num = ball_on_tracker5
        key = 32 + ball_on_tracker5 - 1
    elif g_tracker_number == 6:
        num = ball_on_tracker6
        key = 40 + ball_on_tracker6 - 1
    elif g_tracker_number == 7:
        num = ball_on_tracker7
        key = 48 + ball_on_tracker7 - 1
    elif g_tracker_number == 8:
        num = ball_on_tracker8
        key = 56 + ball_on_tracker8 - 1

    ball_list[key].penup()
    ball_list[key].ht()
    ball_list[key].shape("circle")
    ball_list[key].shapesize(3.00, 3.00, 5.00)

    if g_turn % 2 == 1:
        g_color = 'blue'
        ball_list[key].fillcolor(g_color)
        blue_number = int((g_tracker_number-1)*8 + num)
        g_blue_list.append(blue_number)
        g_blue_list.sort()
    else:
        g_color = 'purple'
        ball_list[key].fillcolor(g_color)
        purple_number = int((g_tracker_number-1)*8 + num)
        g_purple_list.append(purple_number)
        g_purple_list.sort()

    ball_list[key].pencolor("")
    ball_list[key].speed(0)
    ball_list[key].setposition(tracker, height)
    ball_list[key].st()
    scn.onclick(land_which_tracker)
    check_connect_blue()
    check_connect_purple()
    check_tie()


def check_connect_blue():
    """
    Check whether blue wins.

    Return four connected blue balls with red border and heading "Winner! Player Blue".

        eg: Eligible situations include:
            (1)  (B ball) (B ball) (B ball) (B ball)

            (2)  (B ball)
                 (B ball)
                 (B ball)
                 (B ball)

            (3)  (B ball)
                        (B ball)
                                (B ball)
                                        (B ball)

            (4)                         (B ball)
                                (B ball)
                        (B ball)
                (B ball)                  
    """

    for i in g_blue_list:
        if (int(i + 1) in g_blue_list) and (int(i + 2) in g_blue_list) and (int(i + 3) in g_blue_list):
            ball_list[i - 1].pencolor("red")
            ball_list[i].pencolor("red")
            ball_list[i + 1].pencolor("red")
            ball_list[i + 2].pencolor("red")
            scn.onclick(None)
            turtle.title("Winner! Player Blue")
        elif (int(i + 8) in g_blue_list) and (int(i + 16) in g_blue_list) and (int(i + 24) in g_blue_list):
            ball_list[i - 1].pencolor("red")
            ball_list[i + 7].pencolor("red")
            ball_list[i + 15].pencolor("red")
            ball_list[i + 23].pencolor("red")
            scn.onclick(None)
            turtle.title("Winner! Player Blue")
        if i not in [8, 16, 24, 32, 40, 48, 56, 64, 7, 15, 23, 31, 39, 47, 55, 63, 6, 14, 22, 30, 38, 46, 54, 62]:
            if (int(i + 9) in g_blue_list) and (int(i + 18) in g_blue_list) and (int(i + 27) in g_blue_list):
                ball_list[i - 1].pencolor("red")
                ball_list[i + 8].pencolor("red")
                ball_list[i + 17].pencolor("red")
                ball_list[i + 26].pencolor("red")
                scn.onclick(None)
                turtle.title("Winner! Player Blue")
        if i not in [3, 11, 19, 27, 35, 43, 51, 59, 2, 10, 18, 26, 34, 42, 50, 58, 1, 9, 17, 25, 33, 41, 49, 57]:
            if (int(i + 7) in g_blue_list) and (int(i + 14) in g_blue_list) and (int(i + 21) in g_blue_list):
                ball_list[i - 1].pencolor("red")
                ball_list[i + 6].pencolor("red")
                ball_list[i + 13].pencolor("red")
                ball_list[i + 20].pencolor("red")
                scn.onclick(None)
                turtle.title("Winner! Player Blue")    


def check_connect_purple():
    """
    Check whether purple wins.

    Return four connected purple balls with red border and heading "Winner! Player Purple".

        eg: Eligible situations include:
            (1)  (P ball) (P ball) (P ball) (P ball)

            (2)  (P ball)
                 (P ball)
                 (P ball)
                 (P ball)

            (3)  (P ball)
                        (P ball)
                                (P ball)
                                        (P ball)

            (4)                         (P ball)
                                (P ball)
                        (P ball)
                (P ball)                  
    """

    for i in g_purple_list:
        if (int(i + 1) in g_purple_list) and (int(i + 2) in g_purple_list) and (int(i + 3) in g_purple_list):
            ball_list[i - 1].pencolor("red")
            ball_list[i].pencolor("red")
            ball_list[i + 1].pencolor("red")
            ball_list[i + 2].pencolor("red")
            scn.onclick(None)
            turtle.title("Winner! Player Purple")
        elif (int(i + 8) in g_purple_list) and (int(i + 16) in g_purple_list) and (int(i + 24) in g_purple_list):
            ball_list[i - 1].pencolor("red")
            ball_list[i + 7].pencolor("red")
            ball_list[i + 15].pencolor("red")
            ball_list[i + 23].pencolor("red")
            scn.onclick(None)
            turtle.title("Winner! Player Purple")
        if i not in [8, 16, 24, 32, 40, 48, 56, 64, 7, 15, 23, 31, 39, 47, 55, 63, 6, 14, 22, 30, 38, 46, 54, 62]:
            if (int(i + 9) in g_purple_list) and (int(i + 18) in g_purple_list) and (int(i + 27) in g_purple_list):
                ball_list[i - 1].pencolor("red")
                ball_list[i + 8].pencolor("red")
                ball_list[i + 17].pencolor("red")
                ball_list[i + 26].pencolor("red")
                scn.onclick(None)
                turtle.title("Winner! Player Purple")
        if i not in [3, 11, 19, 27, 35, 43, 51, 59, 2, 10, 18, 26, 34, 42, 50, 58, 1, 9, 17, 25, 33, 41, 49, 57]:
            if (int(i + 7) in g_purple_list) and (int(i + 14) in g_purple_list) and (int(i + 21) in g_purple_list):
                ball_list[i - 1].pencolor("red")
                ball_list[i + 6].pencolor("red")
                ball_list[i + 13].pencolor("red")
                ball_list[i + 20].pencolor("red")
                scn.onclick(None)
                turtle.title("Winner! Player Purple")  


def check_tie():
    """
    Check whether the game tied

    Return the heading "Game Tied!" if the game tied.
    """

    if ball_on_tracker1 == ball_on_tracker2 == ball_on_tracker3 == ball_on_tracker4 == \
       ball_on_tracker5 == ball_on_tracker6 == ball_on_tracker7 == ball_on_tracker8 == 8:
        scn.onclick(None)
        turtle.title("Game Tied!")


def motion(event):
    """
    Track mouse movement.

    Return the x coordinate of the mouse.
    """
    
    global g_last_x
    x = event.x
    g_last_x = x
    tracker_frame(g_last_x)

"""
Generates eight trackers.
"""
eight_trackers()


"""
Combine mouse motion with the motion() function.
"""
g_canvas = turtle.getcanvas()
g_canvas.bind('<Motion>', motion)
scn.onscreenclick(land_which_tracker)
scn.listen()


scn.mainloop()
