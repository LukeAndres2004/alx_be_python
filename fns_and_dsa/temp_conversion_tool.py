farenheit_to_celsius=5/9
celcius_to_farenheit=9/5
def convert_to_celsius(farenheit):
    return (farenheit - 32) * farenheit_to_celsius
def convert_to_farenheit(celcius):
    return (celcius * celcius_to_farenheit) + 32    
def main():
    print("Temperature Converter")
    choice = input("Convert to (C)elsius or (F)arenheit? ").strip().upper()
    if choice == 'C':
        farenheit = float(input("Enter temperature in Farenheit: "))
        celsius = convert_to_celsius(farenheit)
        print(f"{farenheit}°F is {celsius:.2f}°C")
    elif choice == 'F':
        celsius = float(input("Enter temperature in Celsius: "))
        farenheit = convert_to_farenheit(celsius)
        print(f"{celsius}°C is {farenheit:.2f}°F")
    else:
        print("Invalid choice. Please select 'C' or 'F'.")  
if __name__ == "__main__":
    main()
