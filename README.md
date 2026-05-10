# Python Text Encryptor

The Python Text Encryptor is a Python command‑line tool for symmetric encryption and decryption of text messages.
It uses the Fernet module from the cryptography library to ensure secure, symmetric encryption. The program allows users to generate an encryption key, encrypt a
plaintextmessage, and later decrypt it using the same key.

## Requirements
1. Python 3.6 or higher;
2. `Cryptography` library.

## Installation
1. Clone the repository (or download the script directly).
2. Install the required library:
    `pip install cryptography` or `pip3 install cryptography`

## Usage
1. Run the script from your terminal:
    `python python_text_encryptor.py` or `python3 python_text_encryptor.py`.

2. Then follow the interactive menu:
     - Generate a new key – Creates a symmetric Fernet key (displayed in the terminal);
     - Encrypt a message – Prompts for the key and the plaintext, then outputs the encrypted ciphertext;
     - Decrypt a message – Requests the key and the ciphertext, then shows the original plaintext;
     - Exit – Closes the application.

## Author

[Andrea De Vita](https://github.com/andreadevita99)

## License

All rights reserved. This project is provided for demonstration purposes only. No permission is granted to use, copy, modify, merge, publish, distribute, sublicense, or otherwise reproduce any part of this software without explicit written consent from the author. Unauthorized use, modification, or redistribution is strictly prohibited.
