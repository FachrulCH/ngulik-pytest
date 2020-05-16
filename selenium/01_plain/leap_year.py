# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)


def is_leap_year(year: int):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


print("2001: " + str(is_leap_year(2001)))
print("1900: " + str(is_leap_year(1900)))
print("2000: " + str(is_leap_year(2000)))
print("2020: " + str(is_leap_year(2020)))
