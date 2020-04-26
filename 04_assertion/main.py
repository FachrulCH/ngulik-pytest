def is_leap_year(year: int):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


if __name__ == '__main__':
    def assert_equal(expected, actual, message):
        if expected == actual:
            print(f"{message} returned {actual} as expected")
        else:
            print(f"{message} did not returned {expected} as expected, but actual result is {actual}")


    data = {
        2018: False,
        2019: False,
        2020: True,
        2021: True   #invalid
    }

    for year, expect in data.items():
        actual = is_leap_year(year)
        assert_equal(expect, actual, f"Year {year}")