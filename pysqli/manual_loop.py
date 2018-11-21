class ManualLoop:
    def __init__(self, request_builder):
        self.request_builder = request_builder

    def start(self):
        print('[*] You are entering on payload mode, enter a payload to quick send it.')
        while True:
            payload = input('payload : >>>')
            if payload in ['exit', 'quit', 'bye']:
                print('')
                break
            r = self.request_builder(payload)
            print('[*] > {}'.format(r.request.url))
            print('[*] < {}'.format(r.headers))
            print('[*] < {}'.format(r.text))


def loop(rb):
    ManualLoop(rb).start()
