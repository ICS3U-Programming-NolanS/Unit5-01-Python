#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Nov 20 2022
# This program converts the temperature from celsius (°C) to fahrenheit (°F).


def calculate_fahrenheit():
    # get the user's temperature in celsius
    celsius_temp_string = input("Please enter the temperature in celsius (°C): ")
    print("")

    try:
        # converts string into float
        celsius_temp_float = float(celsius_temp_string)
        # convert user input from celsius to fahrenheit
        fahrenheit_temp = (9.0 / 5.0) * celsius_temp_float + 32
        print(
            "{:,.2f}°C in fahrenheit is: {:,.2f}°F".format(
                celsius_temp_float, fahrenheit_temp
            )
        )

    # checks if the number is a string
    except Exception:
        print("{} is not a number...please enter a number!".format(celsius_temp_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
