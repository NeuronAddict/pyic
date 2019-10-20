import cmd2
from termcolor import colored
from pyic.loggers import HttpLogger


class PayloadCmd(cmd2.Cmd):
    intro = '\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n'
    prompt = colored('payload : >>> ', 'red')

    def __init__(self, request_builder, logger=HttpLogger(), extractor=None, delete_set=True, delete_quit=False):
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

        if delete_quit:
            del cmd2.Cmd.do_quit

        if delete_set:
            del cmd2.Cmd.do_set

    def do_exit(self, line):
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
