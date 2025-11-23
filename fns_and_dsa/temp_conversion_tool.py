FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(farenheit):
    return (farenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_farenheit(celcius):
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32    
def get_valid_temperature(prompt):
    """Keep asking until user enters a valid number"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number (e.g. 98.6, -10, 212)")
def main():
    print("Temperature Converter")
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if choice == 'C':
        farenheit = get_valid_temperature("Enter the temperature to convert: ")
        celsius = convert_to_celsius(farenheit)
        print(f"{farenheit}°F is {celsius:.2f}°C")
    elif choice == 'F':
        celsius = get_valid_temperature("Enter the temperature to convert: ")
        farenheit = convert_to_farenheit(celsius)
        print(f"{celsius}°C is {farenheit:.2f}°F")
    else:
        raise ValueError ("Invalid choice. Please select 'C' or 'F'.")  
if __name__ == "__main__":
    main()




