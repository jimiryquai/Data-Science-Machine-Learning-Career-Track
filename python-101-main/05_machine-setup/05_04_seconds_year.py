# Use the interpreter to calculate how many seconds are in a year.
# Then write the code in this script file below this line.

# calculate seconds in a year
def seconds_in_a_year():
    seconds_in_a_minute = 60
    minutes_in_an_hour = 60
    hours_in_a_day = 24
    days_in_a_year = 365
    return seconds_in_a_minute * minutes_in_an_hour * hours_in_a_day * days_in_a_year

print(seconds_in_a_year())
