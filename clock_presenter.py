from turtle import *


class ClockPresenter:
    seconds_arrow_length = 70
    minutes_arrow_length = 50
    hours_arrow_length = 30

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
        hideturtle()

    def __del__(self):
        exitonclick()

    def draw(self):
        self._draw_circle()
        self._draw_indicators()
        update()

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

    def _draw_arrow(self, angle: int, length: int):
        penup()
        color(self._color)
        goto(0, 0)
        pendown()
        setheading(angle + 90)
        forward(length)
        update()

    def _clear_arrow(self, angle: int, length: int):
        penup()
        color(self._background_color)
        goto(0, 0)
        pendown()
        setheading(angle + 90)
        forward(length)
        update()

    def draw_arrows(self, seconds: int, minutes: int, hours: int):
        second_angle = -self._calculate_angle(seconds, 60)
        minute_angle = -self._calculate_angle(minutes, 60)
        hour_angle = -self._calculate_hour_angle(hours)
        self._draw_arrow(second_angle, self.seconds_arrow_length)
        self._draw_arrow(minute_angle, self.minutes_arrow_length)
        self._draw_arrow(hour_angle, self.hours_arrow_length)

    def clear_arrows(self, seconds: int, minutes: int, hours: int):
        second_angle = -self._calculate_angle(seconds, 60)
        minute_angle = -self._calculate_angle(minutes, 60)
        hour_angle = -self._calculate_hour_angle(hours)
        self._clear_arrow(second_angle, self.seconds_arrow_length)
        self._clear_arrow(minute_angle, self.minutes_arrow_length)
        self._clear_arrow(hour_angle, self.hours_arrow_length)

    @staticmethod
    def _calculate_angle(value: int, maximum: int, minimum: int = 0) -> int:
        if value == minimum:
            return minimum
        return int((360 * value) / maximum)

    @staticmethod
    def _calculate_hour_angle(hours: int) -> int:
        max_hours = 12
        angle_for_hour = 30
        hours_in_range = hours % max_hours
        return angle_for_hour * hours_in_range
