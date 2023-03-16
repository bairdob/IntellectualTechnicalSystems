import sys
import unittest
from unittest import TestCase

sys.path.append('../practice1')
from botcontrol import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.right_angle = 1.5707963267948966  # прямой угол
        self.robot = Robot(linear_velocity=1.,
                           angular_velocity=1.5707963267948966)

    def test_distance(self):
        correct_distance = 2.
        self.assertEqual(correct_distance, self.robot.calc_distance(0, 2))

    def test_distance_time(self):
        correct_time = 1
        self.assertEqual(correct_time, self.robot.calc_distance_time(1))

    def test_angle(self):
        correct_angle = self.right_angle
        self.assertEqual(correct_angle, self.robot.calc_angle(0, 1))

    def test_calc_rotate_time(self):
        correct_time = 1
        self.assertEqual(correct_time,
                         self.robot.calc_rotate_time(self.right_angle))


if __name__ == "__main__":
    unittest.main()
