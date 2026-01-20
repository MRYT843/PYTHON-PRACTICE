import random
import string

def generate_password(length, include_numbers, include_symbols):
    # Base characters: letters
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")

    # Get user inputs
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 7:
                print("Invalid length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    try:
        while True:
            inc_num = input("Include numbers? (y/n): ").lower().strip()
            if inc_num in ['y', 'n']:
                include_numbers = inc_num == 'y'
                break
            else:
                print("Please enter y or n.")

        while True:
            inc_sym = input("Include symbols? (y/n): ").lower().strip()
            if inc_sym in ['y', 'n']:
                include_symbols = inc_sym == 'y'
                break
            else:
                print("Please enter y or n.")

        while True:
            try:
                num_passwords = int(input("How many passwords to generate? "))
                if num_passwords > 0:
                    break
                else:
                    print("Number of passwords must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("\nGenerated Passwords:")
        print("====================")
        for i in range(num_passwords):
            password = generate_password(length, include_numbers, include_symbols)
            print(f"{i+1}. {password}")

        # Feedback
        feedback = input("Please provide feedback on the generated passwords: ").strip()
        if not feedback:
            print("ok no problem")
        else:
            print("Thank you for your feedback!")

    except ValueError:
        print("Invalid input. Please enter numbers where required.")

if __name__ == "__main__":
    main()
