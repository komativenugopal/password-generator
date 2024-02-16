import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Please enter a positive integer for the password length.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and print the password
    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
