#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import math


def rounder(pass_by_reference, decimals_number):
    # function adds 1, by reference

    ten_times = 10**decimals_number
    pass_by_reference[0] = pass_by_reference[0] * ten_times
    pass_by_reference[0] = pass_by_reference[0] + 0.5
    pass_by_reference[0] = int(pass_by_reference[0])
    pass_by_reference[0] = pass_by_reference[0] / ten_times


def main():
    # this function gets a number and calls the add_one function

    pass_by_reference = []
    # input
    str_decimals_number = input("Input number of decimals: ")
    str_number = input("Input number: ")
    try:
        number = float(str_number)
        decimals_number = int(str_decimals_number)
        pass_by_reference.append(number)
        rounder(pass_by_reference, decimals_number)
        print("\nRounded number is: {0}".format(pass_by_reference[0]))
    except Exception:
        print("\nInvalid Input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
