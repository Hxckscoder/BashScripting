import random
import string

def generate_password(length, mode):
    """Generates a random password of the given length and type."""
    # Define the characters that can be used in the password based on the mode
    if mode == "letters":
        characters = string.ascii_letters
    elif mode == "digits":
        characters = string.digits
    elif mode == "letters_digits":
        characters = string.ascii_letters + string.digits
    elif mode == "letters_digits_punctuation":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    # Use the random module to generate a password of the desired length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get input from the user for the password length and mode
length = int(input("Enter the password length: "))
mode = input("Enter the password mode (all/letters/digits/letters_digits/letters_digits_punctuation): ")

# Generate the password based on the input
password = generate_password(length, mode)
print("Your password is:", password)
