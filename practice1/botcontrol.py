import sys
import numpy as np
from math import acos

from settings import IP, PORT, TOPIC, LINEAR_VELOCITY, ANGULAR_VELOCITY, FILE


class Robot():

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 angle: float = 0,
                 linear_velocity: float = 0,
                 angular_velocity: float = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity
        self.points = [] # маршрут робота

    def readData(self, path: str) -> np.ndarray:
        """
        читаeт текстовый файл с координатами x,y 
            :param path: путь до файла
            :return: список точек
        """
        try:
            f = open(path, 'r')
        except OSError:
            print('Could not open/read file:', readpath)
        with f:
            self.points = np.loadtxt(path, dtype=float)
            return self.points

    def calc_distance(self, x, y) -> float:
        """
        возвращает расстояние от робота до точки
            :param х: координатa x
                   y: координатa y
            :return: декартово расстояние
        """
        distance = (self.x - x)**2 + (self.y - y)**2
        return distance**(0.5)

    def calc_distance_time(self, distance: float):
        """
        вычисляет время движения по известному расстоянию
            :param distance: расстояние
            :return: время движения
        """
        return distance / self.linear_velocity  

    def calc_angle(self, x, y):
        """
        Вычисляет угол поворота на следующую точку 
        в промежуточной точке маршрута
            :param х: координатa x
                   y: координатa y
            :return: угол поворота
        """
        if self.x * x + self.y * y == 0:
            cos = 0
        else:
            # Получим косинус угла по формуле
            cos = (self.x * x + self.y * y) / (
                (self.x * self.x + self.y * self.y)**0.5 *
                (x * x + y * y)**0.5)
        # Вернем arccos полученного значения (в радианах!)
        return acos(cos) + self.angle

    def calc_rotate_time(self, angle):
        """
        вычисляет время, необходимое для поворота на заданный угол
            :param angle: угол поворота 
            :return: время поворта
        """
        return angle / self.angular_velocity

    def create_message(self):
        """
        формирует команды боту на движение и останов по маршруту
        """
        msg = {"cmd": "", "val": ""}
        # устанавливаем начальное положение робота
        self.x, self.y = self.points[0][0], self.points[0][1]

        eps = 2.220446049250313e-16
        right_angle = 1.5707963267948966  # прямой угол

        for index, value in enumerate(self.points[1:]):
            x, y = value[0], value[1]
            # расчеты до новой точки
            distance = self.calc_distance(x, y)
            distance_time = self.calc_distance_time(distance)
            angle = self.calc_angle(x, y)
            rotate_time = self.calc_rotate_time(angle)

            # формируем сообщение
            if angle > 0:
                msg["cmd"] = "left"
                msg["val"] = rotate_time
                self.angle = angle
                print(msg)
            elif angle < 0:
                msg["cmd"] = "right"
                msg["val"] = rotate_time
                self.angle = angle
                print(msg)
            if (angle - right_angle) or (angle - 2 * right_angle) < eps:
                msg["cmd"] = "forward"
                msg["val"] = distance_time
                self.x, self.y = x, y
                print(msg)
        print('{\'cmd\': \'stop\'}')

    def send_message_to_robot(self):
        """
        отправляет команды роботу по mqtt
        """
        pass


if __name__ == '__main__':
    try:
        ip = str(sys.argv[1])
        port = int(sys.argv[2])
        topic = str(sys.argv[3])
        linear_velocity = float(sys.argv[4])
        angular_velocity = float(sys.argv[5])
        file = str(sys.argv[6])
    except:
        ip = IP
        port = PORT
        topic = TOPIC
        linear_velocity = LINEAR_VELOCITY
        angular_velocity = ANGULAR_VELOCITY
        file = FILE

    r = Robot(linear_velocity=linear_velocity,
              angular_velocity=angular_velocity)
    r.readData(path=file)
    r.create_message()
