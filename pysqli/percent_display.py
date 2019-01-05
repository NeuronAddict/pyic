import sys

class PercentDisplay:

    def __init__(self, total):
        self.total = total

    def init_display(self):
        sys.stdout.write("[%-20s] 0%%" % '')
        sys.stdout.flush()

    def update_display(self, new_value):
        val = int(new_value / self.total * 100)
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('=' * (int(val / 5)-1) + '>', val))
        sys.stdout.flush()

    def end(self):
        self.update_display(self.total)
