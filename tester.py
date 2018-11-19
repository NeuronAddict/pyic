import requests
from abc import ABC, abstractmethod


class Tester:
   
    def __init__(self, response_condition):
        self.response_condition = response_condition

    @abstractmethod
    def get_request(payload):
        pass
    

    def test(self, payload):
        r = self.get_request(payload)
        return self.response_condition(r)
        

