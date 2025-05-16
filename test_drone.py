# This code tests the drone class and commandProcessor class
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
        self.assertEqual(self.drone.status(), "Position: (0, 0), Direction: West")

    # This checks flying south
    def test_fly_south(self):
        self.drone.right()
        self.drone.fly()
        self.drone.right()  # this is a rotation
        self.drone.fly()    # rotation complete and flying continuously down
        self.assertEqual(self.drone.status(), "Position: (1, 0), Direction: South")

    def test_boundary(self):
        self.drone.launch(0, 0, "North")  # this positions the drone at the bottom left, facing North
        for _ in range(5):            # This is to test the drone and ensure it stays within parameters
            self.drone.fly()      # Attempt to fly
            self.assertEqual(self.drone.status(), "Position: (0, 5), Direction: North")

        self.drone.launch(5, 5, "East")   # This positions the drone at the top right
        self.drone.fly()  # Attempt to fly east
        self.assertEqual(self.drone.status(), "Position: (5, 5), Direction: East")  # Check the position after flying

        self.drone.launch(0, 0, "South")  # This positions the drone bottom right
        self.drone.fly()  # Attempt to fly south
        self.assertEqual(self.drone.status(), "Position: (0, 0), Direction: South")  # The drone should not move

        self.drone.launch(0, 0, "West")   # This positions the drone at the top left
        self.drone.fly()  # Attempt to fly west
        self.assertEqual(self.drone.status(), "Position: (0, 0), Direction: West")  # Should not move

    #This should throw an error
    def invalid_launch(self):
        self.drone.launch(6,6, "North")
        print("Out of boundary")

    def invalid_direction(self):
        self.drone.launch(1,1,"UP")
        print("Invalid direction")


if __name__ == "__main__":
    unittest.main()
