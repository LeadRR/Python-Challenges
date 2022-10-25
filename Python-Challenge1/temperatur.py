# Degree Celsius to Fahrenheit and Kelvin converter

import argparse

parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit and Kelvin')
parser.add_argument('celsius', metavar='celsius', type=int, help='Enter the Temperature value in Celsius')
args = parser.parse_args()

celsius = args.celsius


def ctof(celsius):
    return (celsius * 9 / 5) + 32


def ctok(celsius):
    return celsius + 273.15


print(f"{celsius}°C =", f"{ctof(celsius)}°F =", f"{ctok(celsius)}K")

# Celsius to Fahrenheit = (°C × 9/5) + 32
# Celsius to Kelvin = °C + 273.15
