def fahrenheit_to_celsius(temp):
     fahrenheit_temp = (temp * 9/5) + 32
     return fahrenheit_temp
 
def celsius_to_fahrenheit (temp):
     celsius_temp = 5/9 *(temp - 32)
     return celsius_temp
 
unit = input("Enter the unit of your temperature (C or F): ").strip().upper()
temp = float(input("Enter the temperature to be converted: "))

if unit == 'C':
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result:.2f}°F")
elif unit == 'F':
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {result:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")