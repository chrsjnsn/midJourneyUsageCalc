from midJourneyUsageCalc import get_percentage_left

# Get the day of the month when your minutes reset
reset_day = int(input("Enter the day of the month when your minutes reset: "))

# Get the percentage left in the cycle
percent_left = get_percentage_left(reset_day)

# Print a formatted string telling the user how much percentage is left
print(f"You should have {percent_left:.2f}% left today to be on schedule.")