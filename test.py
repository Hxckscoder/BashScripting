# import random
# import string

# def character(Options):

#     print ("Choose what kind of password you want to be Generated")
#     print ("1. All ")
#     print ("2. Letters ")
#     print ("3. Digits ")
#     print ("4. Letters and Digits ")
#     print ("5. Letters and Digits and Punctuation ")

#     character = raw_input("> ")
#     if character == "1" or "All":
#             character = All
#         print "All"

#     elif character == "2" or "Letters":
#             character = Letters
#         print "Letters"

#     elif character == "3" or "Digits":
#             character = Digits
#         print "Digits"
#     elif character == "4" or "Letters and Digits"
#             character = Letters and Digits
#         print "Letters and Digits"
#     elif character == "5" or "Letters and Digits and Punctuation"
#             character = Letters and Digits and Punctuation
#         print "Letters and Digits and Punctuation"
#     else:
#         print "All, Letters, Digits, Letters and Digits, Letters and Digits and Punctuation"
# def generate_password(length, mode):
#     """Generates a random password of the given length and type."""
#     # Define the characters that can be used in the password based on the mode
#     if mode == "letters":
#         characters = string.ascii_letters
#     elif mode == "digits":
#         characters = string.digits
#     elif mode == "letters_digits":
#         characters = string.ascii_letters + string.digits
#     elif mode == "letters_digits_punctuation":
#         characters = string.ascii_letters + string.digits + string.punctuation
#     else:
#         characters = string.ascii_letters + string.digits + string.punctuation

#     # Use the random module to generate a password of the desired length
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password

# # Get input from the user for the password length and mode
# length = int(input("Enter the password length: "))
# mode = input("Enter the password mode (all/letters/digits/letters_digits/letters_digits_punctuation): ")

# # Generate the password based on the input
# password = generate_password(length, mode)print("Your password is:", password)
import random
import string
import curses

def generate_password(length, mode):
    """Generates a random password of the given length and type."""
    # Define the characters that can be used in the password based on the mode
    if mode == "Letters":
        characters = string.ascii_letters
    elif mode == "Digits":
        characters = string.digits
    elif mode == "Letters and Digits":
        characters = string.ascii_letters + string.digits
    elif mode == "Letters and Punctuation":
        characters = string.ascii_letters + string.punctuation
    elif mode == "All":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError(f"Invalid mode '{mode}'")

    # Use the random module to generate a password of the desired length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Define the available password modes as a list
available_modes = ["All", "Letters", "Digits", "Punctuation", "Letters and Digits", "Letters and Punctuation"]

# Initialize curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()

# Print the available modes to the console
stdscr.addstr("Available password modes:\n")
for i, mode in enumerate(available_modes):
    stdscr.addstr(f"{i + 1}. {mode}\n")

# Prompt the user to choose a mode
choice = 1
while True:
    stdscr.move(choice - 1, 0)
    stdscr.clrtoeol()
    stdscr.addstr(choice - 1, 0, "->")
    c = stdscr.getch()
    if c == curses.KEY_UP:
        choice = max(1, choice - 1)
    elif c == curses.KEY_DOWN:
        choice = min(len(available_modes), choice + 1)
    elif c == ord('\n'):
        break

# Get the chosen mode
mode = available_modes[choice - 1]

# Prompt the user to enter a password length
stdscr.addstr("\nEnter the password length: ")
stdscr.refresh()
length = int(stdscr.getstr().decode())

# Generate the password using the chosen mode and length
password = generate_password(length, mode)

# Print the generated password to the console
stdscr.addstr(f"\nYour {mode.lower()} password of length {length} is:\n")
stdscr.addstr(f"{password}\n")

# Clean up curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
