import os
import random
import copy

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

def get_letter_position(height, width):

        pos1_rows = random.randrange(0, width)
        pos1_cols = random.randrange(0, height)

        coordinates = pos1_rows, pos1_cols

        if coordinates in letters_positions.values():
            get_letter_position(height, width)
        else:
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

    for letter in letters:
        letter_1position = get_letter_position(height, width)
        letter_2position = get_letter_position(height, width)
        letters_positions[letter] = [letter_1position, letter_2position]

    return board

def print_board(board):

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
    for row in board:
        for col in board[row]:
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

        if board_revealed(board):
            endgame = True

        move_counter += 1

    print("Goodbye!")

if __name__ == "__main__":
    main()