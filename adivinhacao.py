import random


def play():
    print("**********")
    print("Welcome to the guessing game!")
    print("**********")

    print("It's a very simple game. Just think about a number and take a guess. You got nothing to lose")

    secret_number = random.randrange(1, 101)
    total_of_attempts = 0
    points = 1000

    print("Choose the level you want to play: ")
    print("(1) Easy  (2) Medium  (3)Hard")

    level = int(input("Type the level: "))

    if level == 1:
        total_of_attempts = 20
    elif level == 2:
        total_of_attempts = 10
    else:
        total_of_attempts = 5

    for number_of_rounds in range(1, total_of_attempts + 1):
        print("Round {} of {}".format(number_of_rounds, total_of_attempts))
        guess_str = input("Take a guess between 1 and 100: ")
        print("You typed: ", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("You should type a number between 1 and 100")
            continue

        hit = guess == secret_number
        greater = guess > secret_number
        lower = guess < secret_number

        if hit:
            print("Congratulations, your guess is correct and you made {} points!".format(points))
            break

        else:
            if greater:
                print("You failed, your guess is greater then the secret number.")
            elif lower:
                print("You failed, your guess is lower then the secret number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("GAME OVER")


if __name__ == "__main__":
    play()

    # input define que algo tem que ser digitado
    # int(input("...")) significa que o que sera digitado sera um valor inteiro
