#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This lets user guess a number

import random


def main():
    # This lets user guess a number
    random_number = random.randint(1, 9)  # a number between 1 and 9

    while True:
        guess_number = input("Enter a number between 1-9 : ")
        try:
            guess_number = int(guess_number)
            if guess_number == random_number:
                print("You guessed correctly!")
                break
            elif guess_number < random_number:
                print("You guessed too low")
            else:
                print("You guessed too high")
        except Exception:
            print("Invalid input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
