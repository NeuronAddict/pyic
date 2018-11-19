import requests
from abc import ABC, abstractmethod


class Tester:
   
    def __init__(self, body_condition):
        self.body_condition = body_condition

    @abstractmethod
    def get_request(payload):
        pass
    

    def test(self, payload):
        r = self.get_request(payload)
        return self.body_condition(r.text)
        

