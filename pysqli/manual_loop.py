from termcolor import colored
from pysqli.loggers import HttpLogger


class ManualLoop:

    def __init__(self, request_builder, logger=HttpLogger()):
        self.request_builder = request_builder
        self.logger = logger

    def start(self, extractor=None):
        print('\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n')

        while True:
            payload = input(colored('payload : >>> ', 'red'))

            if payload in ['exit', 'quit', 'bye', 'quit()']:
                print('')
                break

            r = self.request_builder(payload)

            if self.logger is not None:
                self.logger(r)

            if extractor is not None:
                print(colored('[+] find value : {}'.format(extractor(r)), 'green'))


def loop(rb, logger=HttpLogger(), extractor=None):
    """
    Enter into payload mode. This mode prompt a payload and send it via a request builder.

    :param rb: request builder. A request builder is a callable (class, function, lambda) that get a payload and return a response.
    :param logger: logger for requests. By default for Http, remplace with other if you don't make HTTP (MQTT, TCP, ...)
    :param extractor: Callable that take a response and extract the value read. type help(StartExtract) to get help.
    """
    ManualLoop(rb, logger).start(extractor)
