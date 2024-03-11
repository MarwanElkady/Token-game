# File: File Name
# Purpose:
# "Subtracting Square" game is a two-player game where players take turns subtracting numbers from an initial starting number.
# The numbers they can subtract are limited to non-zero squared numbers. The objective is to strategically choose numbers in a way that forces the remaining number to reach 1.
# The player who takes the last square number wins the game.

# Author: Marwan ibraheem ismael - مروان ابراهيم اسماعيل ابراهيم
# ID: 20230378


# importing the library to make the programe gives a random number
import random


# this function to handel the part when the player choose if he want to enter the starting number by himself or he wants the game gives him the number
# also this function fix if the player enterd a wrong number or a string
def get_starting_number():
    choice = input(
        "Do you want to enter the starting number manually? (yes/no): "
    ).lower()
    if choice == "yes":
        num = int(input("Enter the starting number (between 100 and 200): "))
        if num > 200 or num < 100:
            print("Invalid entry. Please enter a number between 100 and 200.")
            return get_starting_number()
        else:
            return num
    elif choice == "no":
        return random.randint(100, 200)
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")
        return get_starting_number()


# this function is to check the user in-game choices if it more than the ramaning number or like this errors
def Check_Choice(Sqr_nm, strt_nm):
    while True:
        try:
            play = int(input("Enter your choice: "))
            if play in Sqr_nm and strt_nm - play >= 0:
                return play
            elif play > 200:
                print(
                    "Invalid choice! Please choose a number within the range of 1 to 200."
                )
            else:
                print(
                    "Invalid choice! Please choose a valid square number within the range of the remaining number."
                )
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# the main function of the game
def game():

    # the list of the non zero squared numbers
    Sqr_nm = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]

    # the greating meassage to inform the player by our game
    print("*" * 40)
    print("Welcome to our game 'Subtracting Square'")
    print("*" * 40)

    # this var to call the funvtion we make recently to get the starting number
    strt_nm = get_starting_number()

    # printning the started number
    print(f"Our starting number is: {strt_nm}")

    # a var to store the winning player in the end of the game
    winr = None

    # the while loop of the game
    while strt_nm > 1:
        print("Player 1's turn:")
        print(f"Choose from the following square numbers: {Sqr_nm}")
        play = Check_Choice(
            Sqr_nm, strt_nm
        )  # check if the choosen number is correct by calling back the function that responsible for that

        # if the choosen number is correct then we will subtract it from the starting number and print the remaining number aftr the subtraction
        strt_nm -= play
        print(f"The remaining number is: {strt_nm}")

        # if the choosen number by player 1 leads to make the reminded number is 1 so there is no need to make player 2 play as he already won
        if strt_nm == 1:
            winr = "Player 2"
            break

        print("Player 2 turn:")
        print(f"\n Choose from the following square numbers: {Sqr_nm}")
        play = Check_Choice(
            Sqr_nm, strt_nm
        )  # check if the choosen number is correct by calling back the function that responsible for that

        # if the choosen number is correct then we will subtract it from the starting number and print the remaining number aftr the subtraction
        strt_nm -= play
        print(f"The remaining number is: {strt_nm}")

        # if the choosen number by player 1 leads to make the reminded number is 1 so there is no need to make player 2 play as he already won
        if strt_nm == 1:
            winr = "Player 1"
            break
    # at the end of the game we printed the game over message to inform the user that the gmae ended
    print("Game over")

    # here we get the player who won the game and print it
    if winr:
        print(f"{winr} is the winner")


game()
