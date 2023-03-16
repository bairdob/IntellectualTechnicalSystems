import json
from math import sin, cos


def logging(func):
    """
    Выводит информацию в формате time;(sgn)x;(sgn)y;angle
    и записывает все команды в файл
    """
    def wrapper(self, *argv, **kwargv):
        func(self, *argv, **kwargv)

        info = '{:.3f};{:+.1f};{:+.1f};{:.4f}\n'.format(
                self.time, self.x, self.y, self.angle)
        print(info,end='')

        with open("robot.log", "a") as f:
            f.write(info)

    return wrapper

class RobotModel():
    """
    Начальное положение робота в точке (0,0) декартовой 
    системы координат в напрaвлении оси OX
    """
    x = 0  # координата х
    y = 0  # координата y
    angle = 0  # угол, в направлении которого повернут робот (радиан)
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

    def stop(self):
        """
        Останавливает робот
        """
        pass

    



class App():
    robot = RobotModel()

    def process_message(self, message: str) -> dict:
        """
        Выводит и возвращает словарь полученный из сообщения по mqtt
        """
        message_dict = json.loads(message)
        print(message_dict)
        return message_dict

    def send_command_to_robot(self, message: dict):
        """
        Парсит сообщение и отправляет команды роботу
        """
        robot_cmds= {
            'forward': self.robot.forward, 
            'left': self.robot.left, 
            'right': self.robot.right,
            'stop': self.robot.stop
        }

        cmd = message['cmd']
        val = float(message.get('val')) if message.get('val') else None

        if val:
            robot_cmds[cmd](val)
        else:
            robot_cmds[cmd]

        
        
if __name__ == '__main__':
    m1 = '{"cmd": "left", "val": "1.0"}' # поворот на 90 градусов
    m2 = '{"cmd": "forward", "val": "1.0"}'
    m3 = '{"cmd": "stop"}'
    msgs = [m1, m1, m3]
    app = App()

    for msg in msgs: # эмуляция отправки команд
        message = app.process_message(msg)
        app.send_command_to_robot(message)
