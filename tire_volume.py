# Exceeded requirements by adding prices for more tire sizes from user input using conditionals.

import math
import datetime

print("Tire Volume Calculator")
print("----------------------")

# Get input from user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate result
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display result
print()
print("The approximate volume is", round(volume, 2), "liters")

# Get current date
current_date = datetime.date.today()

with open("volumes.txt", "a") as file:
    file.write(f"{current_date} {width} {aspect_ratio} {diameter} {round(volume, 2)}\n")

# Tire prices
tire_prices = {
    (205, 60, 15): 75.99,
    (215, 60, 16): 85.99,
    (225, 65, 17): 95.50,
    (235, 55, 18): 105.99,
}

# Price from user input
if (width, aspect_ratio, diameter) in tire_prices:
    price = tire_prices[(width, aspect_ratio, diameter)]
    print(f"\nThe price is ${price:.2f}.")
else:
    print("\nSorry, no price available.")