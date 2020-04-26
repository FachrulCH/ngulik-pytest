def is_leap_year(year: int):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


if __name__ == '__main__':
    data = {
        2018: False,
        2019: False,
        2020: True,
        2021: False
    }

    for key, val in data.items():
        actual = is_leap_year(key)
        if actual:
            print(f"Year {key} is leap year as expected")
        else:
            print(f"Year {key} did not return as expected, but actual result is {actual}")