# This code tests the drone class
from drone import Drone  # This imports the Drone class from the drone.py
import unittest  # This imports the unittest module


class TestDrone(unittest.TestCase):  # defining the test class to inherit from unittest.Testcase
    def setUp(self):  # This Sets the drone up for an instance before testing it
        self.drone = Drone()
        self.drone.launch(0, 0, "North")

    # This checks the initial state of the drone
    def test_initial_status(self):
        self.assertEqual(self.drone.status(), "Position:(0, 0), Direction: North")

    # This checks if the drone moves north correctly
    def test_fly_north(self):
        self.drone.fly()
        self.assertEqual(self.drone.status(), "Position: (0, 1), Direction: North")

    # This checks if the drone turns right and is flying
    def test_right_and_flying(self):
        self.drone.right()
        self.drone.fly()
        self.assertEqual(self.drone.status(), "Position: (1, 1), Direction: East")

    # This checks if the drone turns left and is flying
    def test_left_and_flying(self):
        self.drone.left()
        self.drone.fly()
        self.assertEqual(self.drone.status(), "Position: (0, -1), Direction: West")

    # This checks flying south
    def test_fly_south(self):
        self.drone.right()
        self.drone.fly()
        self.drone.right()  # this is a rotation
        self.drone.fly()    # rotation complete and flying continuously down
        self.assertEqual(self.drone.status(), "Position: (1, -1), Direction: South")


if __name__ == "__main__":
    unittest.main()
