hrs = 0
mins = 0
time_of_day = 'am'

def convert_to_24_hour(hrs, mins, time_of_day):
    if time_of_day == 'am' or hrs == 12:
        time_of_day = 'pm'
        print(f"{hrs:02d}:{mins:02d} {time_of_day}")
    else:
        hrs += 12
        time_of_day = 'am'
        print(f"{hrs:02d}:{mins:02d} {time_of_day}")

def convert_to_12_hour(hrs, mins, time_of_day):
    if 12 <= hrs < 24:
        time_of_day = 'pm'
        print(f"{hrs:02d}:{mins:02d} {time_of_day}")
    elif 0 <= hrs < 12:
        time_of_day = 'am'
        print(f"{hrs:02d}:{mins:02d} {time_of_day}")

convert_to_24_hour(hrs, mins, time_of_day)
convert_to_12_hour(hrs, mins, time_of_day)
