# Password Hashing and Cracking Tool

## Project Overview
The Password Hashing and Cracking Tool allows users to:

- **Hash Passwords**: Users can input their password to receive its hashed version, which can be safely stored.
- **Crack Passwords**: Users can provide a hashed password and determine if it exists in a pre-defined list of common passwords, with optional salt usage.
- **User Interaction**: The tool prompts users to select whether they want to hash a password or crack an existing hash, guiding them through the process step-by-step.

This project showcases basic cryptographic functions in Python and demonstrates how to work with text files for storing known passwords and salts.

## Technologies Used
- **Python**: The primary programming language used for implementing the hashing and cracking logic.
- **hashlib**: A built-in Python library that provides a way to hash passwords using the SHA-1 algorithm.
- **Text Files**: Utilizes plain text files (`known-salts.txt` and `top-10000-passwords.txt`) to store salts and common passwords, enabling efficient password checking.
- **Command-Line Interface**: The tool is designed to run in a terminal or command prompt, providing a straightforward user experience.

