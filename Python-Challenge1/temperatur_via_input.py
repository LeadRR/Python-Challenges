# Degree Celsius to Fahrenheit and Kelvin converter

try: # If somebody enters non nummers
    celsius = float(input("Enter temperature in °C: "))

    fahrenheit = round((celsius * 9 / 5) + 32, 1)
    kelvin = round(celsius + 273.15, 1)
    
    print(f"{celsius}°C = {fahrenheit}°F = {kelvin}Kelvin")
except ValueError:
    print("Please enter a number!")

# Celsius to Fahrenheit = (°C × 9/5) + 32
# Celsius to Kelvin = °C + 273.15
