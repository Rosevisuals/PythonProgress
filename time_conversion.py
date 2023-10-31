# Time Conversion Program

hrs = 12
mins = 00
time_of_day = 'pm'

# function to accept input from user

def  convert_to_24_hour(hrs, mins, time_of_day):
    # function to convert to 24 hour time
    if (time_of_day == 'am' or hrs == 12):
        time_of_day = 'hrs'
        print(f"{hrs} {mins} {time_of_day}")
    else:
        hrs += 12
        time_of_day = 'hrs'
        print(f"{hrs} {mins} {time_of_day}")

def convert_to_12_hour(hrs, mins, time_of_day="hrs"):
    # function to convert to 12 hr
    if (00 <= hrs <= 12):
        time_of_day = 'am'
        print(f"{hrs} {mins} {time_of_day}")
    if (12 < hrs <= 24):
        hrs -= 12
        time_of_day = 'pm'
        print(f"{hrs} : {mins} {time_of_day}")


convert_to_24_hour(hrs, mins, time_of_day)


