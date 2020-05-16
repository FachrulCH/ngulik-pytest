import requests


class RestfulBooker():
    URL = 'https://restful-booker.herokuapp.com/'

    def _url(self, path: str):
        return URL + path

    def get_booking(self, booking=None):
        return requests.get(self._url('booking'))
