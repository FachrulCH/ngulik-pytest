import requests
from assertpy import assert_that
import restful_booker
import json


def print_request(request: requests):
    print('\n-----------Request----------->')
    print(request.method, request.url)
    headers = '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items())
    print(headers)
    print(request.body)


def print_response(response: requests.Response):
    data = response.json()
    body = json.dumps(data, indent=4)
    resp_body = body
    print('\n<-----------Response-----------')
    headers = '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items())
    print(headers)
    print(resp_body)


class TestRestfulBooking():
    def test_get_list_of_all_booking(self):
        resp = restful_booker.get_bookings()
        print_request(resp.request)
        print_response(resp)
        assert_that(resp.status_code, 200).is_true()
        assert_that(len(resp.json())).is_greater_than(0)

    def test_get_booking_detail(self):
        resp = restful_booker.get_detail_booking(6)
        print_request(resp.request)
        print_response(resp)
        assert_that(resp.status_code, 200).is_true()
        assert_that(resp.json().get('firstname')).is_not_empty()

    def test_create_booking(self):
        resp = restful_booker.create_dummy_booking()
        print_request(resp.request)
        print_response(resp)
        created_booking = resp.json()
        print('bookingid = ', created_booking['bookingid'])


