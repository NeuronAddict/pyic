from abc import abstractmethod


class Tester:

    def __init__(self, response_condition, log=False):
        self.response_condition = response_condition
        self.log = log

    @abstractmethod
    def get_request(self, payload):
        pass

    def test(self, payload):
        r = self.get_request(payload)
        if self.log:
            print("[*] request {}".format(r.url))
            print("[*] response: {}".format(r.text))
        return self.response_condition(r)
