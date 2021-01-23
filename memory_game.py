import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_letter():
    return alphabet[random.randrange(0, len(alphabet))]

def main():
    # write your code here
    pass

if __name__ == "__main__":
    main()