class Tester:

    def __init__(self, request_builder, response_condition, log=False):
        """

        :param request_builder: callable that take a payload to return a response
        :param response_condition: callable that take a response and return a boolean
        :param log:
        """
        self.response_condition = response_condition
        self.log = log
        self.request_builder = request_builder

    def test(self, payload):
        r = self.request_builder(payload)
        if self.log:
            print("[*] request {}".format(r.url))
            print("[*] response: {}".format(r.text))
        return self.response_condition(r)
