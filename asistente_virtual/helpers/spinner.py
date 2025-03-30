import threading
import itertools
import sys
import time

class Spinner:
    def __init__(self, message="Loading..."):
        self.message = message
        self._spinning = False
        self._thread = None

    def _animate(self):
        for symbol in itertools.cycle(['|', '/', '-', '\\']):
            if not self._spinning:
                break
            sys.stdout.write(f'\r{self.message} {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone.               \n')

    def start(self):
        self._spinning = True
        self._thread = threading.Thread(target=self._animate)
        self._thread.start()

    def stop(self):
        self._spinning = False
        self._thread.join()
