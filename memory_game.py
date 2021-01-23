import os
import random
import copy
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_positions = dict()


# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_difficulty():

    diff =''
    print("1 - Easy \n 2 - Medium \n 3 - Hard")
    while diff not in ('1', '2', '3'):
        diff = input("Please choose difficulty: ")
    return diff

def get_random_letter():
    return alphabet[random.randrange(0, len(alphabet))]

def generate_possible_places(height, width):
    return [(x,y) for x in range(width) for y in range(height)]

def get_letter_position(possible_places):

    coordinates = random.choice(possible_places)

    return coordinates

def generate_board(height, width):

    board = [['#' for columns in range(width)] for rows in range(height)] # get empty board

    max_letters = height*width / 2 #determine how many letters do you need

    if (max_letters > len(alphabet)) or (max_letters % 2 != 0): # If the amount of letters is greater than the amount of letters in latin alphabet, raise a `ValueError`.
        raise ValueError
    else:
        max_letters = int(max_letters)
    
    letters = []

    for letter in range(max_letters):
        letters.append(get_random_letter())

# lets make it a dictionary with {letters: position1, position2}

    possible_places = generate_possible_places(height, width)

    for letter in letters:

        position1 = get_letter_position(possible_places)
        pos1_index = possible_places.index(position1)
        possible_places.pop(pos1_index)
        position2 = get_letter_position(possible_places)
        pos2_index = possible_places.index(position2)
        possible_places.pop(pos2_index)

        letters_positions[letter] = [position1, position2]

    return board

def print_board(board, shadow=False):

    console_clear()

    print(2*' ', end="")
    letters_to_use = alphabet[0:len(board[0])]
    for letter in letters_to_use:
        print(letter, end=" ")
    print('\n')

    for row in range(len(board)):
        print(row+1, end=' ')
        for x in board[row]:
            print(x, end=" ")
        print('')


def is_letternumber(move, letters, num_rows):

    column = move[0].upper()
    row = move[1:len(move)]

    if move == 'quit':
        exit()

    elif column not in letters:
        print('Your move is invalid. Please try again.')
        return False
    
    else:
        return True


def get_move(board):
    #determining board rows and cols
    num_rows = len(board)
    num_cols = len(board[0])

    #assigning letters to available rows
    letters = alphabet[:num_cols]
    
    validator = False

    while not validator:
        move = input(f"Please, pick a move from A to {letters[-1]} and from 1 to {num_cols-1}:")

        if is_letternumber(move, letters, num_rows):
            validator = True
            row = int(move[1:len(move)]) - 1
            col = alphabet.index(move[0].upper())
     
    return row, col


def board_revealed(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '#':
                return False
    return True

def main():
    
    endgame = False

    print("Welcome to Memory Game!")

    difficulty = choose_difficulty()

    diffic_base = {'1': (5,4), '2': (5,6), '3':(5,10)}

    width, height = diffic_base[difficulty]

    board = generate_board(width, height)

    move_counter = 0

    while not endgame: # endgame if all letters are revealed

        print_board(board)

        # go to revealing sequence
        row, col = get_move(board)

        tempboard = copy.deepcopy(board)

        lastguessed = row, col

        for key, value in letters_positions.items():
            if (row, col) in value:
                letter_to_reveal = key

        tempboard[row][col] = letter_to_reveal 

        print_board(tempboard)

        # reveal 2nd letter

        row, col = get_move(board)

        if (row, col) in lastguessed:
            row, col = get_move(board)

        for key, value in letters_positions.items():
            if (row, col) in value:
                second_letter_to_reveal = key

        tempboard[row][col] = second_letter_to_reveal

        print_board(tempboard)

        if letter_to_reveal == second_letter_to_reveal:
            board = tempboard
        else:
            time.sleep(1)

        if board_revealed(board):
            endgame = True

        move_counter += 1

    print("Goodbye!")

if __name__ == "__main__":
    main()