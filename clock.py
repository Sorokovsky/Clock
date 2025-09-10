import datetime
import time

from clock_presenter import ClockPresenter


class Clock:
    def __init__(self):
        self._presenter = ClockPresenter()

    def start(self):
        self._presenter.draw()
        while True:
            now = datetime.datetime.now()
            year = now.hour
            minute = now.minute
            second = now.second
            self._presenter.draw_arrows(second, minute, year)
            time.sleep(1)
            self._presenter.clear_arrows(second, minute, year)
