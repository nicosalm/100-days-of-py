# function to subtract two 24-hour times formatted as HH:MM:SS
# returns a string formatted as HH:MM:SS

def time_difference(time1, time2):
    # split the times into hours, minutes, and seconds
    time1 = time1.split(":")
    time2 = time2.split(":")

    # convert the times into seconds
    time1 = int(time1[0])*3600 + int(time1[1])*60 + int(time1[2])
    time2 = int(time2[0])*3600 + int(time2[1])*60 + int(time2[2])

    # subtract the times
    time3 = time1 - time2

    # convert the time back into hours, minutes, and seconds
    hours = time3 // 3600
    minutes = (time3 % 3600) // 60
    seconds = (time3 % 3600) % 60

    # format the time, adding a leading zero if necessary
    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    time3 = str(hours) + ":" + str(minutes) + ":" + str(seconds)

    return time3

print(time_difference("10:00:00", "9:00:00"))