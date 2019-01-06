import sys
import threading
import time
from threading import Thread


class PercentDisplay:

    def __init__(self, total):
        self.total = total

    def init_display(self):
        sys.stdout.write("[%-20s] 0%%" % '')
        sys.stdout.flush()

    def update_display(self, new_value):
        val = int(new_value / self.total * 100)
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('=' * (int(val / 5) - 1) + '>', val))
        sys.stdout.flush()

    def end(self):
        self.update_display(self.total)
        sys.stdout.flush()


class ThreadedPercentDisplay:

    def __init__(self, total, delay=0.2):
        self.total = total
        self.value = 0
        self.delay = delay
        self.pd = PercentDisplay(total)
        self.stop = True
        self.thread_lock = threading.Lock()

    def start(self):
        if not self.stop:
            raise Exception('Already started')

        self.stop = False
        self.pd.init_display()

        def f():
            while not self.stop:
                time.sleep(self.delay)
                self.pd.update_display(self.value)

        self.display_thread = Thread(None, f)
        self.display_thread.start()

    def add(self, v=1):
        with self.thread_lock:
            self.value += 1

    def stop_update_display(self):
        self.stop = True
        self.display_thread.join()
        self.pd.end()
