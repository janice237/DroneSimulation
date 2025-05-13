class Drone:
    def __init__(self):
        self.x = 0  # initializing x coordinate
        self.y = 0  # initializing y coordinate
        self.direction = "North"  # This is the initial direction.

    def launch(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        print(f"X coordinate: {self.x},Y coordinate:{self.y},Direction:{self.direction}")

    # This is the Flying Method
    def fly(self):  # moving the drone based on its current position
        if self.direction == "North":
            self.y += 1  # It continuously moves upward
        elif self.direction == "South":
            self.y += 1  # It continuously moves downward
        elif self.direction == "East":
            self.x += 1  # It moves continuously to the right
        elif self.direction == "West":
            self.x -= 1  # It moves on the opposite of the x coordinate, that is the left

    # This is moving the drone in several directions
    def right(self):
        directions = ['North', 'East', 'South', 'West']  # Initializing the different possible directions
        current_index = directions.index(
            self.direction)   #This goes to the direction list and takes the current position(index) of the drone.
        self.direction = directions[(current_index + 1) % 4]  # This moves to the next position in the list and wraps around to 4 which signifies all the positions

    def left(self):
        directions = ['North', 'West', 'South', 'East']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    # This will check and return the current status of the drone.
    def status(self):
        return f"Position: ({self.x}, {self.y}), Direction: {self.direction}"
