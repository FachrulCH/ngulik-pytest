import sys

sys.path.insert(0, 'leap_year.py')
import leap_year


# print("is 2020 leap year? the answer is " + str(leap_year.is_leap_year(2020)))
years = [2017, 2018, 2019, 2020, 2021]
for yrs in years:
    print(f"is {yrs} leap year? that is {leap_year.is_leap_year(yrs)}")