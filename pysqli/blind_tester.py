from termcolor import colored


class BlindTester:
    """
    A Tester can test if a sqli injected query return true or false (its a blind tester).
    """
    def __init__(self, request_builder, response_condition, logger=None):
        """
        Create e new Blind tester. To do this, we need :
        - a query, make with requests from a payload
        - a condition, to determine if the result is True from a response

       they can be lambda, function or callable objects
       - The query take a String payload to return a requests response
       - The condition take a response to return a boolean

        example :
        tester = Tester(
                    lambda payload : requests.get('http://127.0.0.1/inject.php', params={'id': '1 {}'.format(payload)}),
                    lambda r: 'error' not in r.text)

        :param request_builder: callable that take a payload to return a response
        :param response_condition: callable that take a response and return a boolean
        :param log: if True, log all requests / response (very verbose). False by default.
        """
        self.response_condition = response_condition
        self.logger = logger
        self.request_builder = request_builder

    def test(self, payload):
        r = self.request_builder(payload)
        if self.logger is not None:
            print(colored("[*] payload : {}".format(payload), 'red'))
            self.logger(r)
        return self.response_condition(r)
