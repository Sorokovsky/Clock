from turtle import *
import time

class ClockPresenter:
    def __init__(self, radius: int = 100):
        self._radius = radius
        self._background_color = "darkGreen"
        self._color = "white"
        reset()
        pen()
        pensize(3)
        speed(0)
        tracer(0)
        title("Годинник")
        setup(1000, 1000)
        bgcolor(self._background_color)
        penup()
        colormode(255)

    def draw(self):
        self._draw_circle()
        self._draw_indicators()
        self._draw_arrows()
        update()
        exitonclick()

    def _draw_circle(self):
        goto(0, -100)
        pendown()
        color(self._color)
        fillcolor(self._color)
        circle(self._radius)

    def _draw_indicators(self):
        color(self._color)
        for i in range(0, 60):
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
        second_arrow_length = 70
        minute_arrow_length = int(second_arrow_length / 2)

        penup()
        goto(0, 0)
        pendown()
        color(self._color)
        forward(minute_arrow_length)
        update()

        tracer(1)
        while True:
            for i in range(4, 60):
                penup()
                goto(0, 0)
                setheading(-i * 360 / 60)
                pendown()
                color(self._color)
                forward(second_arrow_length)
                update()
                time.sleep(1)
                color(self._background_color)
                backward(second_arrow_length)
                backward(second_arrow_length)