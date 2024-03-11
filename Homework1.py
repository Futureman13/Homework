from datetime import datetime
def get_days_from_today(date):
    now_days = datetime.now().toordinal()
    try:
        formatted_date = datetime.strptime(date,"%Y-%m-%d")
        days_date = formatted_date.toordinal()
        difference = now_days - days_date
        print(difference)
    except ValueError:
        print("Date entered incorrectly")
        date = input("Be careful and enter the day in format Year-month-day(ХХХ-MM-DD) :")
        get_days_from_today(date)

date = input("Enter the date (ХХХ-MM-DD) :")
get_days_from_today(date)