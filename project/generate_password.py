#generate_password

import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digits + special_chars

    if not all_chars:
        raise ValueError("At least one character type must be selected")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

# Start the password generator
main()
