from termcolor import colored


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
            print(colored('[*] (request) {}'.format(r.request.url), 'blue'))
            print(colored('    (headers) {}'.format(r.request.headers), 'blue'))
            print(colored('    (body) {}'.format(r.request.body), 'blue'))
            print('[*] (response) {}'.format(r.status_code))
            print('    (headers) {}'.format(r.headers))
            print('    (text body)\n {}'.format(r.text))


def loop(rb):
    ManualLoop(rb).start()
