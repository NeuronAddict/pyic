from termcolor import colored


class ManualLoop:
    def __init__(self, request_builder):
        self.request_builder = request_builder

    def start(self, extractor=None):
        print('\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n')
        while True:
            payload = input(colored('payload : >>> ', 'red'))
            if payload in ['exit', 'quit', 'bye', 'quit()']:
                print('')
                break
            r = self.request_builder(payload)
            print(colored('[*] (request) {}'.format(r.request.url), 'blue'))
            print(colored('    (headers) {}'.format(r.request.headers), 'blue'))
            print(colored('    (body) {}'.format(r.request.body), 'blue'))
            print('[*] (response) {}'.format(r.status_code))
            print('    (headers) {}'.format(r.headers))
            print('    (text body)\n {}'.format(r.text))
            if extractor is not None:
                print(colored('[+] find value : {}'.format(extractor(r)), 'green'))


def loop(rb, extractor=None):
    """
    Enter into payload mode. This mode prompt a payload and send it via a request builder.

    :param rb: request builder. A request builder is a callable (class, function, lambda) that get a payload and return a response.
    :param extractor: Callable that take a response and extract the value read. type help(StartExtract) to get help.
    """
    ManualLoop(rb).start(extractor)
