from termcolor import colored, cprint

class ManualLoop:
    def __init__(self, request_builder):
        self.request_builder = request_builder

    def start(self):
        print('\n[*] You are entering on payload mode, enter a payload to quick send it via your request builder.\n')
        while True:
            payload = input(colored('payload : >>> ', 'red'))
            if payload in ['exit', 'quit', 'bye', 'quit()']:
                print('')
                break
            r = self.request_builder(payload)
            print('[*] (request) > {}'.format(r.request.url))
            print('    (headers) > {}'.format(r.request.headers))
            print('    (body) > {}'.format(r.request.body))
            print('[*] (response) < {}'.format(colored(r.status_code, 'blue')))
            print('    (headers) < {}'.format(colored(r.headers, 'blue')))
            print('    (text body) < {}'.format(colored(r.text, 'blue')))


def loop(rb):
    ManualLoop(rb).start()
