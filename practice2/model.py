import json
from math import atan, sin, cos


def logging(func):
    """
    Выводит сообщение в формате time;(sgn)x;(sgn)y;angle
    """
    def wrapper(self, *argv, **kwargv):
        func(self, *argv, **kwargv)
        print('{:.3f};{:+.1f};{:+.1f};{:.4f}'.
              format(self.time, self.x, self.y, self.angle))
    return wrapper

class RobotModel():
    """
    Робот стоит в точке (0,0) декартовой системы координат
    в напрaвлении оси OX
    """
    x = 0  # координата х
    y = 0  # координата y
    angle = 0  # угол, в направлении которого повернут робот (в радианах)
    velocity = 1  # линейная скорость робота
    angle_velocity = 1.5708  # угловая скорость поворота робота
    time = 0  # время отсчета начала движения

    @logging
    def forward(self, time: float):
        """
        Устанавливает позицию роботa по координатам dx,dy за промежуток dt
        """
        eps = 2e-16
        step = 0.1
        timer = 0
        dx = 0
        dy = 0
        while (timer - time + step) <= eps:
            l = self.velocity * step  # гипотенуза
            dx = l * cos(self.angle)
            dy = l * sin(self.angle)
            self.x += dx
            self.y += dy
            timer += step
            self.time += step

    @logging
    def left(self, time: float):
        """
        Поворачивает робот в положительном направлении
        """
        self.angle += self.angle_velocity * time
        self.time += time

    @logging
    def right(self, time: float):
        """
        Поворачивает робот в отрицательном направлении
        """
        self.angle += -self.angle_velocity * time
        self.time += time

    def stop(self, time: float):
        """
        Записывает в csv файл, метку времени, координаты x,y и угол
        """
        pass


class App():
    robot = RobotModel()

    def process_message(self, message: str) -> dict:
        message_dict = json.loads(message)
        return message_dict

    def send_command(cmd):
        pass


if __name__ == '__main__':
    s = '{"cmd": "forward", "val": "5.0"}'
    a = App().process_message(s)
    r = RobotModel()
    r.left(1)  # поворот на 90 градусов
    r.forward(1)
