from termcolor import colored


class HttpLogger:
    def __call__(self, r):

        print(colored("\n[*] > {} {}".format(r.request.method, r.url), 'cyan'))
        print(colored("[*] > {}".format(r.request.headers), 'cyan'))

        if hasattr(r.request, 'data'):
            print(colored("[*] > {}".format(r.request.data), 'cyan'))

        if r.request.body is not None:
            print(colored('{}'.format(r.request.body), 'cyan'))

        print(colored('\n[*] < {}'.format(r.status_code), 'magenta'))
        print(colored("[*] < {}".format(r.headers), 'magenta'))
        print("{}\n".format(r.text))
