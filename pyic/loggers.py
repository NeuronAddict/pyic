from termcolor import colored


class HttpLogger:

    def __init__(self, filter=None):
        self.extractor = filter

    def __call__(self, r):

        print(colored("\n[*] > {} {}".format(r.request.method, r.request.url), 'cyan'))
        print(colored("[*] > {}".format(r.request.headers), 'cyan'))

        if hasattr(r.request, 'data'):
            print(colored("[*] > {}".format(r.request.data), 'cyan'))

        if r.request.body is not None:
            print(colored('{}'.format(r.request.body), 'cyan'))

        print(colored('\n[*] < {}'.format(r.status_code), 'magenta'))
        print(colored("[*] < {}\n".format(r.headers), 'magenta'))

        if self.extractor is None:
            print("{}\n".format(r.text))
        else:
            print("{}\n".format(self.extractor(r)))

        print(colored("[*] Response time : {}s\n".format(r.elapsed.total_seconds()), 'magenta'))
