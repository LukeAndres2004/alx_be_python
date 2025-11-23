from datetime import datetime, timedelta

def display_current_datetime():
    """Part 1: Display the current date and time in a nice format"""
    current_date = datetime.now()                    # Get current date & time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return formatted_date

def calculate_future_date(days_to_add):
    """Part 2: Calculate and display the future date after adding days"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"In {days_to_add} days, the date will be: {formatted_future}")
    return formatted_future

def main():
    print("Date & Time Program")
    print("=" * 40)
    
    # Part 1
    display_current_datetime()
    print()  # empty line for readability
    
    # Part 2
    while True:
        try:
            days = int(input("Enter the number of days to add to today: "))
            if days < 0:
                print("Please enter a positive number or zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer (e.g. 0, 5, 30)")
    
    calculate_future_date(days)

# Run the program
if __name__ == "__main__":
    main()

