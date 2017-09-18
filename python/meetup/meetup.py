from datetime import date
import calendar

def meetup_day(year, month, dayOfWeek, dateOffset):
    cal = calendar.LocaleTextCalendar(locale='en_US')
    weeks = cal.monthdayscalendar(year, month)
    days = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, \
            "Friday":4, "Saturday":5, "Sunday":6}
    weekValues = {"1st":0, "2nd":1, "3rd":2, "4th":3, "5th":4, \
                  "teenth":-2, "last":-1}
    dayIndex = days.get(dayOfWeek)
    weekOffset = weekValues.get(dateOffset)
    
    day = find_day_in_month(weeks, dayIndex, weekOffset)
    return date(year, month, day)

    
def find_day_in_month(weeks, dayIndex, weekOffset):
    
    # Get days in month
    
    if weekOffset >= 0:
        # Find week containing first queried day of the month
        weekOfFirstDay = find_first_week_containing_queried_day(weeks, dayIndex)
        week = weeks[weekOfFirstDay + weekOffset]
    elif weekOffset == -1:
        # Find week containing last day
        weekOfLastDay = find_last_week_containing_queried_day(weeks, dayIndex)
        week = weeks[weekOfLastDay]
    else:
        # Find week containing teenth day
        weekOfTeenthDay = find_teenth_week_containing_queried_day(weeks, dayIndex)
        week = weeks[weekOfTeenthDay]

    return week[dayIndex]    
    

def find_first_week_containing_queried_day(weeks, dayIndex):
    dayValue = 0
    i = 0
    
    while dayValue == 0:
        week = weeks[i]
        dayValue = week[dayIndex]
        i += 1

    return i - 1


def find_last_week_containing_queried_day(weeks, dayIndex):
    dayValue = 0
    i = len(weeks) - 1
    
    while dayValue == 0:
        week = weeks[i]
        dayValue = week[dayIndex]
        i -= 1

    return i + 1


def find_teenth_week_containing_queried_day(weeks, dayIndex):
    dayValue = 0
    i = 0

    while dayValue == 0:
        week = weeks[i]
        # Check if week day is between 13 and 19, if not increment week by 1
        if week[dayIndex] >= 13 and week[dayIndex] <= 19:
            dayValue = week[dayIndex]
        i += 1

    return i - 1

    
