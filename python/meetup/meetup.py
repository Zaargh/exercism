# import calendar
# from datetime import date
#
#
# class MeetupDayException(Exception):
#     pass
#
#
# FIRST_FIFTH = ['1st', '2nd', '3rd', '4th', '5th']
#
#
# def get_d_o_w(day_of_week):
#     """ Returns day of week number (d_o_w):
#         Monday: 0, ..., Sunday: 6
#     """
#     week = list(calendar.day_name)
#     return week.index(day_of_week)
#
#
# def meetup_day(year, month, day_of_week, which):
#     """ Solution uses Calendar class from calendar module.
#         Calendar.itermonthdays2 returns iterator of tuples
#         (day_of_month, weekday)
#     """
#     d_o_w = get_d_o_w(day_of_week)
#     cal = calendar.Calendar()
#     # List all possible days (all Mondays, all Tuesdays, etc.)
#     possible_dates = [day for day in cal.itermonthdays2(year, month)
#                       if (day[0] != 0 and day[1] == d_o_w)]
#
#     if which in FIRST_FIFTH:
#         try:
#             day_number = possible_dates[FIRST_FIFTH.index(which)][0]
#         except IndexError:
#             raise MeetupDayException
#     elif which == 'teenth':
#         teenth = (13, 14, 15, 16, 17, 18, 19)
#         for possibility in possible_dates:
#             if possibility[0] in teenth:
#                 day_number = possibility[0]
#     elif which == 'last':
#         day_number = possible_dates[-1][0]
#
#     return date(year, month, day_number)



import calendar
import datetime


WEEKDAY_TO_INT = dict(zip(calendar.day_abbr, range(7)))
ORDINAL_TO_START_DAY = {
    "1st": 1,
    "2nd": 8,
    "teenth": 13,
    "3rd": 15,
    "4th": 22,
    "5th": 29,
}


def meetup_day(year, month, weekday_name, ordinal):
    weekday = WEEKDAY_TO_INT[weekday_name[:3]]

    if ordinal == "last":
        _, start_date_num = calendar.monthrange(year, month)
        date_range = range(0, -7, -1)
    else:
        start_date_num = ORDINAL_TO_START_DAY[ordinal]
        date_range = range(0, 8)

    start_date = datetime.date(year, month, start_date_num)

    for d in (start_date + datetime.timedelta(days=i) for i in date_range):
        if d.weekday() is weekday:
            return d
