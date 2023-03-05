import datetime, calendar

def get_percentage_left(reset_day) -> float:
    # If the reset day is greater than 28, set it to 28
    if reset_day > 28:
        reset_day = 28
    # Get the current day of the month
    now = datetime.datetime.now()
    # Get the number of days in the month this cycle
    if reset_day > now.day:
        days_in_month = calendar.monthrange(now.year, now.month - 1)[1]
    else:
        days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate days left in the cycle
    if reset_day > now.day:
        days_left = reset_day - now.day
    else:
        days_left = days_in_month - now.day + reset_day

    # Calculate percentage left in the cycle
    percent_left = 100 / days_in_month * (days_left - 1)

    return percent_left