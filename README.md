
# Secure Password Generator 🛡️

This Secure Password Generator is a Python-based CLI tool designed to create strong 🏋️‍♂️ and customizable passwords using words from the English dictionary 📚. It allows users to specify various parameters such as word length, the number of words, and separators to generate passwords that meet diverse security requirements.

## Features ✨

- Generates passwords composed of English dictionary words.
- Configurable word length, number of words, padding symbols, and separators.
- Option to load configuration from a `config.py` file or input parameters through CLI.
- Organizes words by length for efficient password generation.

## Installation 🚀

To set up the Secure Password Generator, clone this repository to your local machine:

```bash
git clone https://github.com/StanleyAlbayeros/xkcdpass
cd secure-password-generator
```

Ensure you have Python 3.x installed on your system. No additional external libraries are required as the script uses standard Python libraries.

## Usage 📖

To run the password generator, navigate to the repository directory and execute:

```bash
python main.py
```

You will be prompted to choose whether to load settings from `config.py`. Respond with `Y` to use predefined settings or `N` to input parameters manually.

### Configuration Options ⚙️

- `num_words`: Number of words in the password.
- `padding_symbol`: Symbol used for padding at the beginning and end.
- `separator`: Symbol used to separate words in the password.
- `num_passwords`: Number of passwords to generate.
- `start_case`: Case of the first word (`lower` or `upper`); subsequent words will alternate.
- `word_length`: Length of each word in the password.

These parameters can be defined in `config.py` for quick setup or inputted manually when prompted.

## Contributing 🤝

Contributions to the Secure Password Generator are welcome! Feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Credits and License 📜

This project uses a comprehensive list of English words sourced from [dwyl/english-words](https://github.com/dwyl/english-words), available under the [MIT license](https://opensource.org/licenses/MIT).

## License

[MIT](https://choosealicense.com/licenses/mit/)
