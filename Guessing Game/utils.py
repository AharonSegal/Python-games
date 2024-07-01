"""
Word Guessing Game - Utilities Module

This module contains utility functions used in the Word Guessing Game.
"""

def get_valid_integer_input(prompt: str, min_value: int = 1) -> int:
    """
    Prompt for and validate integer input.

    This function repeatedly prompts the user until a valid integer input
    is provided that meets the minimum value requirement.

    Args:
        prompt (str): The input prompt to display.
        min_value (int): The minimum acceptable value (default: 1).

    Returns:
        int: A valid integer input that meets the minimum value requirement.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Please enter a valid number.")