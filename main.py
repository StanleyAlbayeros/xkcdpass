import json
import random

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
        import config
        print("Configuration loaded from config.py.")
        return {
            'num_words': config.num_words,
            'padding_symbol': config.padding_symbol,
            'separator': config.separator,
            'num_passwords': config.num_passwords,
            'start_case': config.start_case,
            'word_length': config.word_length  # Ensure word_length is defined in config.py
        }
    except ImportError:
        print("config.py not found.")
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
        'word_length': int(input("Word length: "))  # Ask for word length
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
    passwords = []
    for _ in range(config['num_passwords']):
        words = []
        is_upper = config['start_case'] == 'upper'
        for _ in range(config['num_words']):
            # Use the specified word_length for all words
            words.append(select_word(words_by_length, config['word_length'], is_upper))
            is_upper = not is_upper  # Alternate case
        passwords.append(config['padding_symbol'] + config['separator'].join(words) + config['padding_symbol'])
    return passwords

if __name__ == "__main__":
    use_config = query_yes_no("Do you want to load settings from config.py?")
    if use_config:
        config = load_config()
        if not config:  # Fallback to manual config if config.py couldn't be loaded
            config = input_config()
    else:
        config = input_config()

    words_by_length = load_words_and_organize_by_length()
    passwords = generate_password(words_by_length, config)
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)
