import sys
import datetime

sys.path.insert(0, 'leap_year.py')
import leap_year


class User:
    _name = ""
    _birtday = ""

    def __init__(self, name: str, birtday: str):
        self._name = name
        self._birtday = birtday

    def is_born_in_leap_year(self):
        birtdate = datetime.datetime.strptime(self._birtday, "%Y-%m-%d")
        return leap_year.is_leap_year(birtdate.year)


if __name__ == '__main__':
    def assert_equal(expected, actual, message):
        if expected == actual:
            print(f"{message} returned {actual} as expected")
        else:
            print(f"{message} did not returned {expected} as expected, but actual result is {actual}")


    data = {
        "2018-01-03": False,
        "2019-08-23": False,
        "2020-10-11": True,
        "2021-12-25": True  # invalid
    }

    for birtday, expect in data.items():
        # setup
        user = User(f"Alul {birtday}", birtday)
        # execution
        actual = user.is_born_in_leap_year()
        # assertion
        assert_equal(expect, actual, f"User born in {birtday} is ")
