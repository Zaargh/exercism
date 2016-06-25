# Unfinished solution - works for '1st' ... '5th' and 'teenth' options.
# New one, using other method will follow.


import calendar
from datetime import date


class MeetupDayException(Exception):
    pass


FIRST_FIFTH = ['1st', '2nd', '3rd', '4th', '5th']


def get_day_number(day_of_week):
    week = list(calendar.day_name)
    return week.index(day_of_week)


def meetup_day_first_fifth(year, month, day_number, which):
    """ Returns date of meetup day for '1st', '2nd', '3rd', '4th' and '5th'
        days.
    """
    first_day_of_month, month_len = calendar.monthrange(year, month)
    week_offset = FIRST_FIFTH.index(which)
    month_day = (day_number - first_day_of_month) % 7 + 1 + (7 * week_offset)
    if month_day <= month_len:
        return date(year, month, month_day)
    else:
        raise MeetupDayException


def meetup_day_teenth(year, month, day_number):
    """ Returns date of 'teenth' meetup day.
    """
    first_day_of_month, _ = calendar.monthrange(year, month)
    thirteenth = (first_day_of_month + 12) % 7
    month_day = (day_number - thirteenth) % 7 + 13
    return date(year, month, month_day)


def meetup_day_last(year, month, day_of_week):
    """ Returns date of 'last' meetup day.
    """
    # first_day_of_month, month_len = calendar.monthrange(year, month)
    # last_day_dow = (first_day_of_month + month_len) % 7
    # month_day = last_day_dow - day_number
    pass


def meetup_day(year, month, day_of_week, which):
    """ Returns date of meetup day.
    """
    day_number = get_day_number(day_of_week)
    if which in FIRST_FIFTH:
        return meetup_day_first_fifth(year, month, day_number, which)
    elif which == 'teenth':
        return meetup_day_teenth(year, month, day_number)
    elif which == 'last':
        return meetup_day_last(year, month, day_number)
