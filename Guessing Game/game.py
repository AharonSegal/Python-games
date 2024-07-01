"""
Word Guessing Game - Game Module

This module contains the main game logic for the Word Guessing Game.
It includes the WordGuessingGame class which manages the game state and flow.
"""

import json
import random
from typing import List, Dict

class WordGuessingGame:
    """
    A class to represent the Word Guessing Game.

    This class manages the game state, including players, scores, and words.
    It also contains methods to play the game and manage rounds.
    """

    def __init__(self, words_file: str, num_players: int, num_games: int):
        """
        Initialize the Word Guessing Game.

        Args:
            words_file (str): Path to the JSON file containing words.
            num_players (int): Number of players in the game.
            num_games (int): Number of words to guess (rounds to play).
        """
        self.words_dict = self.load_words(words_file)
        self.words_bank = self.create_word_bank()
        self.num_players = num_players
        self.num_games = min(num_games, len(self.words_bank))
        self.players = []
        self.scores = []

    @staticmethod
    def load_words(file_path: str) -> Dict[str, List[str]]:
        """
        Load words from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Dict[str, List[str]]: Dictionary of categories and their associated words.

        Raises:
            SystemExit: If the file is not found or cannot be parsed.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading words file: {e}")
            exit(1)

    def create_word_bank(self) -> List[str]:
        """
        Create a list of unique words from all categories.

        Returns:
            List[str]: List of unique words.
        """
        return list({word.lower() for words_list in self.words_dict.values() for word in words_list})

    def setup_players(self):
        """
        Prompt for and store player names, ensuring uniqueness.
        """
        for i in range(self.num_players):
            while True:
                name = input(f"\nEnter name for player No. {i + 1}: ").strip()
                if name and name not in self.players:
                    self.players.append(name)
                    self.scores.append(0)
                    break
                print("Please enter a unique, non-empty name.")

    def play_game(self):
        """
        Main game loop. Sets up players and runs multiple rounds of word guessing.
        """
        print("\nWelcome to the Word Guessing Game!\n")
        self.setup_players()

        for game_number in range(1, self.num_games + 1):
            word = random.choice(self.words_bank)
            self.words_bank.remove(word)
            hint = next(key for key, value in self.words_dict.items() if word in value)

            print(f"\nGame No. {game_number}:")
            print(f"The category of the word is: {hint}")

            self.play_round(word, game_number)

        self.announce_winner()

    def play_round(self, word: str, game_number: int):
        """
        Play a single round of the game for a given word.

        Args:
            word (str): The word to be guessed.
            game_number (int): The current game number.
        """
        word_progress = ["_"] * len(word)
        used_letters = set()
        current_player = 0

        while '_' in word_progress:
            print(' '.join(word_progress))
            print(f"Letters guessed: {', '.join(sorted(used_letters))}")

            player = self.players[current_player]
            letter = input(f"\n{player}, enter a letter: ").lower().strip()

            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter.")
                continue

            if letter in used_letters:
                print("This letter has already been guessed.")
                continue

            used_letters.add(letter)

            if letter in word:
                print("Correct guess!")
                for i, char in enumerate(word):
                    if char == letter:
                        word_progress[i] = letter
                        self.scores[current_player] += 1
            else:
                print("Incorrect guess.")

            current_player = (current_player + 1) % self.num_players

        print(f"\nWord completed! The word was: {word.capitalize()}")
        self.print_scoreboard()

    def print_scoreboard(self):
        """
        Print the current scoreboard showing each player's points.
        """
        print("\nCurrent Scoreboard:")
        for player, score in zip(self.players, self.scores):
            print(f"{player}: {score} points")
        print()

    def announce_winner(self):
        """
        Determine and announce the winner(s) of the game.
        """
        print("\nGame Over!")
        high_score = max(self.scores)
        winners = [player for player, score in zip(self.players, self.scores) if score == high_score]

        print("\nFinal Scores:")
        for player, score in zip(self.players, self.scores):
            print(f"{player}: {score} points")

        if len(winners) == 1:
            print(f"\nThe winner is {winners[0]} with {high_score} points!")
        else:
            print(f"\nIt's a tie! The winners are {', '.join(winners)} with {high_score} points each!")