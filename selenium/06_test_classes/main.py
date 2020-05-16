import sys
import datetime

sys.path.insert(0, 'leap_year.py')
import leap_year


class Tests():
    def run(self):
        for method in dir(self):
            if str(method).startswith("tests"):
                getattr(self, method)()

    def assert_equal(self, expected, actual):
        if expected == actual:
            print(f"{actual} returned {expected} as expected")
        else:
            print(f"{actual} did not returned {expected} as expected, but actual result is {actual}")

    def assert_true(self, actual):
        self.assert_equal(True, actual)

    def assert_false(self, actual):
        self.assert_equal(False, actual)


class User:
    _name = ""
    _birtday = ""

    def __init__(self, name: str, birtday: str):
        self._name = name
        self._birtday = birtday

    def is_born_in_leap_year(self):
        print(f"User {self._name} born in {self._birtday}")
        birtdate = datetime.datetime.strptime(self._birtday, "%Y-%m-%d")
        return leap_year.is_leap_year(birtdate.year)


if __name__ == '__main__':
    class UserTest(Tests):
        def test_not_born_in_leap_year_when_born_in_2018(self):
            user = User("Unyil", "2018-02-02")
            self.assert_false(user.is_born_in_leap_year())

        def test_not_born_in_leap_year_when_born_in_2019(self):
            user = User("Usro", "2019-03-30")
            self.assert_false(user.is_born_in_leap_year())

        def test_born_in_leap_year_when_born_in_2020(self):
            user = User("Ipin", "2020-11-13")
            self.assert_true(user.is_born_in_leap_year())

        def test_not_born_in_leap_year_when_born_in_2021(self):
            user = User("Upin", "2021-01-10")
            self.assert_true(user.is_born_in_leap_year())  # wrong expected


    test = UserTest()
    test.run()
