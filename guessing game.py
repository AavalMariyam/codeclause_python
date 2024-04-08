import random

def provide_hint(number, guess):
    if number % 2 == 0:
        print("Hint: The number is divisible by 2.")
    if number % 3 == 0:
        print("Hint: The number is divisible by 3.")
    if number % 5 == 0:
        print("Hint: The number is divisible by 5.")
    if number % 7 == 0:
        print("Hint: The number is divisible by 7.")
    if guess > number:
        print("Hint: Guess lower!")
    else:
        print("Hint: Guess higher!")

def main():
    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 10. Try to guess it!")

    number_to_guess = random.randint(1, 10)
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")

        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
        else:
            provide_hint(number_to_guess, guess)

if __name__ == "__main__":
    main()
