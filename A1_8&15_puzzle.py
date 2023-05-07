"""
This is an 8/15 puzzle game written in python.
Users can choose the puzzle type and use custom keys to play.
"""
import random
import sys


a = ""  # letter use for four moving directions.
d = ""
w = ""
s = ""
small_puzzle_list = []  # Lists that include the disorder elements in initial 8 or 15 puzzle.
large_puzzle_list = []
eight_move = ""  # The sliding direction for 8 or 15 move.
fifteen_move = ""
sol8 = ""  # The prompt of the direction for the next 8 or 15 puzzle slide.
sol15 = ""
step8 = 0  # Steps for eight_puzzle or fifteen_puzzle.
step15 = 0


"""Give users a brief introduction to the program."""
print("\nWelcome to python layman's puzzle game, you will be prompted :)")
print("This is a 8 or 15-tile puzzle game, use your wisdom to slide and solve the problem!\n")


def letter_input():
    """
    Ask for the letters to represent the sliding direction.

    Return letters that represent each sliding direction.
    """

    global a, d, w, s
    a = input("Enter the letter used for Left move: ")
    d = input("Enter the letter used for Right move: ")
    w = input("Enter the letter used for Up move: ")
    s = input("Enter the letter used for Down move: ")
    a = a.lower()
    d = d.lower()
    w = w.lower()
    s = s.lower()
    return a, d, w, s


def whether_alpha(user_input):
    """
    Judge whether the input is letter.

    Return False if is letter, else return True.
    """
    
    if user_input.isalpha():
        return False
    else:
        return True    


def whether_same():
    """
    Judge whether user use the same letter to represent two or more slide.

    Return False if the input has the same number, else return True.
    """

    letter_list = [a, d, w, s]
    k = -1
    same_number = 0
    for i in letter_list:
        k += 1
        for j in letter_list[k + 1:4]:
            if i == j:
                same_number += 1
    if same_number != 0:
        return False
    else:
        return True


def get_inv_count8(array):
    """
    This function count inversions in given 8 puzzle.

    Return the inversion count number.
    """

    inversion_count = 0
    empty_value = ' '
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if array[j] != empty_value and array[i] != empty_value and array[i] > array[j]:
                inversion_count += 1
    return inversion_count


def is_solvable8(puzzle):
    """
    Check if a given instance of 8-puzzle is solvable or not.

    Return True if solvable.
    """

    e_puzzle = []
    for i in puzzle:
        e_puzzle.append(str(i))
    inversion_count = get_inv_count8([j for sub in e_puzzle for j in sub])
    return inversion_count % 2 == 0


def get_inv_count15(array):
    """
    This function count inversions in given 15 puzzle.

    Return the inversion count number.
    """

    inversion_count = 0
    empty_value = ' '
    for i in range(0, 16):
        for j in range(i + 1, 16):
            if array[j] != empty_value and array[i] != empty_value and array[i] > array[j]:
                inversion_count += 1
    return inversion_count


def is_solvable15(puzzle):
    """
    Check if a given instance of 15-puzzle is solvable or not.

    Return True if solvable.
    """

    f_puzzle = []
    for i in puzzle:
        f_puzzle.append(str(i))
    inversion_count = get_inv_count15([j for sub in f_puzzle for j in sub])
    return inversion_count % 2 != 0


def eight_puzzle():
    """
    Randomly create the initial 3*3 solvable eight_puzzle situation.

    Return the initial 3*3 solvable eight_puzzle situation. 
        e.g     1       2
                8   7   3
                5   4   6
    """

    global small_puzzle_list
    small_nums = random.sample(range(1, 9), 8)
    hollow = [' ']
    small_puzzle_list = small_nums + hollow
    random.shuffle(small_puzzle_list)
    t = 0
    if is_solvable8(small_puzzle_list):
        print("\n")
        print("A solvable puzzle has created, now start your try\n")
        for i in small_puzzle_list:
            t += 1
            if t % 3 == 0:
                print("%3s" % str(i))
            else:
                print("%3s" % str(i), end=" ")
        print("\n")
    else:
        eight_puzzle()


def fifteen_puzzle():
    """
    Randomly create the initial 4*4 solvable fifteen_puzzle situation.

    Return the initial 4*4 solvable fifteen_puzzle situation.
        e.g     7   9   6   13
                8   3   4   2
                1   5   11  14
                10      12  15
    """

    global large_puzzle_list
    large_nums = random.sample(range(1, 16), 15)
    hollow = [' ']
    large_puzzle_list = large_nums + hollow
    random.shuffle(large_puzzle_list)
    if is_solvable15(large_puzzle_list):
        print("\n")
        print("A solvable puzzle has created, now start your try\n")
        for i in range(len(large_puzzle_list)):
            if (i + 1) % 4 == 0:
                print("%-3s" % str(large_puzzle_list[i]))
            else:
                print("%-3s" % str(large_puzzle_list[i]), end=" ")
        print("\n")
    else:
        fifteen_puzzle()


def eight_puzzle_empty_position():
    """
    Prompt the direction of the next slide for eight_puzzle.

    Return the Prompt.
        e.g. If the puzzle is:

            1       2      
            8   7   3
            5   4   6

        the prompt is: (left-a, right-d, up-w).          
    """

    global sol8
    location8 = small_puzzle_list.index(" ")
    if location8 == 0:
        sol8 = "(left-" + a + ", " + "up-" + w + ")"
    elif location8 == 1:
        sol8 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ")"
    elif location8 == 2:
        sol8 = "(right-" + d + ", " + "up-" + w + ")"
    elif location8 == 3:
        sol8 = "(left-" + a + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location8 == 4:
        sol8 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location8 == 5:
        sol8 = "(right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location8 == 6:
        sol8 = "(left-" + a + ", " + "down-" + s + ")"
    elif location8 == 7:
        sol8 = "(left-" + a + ", " + "right-" + d + ", " + "down-" + s + ")"
    elif location8 == 8:
        sol8 = "(right-" + d + ", " + "down-" + s + ")"
    return sol8


def fifteen_puzzle_empty_position():
    """
    Prompt the direction of the next slide for fifteen_puzzle.

    Return the prompt.
        e.g. If the puzzle is:

            7   9   6   13
            8   3   4   2
            1   5   11  14
            10      12  15

        the prompt is: (left-a, right-d, down-s).       
    """

    global sol15
    location15 = large_puzzle_list.index(" ")
    if location15 == 0:
        sol15 = "(left-" + a + ", " + "up-" + w + ")"
    elif location15 == 1:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ")"
    elif location15 == 2:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ")"
    elif location15 == 3:
        sol15 = "(right-" + d + ", " + "up-" + w + ")"
    elif location15 == 4:
        sol15 = "(left-" + a + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 5:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 6:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 7:
        sol15 = "(right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 8:
        sol15 = "(left-" + a + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 9:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 10:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 11:
        sol15 = "(right-" + d + ", " + "up-" + w + ", " + "down-" + s + ")"
    elif location15 == 12:
        sol15 = "(left-" + a + ", " + "down-" + s + ")"
    elif location15 == 13:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ")"
    elif location15 == 14:
        sol15 = "(left-" + a + ", " + "right-" + d + ", " + "up-" + w + ")"
    elif location15 == 15:
        sol15 = "(right-" + d + ", " + "down-" + s + ")"
    return sol15


def eight_puzzle_move():
    """
    Adjust the number position in the eight_puzzle graphics according to the slide.

    Return "invalid direction" if the direction of slide is wrong.
        e.g.
            If the puzzle is:

                1       2      
                8   7   3
                5   4   6

            and you input "s", it wil return "invalid direction".

    Return to choose the puzzle type if the user successfully solves the puzzle.
    """

    global step8
    global eight_move
    global small_puzzle_list
    eight_puzzle_empty_position()
    if step8 == 0:
        eight_move = input("Enter your move" + sol8 + ": ")
        eight_move = eight_move.lower()
        step8 += 1
    else:
        step8 += 1
        loc = small_puzzle_list.index(' ')
        if eight_move == a:
            if loc == 2:
                print("\ninvalid direction\n")
            elif loc == 5:
                print("\ninvalid direction\n")
            elif loc == 8:
                print("\ninvalid direction\n")
            else:
                small_puzzle_list[loc], small_puzzle_list[loc + 1] = small_puzzle_list[loc + 1], small_puzzle_list[loc]
                print_8()
        elif eight_move == d:
            if loc == 0:
                print("\ninvalid direction\n")
            elif loc == 3:
                print("\ninvalid direction\n")
            elif loc == 6:
                print("\ninvalid direction\n")
            else:
                small_puzzle_list[loc], small_puzzle_list[loc - 1] = small_puzzle_list[loc - 1], small_puzzle_list[loc]
                print_8()
        elif eight_move == w:
            if loc == 6:
                print("\ninvalid direction\n")
            elif loc == 7:
                print("\ninvalid direction\n")
            elif loc == 8:
                print("\ninvalid direction\n")
            else:
                small_puzzle_list[loc], small_puzzle_list[loc + 3] = small_puzzle_list[loc + 3], small_puzzle_list[loc]
                print_8()
        elif eight_move == s:
            if loc == 0:
                print("\ninvalid direction\n")
            elif loc == 1:
                print("\ninvalid direction\n")
            elif loc == 2:
                print("\ninvalid direction\n")
            else:
                small_puzzle_list[loc], small_puzzle_list[loc - 3] = small_puzzle_list[loc - 3], small_puzzle_list[loc]
                print_8()
        else:
            print("\ninvalid input\n")        
        eight_puzzle_empty_position()
        if small_puzzle_list != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
            eight_move = input("Enter your move" + sol8 + ": ")
            eight_move = eight_move.lower()
    if small_puzzle_list != [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        return eight_puzzle_move()
    elif small_puzzle_list == [1, 2, 3, 4, 5, 6, 7, 8, ' ']:
        step8 = int(step8) - 1
        step8 = str(step8)
        print("CONGRATULATIONS! You have solved the problem, your total step is " + step8)
        step8 = 0
        p_type()
        return True


def print_8():
    """
    Output the 8_puzzle after sliding.

    Return the 8_puzzle after sliding.
        e.g.
            If the puzzle is:

                1       2
                8   7   3
                5   4   6

            and you input "w", it wil return:

            
                1   7   2
                8       3
                5   4   6
    """

    print("\n")
    for i in range(len(small_puzzle_list)):
        if (i + 1) % 3 == 0:
            print("%3s" % str(small_puzzle_list[i]))
        else:
            print("%3s" % str(small_puzzle_list[i]), end=" ")
    print("\n")


def fifteen_puzzle_move():
    """
    Adjust the number position in the eight_puzzle graphics according to the slide.

    Return "invalid direction" if the direction of slide is wrong.
        e.g.
            If the puzzle is:

                7   9   6   13
                8   3   4   2
                1   5   11  14    
                10      12  15

            and you input "w", it wil return "invalid direction".

    Return to choose the puzzle type if the user successfully solves the puzzle.
    """

    global step15
    global fifteen_move
    global large_puzzle_list
    fifteen_puzzle_empty_position()
    if step15 == 0:
        fifteen_move = input("Enter your move" + sol15 + ": ")
        fifteen_move = fifteen_move.lower()
        step15 += 1
    else:
        step15 += 1
        loc = large_puzzle_list.index(' ')
        if fifteen_move == a:
            if loc == 3:
                print("\ninvalid direction\n")
            elif loc == 7:
                print("\ninvalid direction\n")
            elif loc == 11:
                print("\ninvalid direction\n")
            elif loc == 15:
                print("\ninvalid direction\n")
            else:
                large_puzzle_list[loc], large_puzzle_list[loc + 1] = large_puzzle_list[loc + 1], large_puzzle_list[loc]
                print_15()
        elif fifteen_move == d:
            if loc == 0:
                print("\ninvalid direction\n")
            elif loc == 4:
                print("\ninvalid direction\n")
            elif loc == 8:
                print("\ninvalid direction\n")
            elif loc == 12:
                print("\ninvalid direction\n")
            else:
                large_puzzle_list[loc], large_puzzle_list[loc - 1] = large_puzzle_list[loc - 1], large_puzzle_list[loc]
                print_15()
        elif fifteen_move == w:
            if loc == 12:
                print("\ninvalid direction\n")
            elif loc == 13:
                print("\ninvalid direction\n")
            elif loc == 14:
                print("\ninvalid direction\n")
            elif loc == 15:
                print("\ninvalid direction\n")
            else:
                large_puzzle_list[loc], large_puzzle_list[loc + 4] = large_puzzle_list[loc + 4], large_puzzle_list[loc]
                print_15()
        elif fifteen_move == s:
            if loc == 0:
                print("\ninvalid direction\n")
            elif loc == 1:
                print("\ninvalid direction\n")
            elif loc == 2:
                print("\ninvalid direction\n")
            elif loc == 3:
                print("\ninvalid direction\n")
            else:
                large_puzzle_list[loc], large_puzzle_list[loc - 4] = large_puzzle_list[loc - 4], large_puzzle_list[loc]
                print_15()
        else:
            print("\ninvalid input\n") 
        fifteen_puzzle_empty_position()
        if large_puzzle_list != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']:
            fifteen_move = input("Enter your move" + sol15 + ": ")
            fifteen_move = fifteen_move.lower()
    if large_puzzle_list != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']:
        return fifteen_puzzle_move()
    elif large_puzzle_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ' ']:
        step15 = int(step15) - 1
        step15 = str(step15)
        print("CONGRATULATIONS, you have solved the problem, your total step is " + step15)
        step15 = 0
        p_type()
        return True


def print_15():
    """
    Output the 15_puzzle after sliding.

    Return the 15_puzzle after sliding.
        e.g.
            If the puzzle is:

                7   9   6   13
                8   3   4   2
                1   5   11  14    
                10      12  15

            and you input "s", it wil return:

                7   9   6   13
                8   3   4   2
                1       11  14
                10  5   12  15
    """

    print("\n")
    for i in range(len(large_puzzle_list)):
        if (i + 1) % 4 == 0:
            print("%-3s" % str(large_puzzle_list[i]))
        else:
            print("%-3s" % str(large_puzzle_list[i]), end=" ")
    print("\n")


def p_type():
    """
    Let the user choose the puzzle type or quit.

    Return the puzzle that the user choose.

    Will be returned if the user solves the puzzle.
    """

    while True:
        puzzle_type = input("\nEnter \"1\" for 8-puzzle, \"2\" for 15-puzzle or \"q\" to end the game: ")
        if puzzle_type == "q":
            print("\nThanks for playing and have a nice day!")
            sys.exit()
        elif puzzle_type == "1":
            eight_puzzle()
            eight_puzzle_move()
            break
        elif puzzle_type == "2":
            fifteen_puzzle()
            fifteen_puzzle_move()
            break
        else:
            print("\nPlease input \"1\", \"2\" or \"q\"")


while True:
    """
    Judge whether the letters that represent the sliding direction meets the requirements.

    Sentence will be printed if there is wrong input.
        Circumstances that do not meet the requirements include:
            1. Some of the input are not letters.  
            2. Some of the input are same.
            3. Use more than one letter to represent one direction.
    """

    letter_input()
    if whether_alpha(a) or whether_alpha(d) or whether_alpha(w) or whether_alpha(s):
        print("\nATTENTION: letter only\n")
    elif len(a) == len(d) == len(w) == len(s) == 1 and whether_same():
        break
    elif whether_same() is False:
        print("\nATTENTION: The four letters should be different\n")
    else: 
        print("\nATTENTION: Only use single letter to represent the step of each direction\n")


"""Let the user choose the puzzle type or quit."""
p_type()
