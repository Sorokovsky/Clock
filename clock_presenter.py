from turtle import *


class ClockPresenter:
    def __init__(self, radius: int = 100):
        self._radius = radius
        self._background_color = "darkGreen"
        self._color = "white"
        reset()
        pen()
        pensize(3)
        speed(1)
        title("Годинник")
        setup(1000, 1000)
        bgcolor(self._background_color)
        penup()
        colormode(255)

    def draw(self):
        self._draw_circle()
        self._draw_indicators()
        self._draw_arrows()
        exitonclick()

    def _draw_circle(self):
        goto(0, -100)
        speed(0)
        pendown()
        color(self._color)
        fillcolor(self._color)
        circle(self._radius)

    def _draw_indicators(self):
        speed(0)
        color(self._color)
        for i in range(0, 60):
            speed(0)
            height = 10
            if i % 5 == 0:
                height *= 2
            penup()
            goto(0, 0)
            forward(self._radius)
            pendown()
            backward(height)
            left(360 / 60)

    def _draw_arrows(self):
        second_arrow_length = 30
        minute_arrow_length = int(second_arrow_length / 2)
        penup()
        goto(0, 0)
        pendown()
        color(self._color)
        forward(self._radius - minute_arrow_length)
        while True:
            for i in range (0, 60):
                penup()
                goto(0, 0)
                pendown()
                color(self._color)
                forward(self._radius - second_arrow_length)
                color(self._background_color)
                backward(self._radius - second_arrow_length)
                left(360 / 60)