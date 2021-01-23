import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_positions = dict()
board = list()

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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


def main():
    board = generate_board(6, 6)

if __name__ == "__main__":
    main()