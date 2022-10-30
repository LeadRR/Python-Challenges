# Degree Celsius to Fahrenheit and Kelvin converter

import sys

celsius = float(sys.argv[1])


def ctof(x):
    return (x * 9 / 5) + 32


def ctok(x):
    return x + 273.15


print(f"{celsius}°C =", f"{ctof(celsius)}°F =", f"{ctok(celsius)}K")

# Celsius to Fahrenheit = (°C × 9/5) + 32
# Celsius to Kelvin = °C + 273.15
