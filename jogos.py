import forca
import adivinhacao


def choose_game():
    print("**********")
    print("Welcome to the PlayRoom! Please, choose the game you want to play:")
    print("(1) The Guessing Game (2) The Hangman")

    game = int(input("Type your game: "))

    if game == 1:
        print("Running The Guessing Game")
        adivinhacao.play()
    elif game == 2:
        print("Running The Hangman")
        forca.play()

    print("**********")


if __name__ == "__main__":
    choose_game()
