#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on April 2022
# This program
def main():
    # this function

    # input
    print("This program tells the user whether a number is odd or even")
    user_integer_string = input("Enter a number: ")

    # process & output
    try:
        user_integer = int(user_integer_string)

        if user_integer % 2 == 0:
            print("The number is an even number.")
        else:
            print("The number is an odd number.")
    except Exception:
        print("Invalid integer entered, please try again.")
    print("Done.")


if __name__ == "__main__":
    main()
