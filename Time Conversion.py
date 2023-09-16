def timeConversion(time_12hr):
    # Split the input string into hours, minutes, seconds, and AM/PM
    time_list = time_12hr.split(":")
    hours = int(time_list[0])
    minutes = int(time_list[1])
    seconds_ampm = time_list[2]

    # If in PM hours and not 12 PM, add `12` to the hour
    if "PM" in seconds_ampm and hours != 12:
        hours += 12
    # If in AM hours and 12 AM, means it is midnight and should start from `0`
    elif "AM" in seconds_ampm and hours == 12:
        hours = 0

    military_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{seconds_ampm[:2]}"

    return military_time


time_12hr = input()
result = timeConversion(time_12hr)
print(result)
