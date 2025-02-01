import random
import string

def generate_password():
    # User input for password length
    length = int(input("Enter the desired password length: "))

    # Defining the character set (letters, digits, special characters)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print("\nGenerated Password:", password)

# Run the password generator
generate_password()
