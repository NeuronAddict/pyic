import cmd2
from termcolor import colored
from pyic.loggers import HttpLogger


class PayloadCmd(cmd2.Cmd):
    intro = '\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n'
    prompt = colored('payload : >>> ', 'red')

    def __init__(self, request_builder, logger=HttpLogger(), extractor=None, delete_set=True):
        """
        Create a CmdLine for payload mode
        :param request_builder: Request builder to use. This rb will use the entered line as payload and forward
                                response to the extractor and logger
        :param logger: Logger to use. By default use the HttpLogger that print http response and response time
        :param extractor: A callable that extract a value from the reponse (use StarExtract for get simple value)
        :param delete_set: Do not execute the the set command (if you want type set in payload mode),
                           see https://cmd2.readthedocs.io/en/latest/features/settings.html
        """
        super().__init__(allow_cli_args=False, allow_redirection=False)
        self.request_builder = request_builder
        self.logger = logger
        self.extractor = extractor
        del cmd2.Cmd.do_alias
        del cmd2.Cmd.do_edit
        del cmd2.Cmd.do_eof
        del cmd2.Cmd.do_help
        del cmd2.Cmd.do_macro
        del cmd2.Cmd.do_py
        del cmd2.Cmd.do_shortcuts
        del cmd2.Cmd.do_history
        del cmd2.Cmd.do_run_pyscript
        del cmd2.Cmd.do_run_script
        del cmd2.Cmd.do__relative_run_script
        del cmd2.Cmd.do_shell
        del cmd2.Cmd.do_quit

        if delete_set:
            del cmd2.Cmd.do_set

    def do_exit(self, line):
        """Exit payload mode"""
        return True

    def default(self, line):
        payload = line.raw
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
