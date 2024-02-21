import json
import random
import config
import time
import logging


logging.basicConfig(level=logging.DEBUG)

# format logging: [L]evel - [D]ate and Time - [M]essage
logging.basicConfig(format='[%(levelname)s] - [%(asctime)s] - %(message)s')

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return the answer."""
    valid = {"yes": True, "y": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        logging.error(f"invalid default answer: '{default}'")
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt).lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")

def load_config():
    """Load configuration from config.py."""
    try:
        logging.info("Configuration loaded from config.py.")
        return {
            'num_words': config.num_words,
            'padding_symbol': config.padding_symbol,
            'separator': config.separator,
            'num_passwords': config.num_passwords,
            'start_case': config.start_case,
            'word_length': config.word_length
        }
    except ImportError:
        logging.error("config.py not found.")
        return None

def input_config():
    """Manually input configuration."""
    print("Manual configuration:")
    return {
        'num_words': int(input("Number of words: ")),
        'padding_symbol': input("Padding symbol: "),
        'separator': input("Separator: "),
        'num_passwords': int(input("Number of passwords: ")),
        'start_case': input("Start case ('lower' or 'upper'): "),
        'word_length': int(input("Word length: "))
    }

def load_words_and_organize_by_length():
    """Loads words from a JSON file and organizes them by length."""
    with open('words.json', 'r') as file:
        words_dict = json.load(file)
    words_by_length = {}
    for word in words_dict.keys():
        words_by_length.setdefault(len(word), []).append(word)
    return words_by_length

def select_word(words_by_length, desired_length, is_upper):
    """Selects a random word of the desired length and applies case transformation."""
    words = words_by_length.get(desired_length, [])
    if not words:
        return "NoWordFound"
    word = random.choice(words)
    return word.upper() if is_upper else word.lower()

def generate_password(words_by_length, config):
    """Generates passwords based on the configuration, using a uniform word length."""
    padding_symbol = config['padding_symbol']
    separator = config['separator']
    return [
        padding_symbol + separator.join([
            select_word(words_by_length, config['word_length'], is_upper)
            for is_upper in [config['start_case'] == 'upper'] * config['num_words']
        ]) + padding_symbol
        for _ in range(config['num_passwords'])
    ]

if __name__ == "__main__":
    logging.info("Password Generator started")
    use_config = query_yes_no("Do you want to load settings from config.py?")
    if use_config:
        config = load_config()
        if not config:
            config = input_config()
    else:
        config = input_config()
    
    logging.info(f"Configuration: {config}")

    words_by_length = load_words_and_organize_by_length()
    
    start_time = time.time()  # Start time

    passwords = generate_password(words_by_length, config)

    end_time = time.time()  # End time
    elapsed_time = end_time - start_time
    average_time_per_password = elapsed_time / config['num_passwords']

    logging.info("Generated Passwords")
    
    with open('passwords.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    logging.info("Passwords saved to passwords.txt")    
    logging.info(f"Elapsed Time: {elapsed_time} seconds")
    logging.info(f"Average Time per Generated Password: {average_time_per_password} seconds")