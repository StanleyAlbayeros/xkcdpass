import json
import random
from config import (num_words, padding_symbol, separator, num_passwords, start_case)

def load_words_and_organize_by_length():
    """Loads words from a JSON file and organizes them by length."""
    with open('words.json', 'r') as file:
        words_dict = json.load(file)
    # Organize words by length
    words_by_length = {}
    for word in words_dict.keys():
        word_length = len(word)
        if word_length not in words_by_length:
            words_by_length[word_length] = [word]
        else:
            words_by_length[word_length].append(word)
    return words_by_length

def select_word(words_by_length, desired_length, is_upper):
    """Selects a random word of the desired length from the organized dictionary and applies case transformation."""
    if desired_length in words_by_length:
        word = random.choice(words_by_length[desired_length])
        return word.upper() if is_upper else word.lower()
    else:
        return None  # Or handle the absence of words of the desired length differently

def generate_password(words_by_length, num_words, padding, sep, start_case, word_lengths):
    """Generates a password based on the specified parameters, alternating case."""
    words = []
    is_upper = (start_case == "upper")
    for length in word_lengths:
        word = select_word(words_by_length, length, is_upper)
        if word:  # Ensure a word was found
            words.append(word)
            is_upper = not is_upper  # Alternate case
    return padding + sep.join(words) + padding

if __name__ == "__main__":
    # Load words and organize them by length
    words_by_length = load_words_and_organize_by_length()
    # Define desired lengths for each word in the password
    word_lengths = [4, 5, 6]  # Example: Generate passwords from words of lengths 4, 5, and 6
    passwords = [generate_password(words_by_length, num_words, padding_symbol, separator, start_case, word_lengths)
                 for _ in range(num_passwords)]
    print("\n".join(passwords))
