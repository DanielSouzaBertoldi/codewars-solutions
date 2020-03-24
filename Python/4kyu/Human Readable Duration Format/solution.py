# Yeah, I admit.
# I took the lazy approach with this one.
# It was incredibly frustrating trying to make it work in
# python. Well, I've since then learned my lesson and
# created a more "automatic" solution in the other programming
# languages instead of brute forcing my solution.

def format_duration(seconds):
    if seconds == 0:
        result = "now"

    years = seconds//31536000
    days = (seconds-(31536000*years))//86400
    hours = (seconds - years*31536000 - days*86400)//3600
    minutes = (seconds - years*31536000 - days*86400 - hours*3600)//60
    seconds = seconds - years*31536000 - days*86400 - hours*3600 - minutes*60
    
    if years and days and hours and minutes and seconds:
        result = ("{0} year{1}, ".format(years, "s" if years!=1 else "") if years else "") + \
        ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif years and days and hours and minutes:
        result = ("{0} year{1}, ".format(years, "s" if years!=1 else "") if years else "") + \
        ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1} and ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1}".format(minutes, "s" if minutes!=1 else "") if minutes else "")
    elif days and hours and minutes and seconds:
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif hours and minutes and seconds:
        result = ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif days and minutes and seconds:
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif days and hours and minutes:
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1} and ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1}".format(minutes, "s" if minutes!=1 else "") if minutes else "")
    elif days and hours and seconds:
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1} and ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")    
    elif minutes and seconds:
        result = ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif seconds:
        result = ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    elif minutes:
        result = ("{0} minute{1}".format(minutes, "s" if minutes!=1 else "") if minutes else "")
    elif hours:
        result = ("{0} hour{1}".format(hours, "s" if hours!=1 else "") if hours else "")
    elif days:
        result = ("{0} day{1}".format(days, "s" if days!=1 else "") if days else "")

    return result