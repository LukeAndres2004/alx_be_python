import datetime

def display_current_datetime():
    current_date=datetime.datetime.now()
    current_date=current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)

def calculate_future_date(days_ahead):
    future_date=datetime.datetime.now() + datetime.timedelta(days=days_ahead)
    future_date=future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date and time after {days_ahead} days:", future_date)   

def main():
    display_current_datetime()
    days=int(input("Enter number of days to add: "))
    calculate_future_date(days)
if __name__ == "__main__":
    main()