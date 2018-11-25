# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):
    if month in {1,3,5,7,8,10,12}:
        return 31
    if month in {4,6,9,11}:
        return 30
    if month == 2 and leap_year(year) == True:
        return 29
    elif month == 2 and leap_year(year) == False:
        return 28


def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    assert ((year1, month1, day1) <= (year2, month2, day2)), "AssertionError"
    days = 0
    while nextDay(year1, month1, day1) <= (year2, month2, day2):
        (year1, month1, day1) = nextDay(year1, month1, day1)
        days += 1
    return days


print(daysBetweenDates(1900, 1, 1, 1901, 1, 1))


