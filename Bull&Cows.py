import random


def main() -> None:
    gen_number = generate_number()
    print(gen_number)

    user_input = ""
    guesses = 0

    while user_input != "exit":
        user_input = input("Enter a number")

        if user_input == "exit":
            break

        if validate_number(user_input) is True:
            guesses += 1
            if check_guess(user_input, gen_number) is True:
                print(f"Correct, you've guessed the right number in {str(guesses)} guesses!")
                break


def generate_number():
    gen_number = []
    i = 0
    while i <= 3:
        random_value = random.randrange(0, 9)
        if gen_number.count(random_value) == 0:
            gen_number.append(random_value)
            i += 1
    return gen_number


def validate_number(user_input):
    test_input = ""
    try:
        test_input = int(user_input)
    except ValueError:
        print("you must enter a number!")
        return False

    if len(user_input) != 4:
        print("number should be 4 digits long!")
        return False

    i = 0
    while i <= 3:
        if user_input.count(user_input[i]) != 1:
            print("don't use duplicate digits in you number!")
            return False
        i += 1
    return True


def check_guess(user_input, gen_number):
    i = 0
    bulls = 0
    cows = 0
    while i <= 3:
        if gen_number[i] == int(user_input[i]):
            bulls += 1
        elif int(user_input[i]) in gen_number:
            cows += 1
        i += 1

    print(f"{str(bulls)} bulls, {str(cows)} cows")

    if bulls == 4:
        return True
    else:
        return False


main()
