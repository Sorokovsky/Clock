import datetime
import time

from clock_presenter import ClockPresenter


class Clock:
    def __init__(self):
        self._presenter = ClockPresenter()
        now: datetime = datetime.datetime.now()
        self._hours = now.hour
        self._minutes = now.minute
        self._seconds = now.second

    def start(self):
        self._presenter.draw()
        self._loop()

    def _tick(self):
        self._seconds += 1
        if self._seconds >= 60:
            self._seconds = 0
            self._minutes += 1
        if self._minutes >= 60:
            self._minutes = 0
            self._hours += 1

    def _draw(self):
        self._presenter.draw_arrows(self._seconds, self._minutes, self._hours)

    def _clear(self):
        self._presenter.clear_arrows(self._seconds, self._minutes, self._hours)

    def _update(self):
        self._clear()
        self._tick()
        self._draw()

    def _loop(self):
        while True:
            self._update()
            time.sleep(1)