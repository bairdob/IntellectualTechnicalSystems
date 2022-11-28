import sys
import numpy as np

from settings import IP, PORT, TOPIC, LINEAR_VELOCITY, ANGULAR_VELOCITY, FILE


class Robot():

    def __init__(self, x: float, y: float, angle: float,
                 linear_velocity: float, angular_velocity: float):
        self.x = None
        self.y = None
        self.angle = None

        self.linear_velocity = None
        self.angular_velocity = None

    def move(self):
        pass

    @classmethod
    def readData(cls, path: str) -> np.ndarray:
        """
        читаet текстовый файл с координатами x и y 
        промежуточных точек маршрута в метрах
            :param path: путь до файла
            :return: список точек
        """
        try:
            f = open(path, 'r')
        except OSError:
            print('Could not open/read file:', readpath)
        with f:
            return np.loadtxt(path, dtype=float)

    @classmethod
    def histDistance(cls, hist1: list, hist2: list) -> float:
        """
        возвращает расстояние между двумя точками
            :param hist1: координаты точки1
                   hist2: координаты точки2
            :return: декартово расстояние
        """
        sum = 0
        for it, value in enumerate(hist1):
            sum += (hist2[it] - hist1[it])**2
        return sum**(0.5)


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

    print((Robot.readData(file)))
    # print(ip, port, topic, linear_velocity, angular_velocity, file)
