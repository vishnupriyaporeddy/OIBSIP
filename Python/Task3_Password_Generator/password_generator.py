
import secrets
import string


def generate_password(length, use_digits, use_symbols):

    characters = string.ascii_letters
    password = []

    # Add at least one number if selected
    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    # Add at least one symbol if selected
    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    # Fill the remaining positions
    for i in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


print("====================================")
print("       RANDOM PASSWORD GENERATOR")
print("====================================")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password must contain at least 8 characters.")
            continue

        digits = input("Include numbers? (yes/no): ").lower()
        symbols = input("Include symbols? (yes/no): ").lower()

        if digits not in ["yes", "no"] or symbols not in ["yes", "no"]:
            print("Please enter yes or no.")
            continue

        use_digits = digits == "yes"
        use_symbols = symbols == "yes"

        if not use_digits and not use_symbols:
            print("Select at least one: numbers or symbols.")
            continue

        password = generate_password(
            length, use_digits, use_symbols
        )

        print("\nGenerated Password:", password)
        print("Password Length:", len(password))

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for using the Password Generator!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")
