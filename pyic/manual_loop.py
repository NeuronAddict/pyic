import cmd2
from termcolor import colored
from pyic.loggers import HttpLogger


class PayloadCmd(cmd2.Cmd):
    intro = '\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n'
    prompt = colored('payload : >>> ', 'red')

    def __init__(self, request_builder, logger=HttpLogger(), extractor=None):
        super().__init__(allow_cli_args=False)
        self.request_builder = request_builder
        self.logger = logger
        self.extractor = extractor

    def do_exit(self, line):
        return True

    def default(self, payload):
        r = self.request_builder(payload)

        if self.logger is not None:
            self.logger(r)

        if self.extractor is not None:
            value = self.extractor(r)
            if value is not None:
                print(colored('[+] find value : {}'.format(value), 'green'))


class ManualLoop:

    def __init__(self, request_builder, logger=HttpLogger()):
        self.request_builder = request_builder
        self.logger = logger

    def start(self, extractor=None):
        PayloadCmd(self.request_builder, self.logger, extractor).cmdloop()


def loop(rb, logger=HttpLogger(), extractor=None):
    """
    Enter into payload mode. This mode prompt a payload and send it via a request builder.

    :param rb: request builder. A request builder is a callable (class, function, lambda) that get a payload and return a response.
    :param logger: logger for requests. By default for Http, remplace with other if you don't make HTTP (MQTT, TCP, ...)
    :param extractor: Callable that take a response and extract the value read. type help(StartExtract) to get help.
    """
    ManualLoop(rb, logger).start(extractor)
