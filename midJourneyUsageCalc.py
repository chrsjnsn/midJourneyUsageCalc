import datetime, calendar

today = datetime.datetime.today()
days_in_month = calendar.monthrange(today.year, today.month)[1]
days_left = days_in_month - today.day
percentage_left = (days_left / days_in_month) * 100

print("Today is {} and there is {:.2f}% of the month left.".format(today.strftime("%B %d"), percentage_left))
