# Python program to convert temperature from Celsius to Fahrenheit and vice versa

# Function to convert degree celsius to fahrenheit
def celsius_to_fahrenheit(c):
    fahrenheit = c * (9/5) + 32
    return fahrenheit


# Function to convert degree fahrenheit to celsius
def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius


temp = float(input("Enter the temperature: "))
option = int(input("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius\n"))
if option == 1:
    print(temp, "°C = ", celsius_to_fahrenheit(temp), "°F")
elif option == 2:
    print(temp, "°F = ", fahrenheit_to_celsius(temp), "°C")
else:
    print("Invalid Option!")