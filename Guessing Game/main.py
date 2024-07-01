"""
Word Guessing Game - Main Module

This module serves as the entry point for the Word Guessing Game. It handles
command-line arguments and initiates the game.

Usage:
    python main.py word_list.json
"""

import argparse
from game import WordGuessingGame
from utils import get_valid_integer_input

def main():
    """
    Main function to set up and run the Word Guessing Game.

    This function parses command-line arguments, prompts for the number of
    players and words, and initiates the game.
    """
    parser = argparse.ArgumentParser(description="Word Guessing Game")
    parser.add_argument("words_file", type=str, help="path to the JSON file containing the list of words")
    args = parser.parse_args()

    num_players = get_valid_integer_input("Enter the number of players: ")
    num_games = get_valid_integer_input("Enter the number of words to guess: ")

    game = WordGuessingGame(args.words_file, num_players, num_games)
    game.play_game()

if __name__ == "__main__":
    main()