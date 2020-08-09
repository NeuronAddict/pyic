import requests

from pyic import PayloadCmd


def test_payload_cmd():
    rb = lambda payload: requests.get('http://127.0.0.1')
    PayloadCmd(rb)
    PayloadCmd(rb)
