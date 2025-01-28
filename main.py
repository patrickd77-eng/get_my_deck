# Clear the console
import os
os.system('cls' if os.name == 'nt' else 'clear')

#You should run this file to start the whole app. "py main.py". Check the readme first!
from core.deck_checker import check_deck
if __name__ == "__main__":
    check_deck()