class Drone:
    def __init__(self, max_x=5, max_y=5):  # This initializes the boundary at 5meters
        self.x = 0  # initializing x coordinate
        self.y = 0  # initializing y coordinate
        self.direction = "North"  # This is the initial direction.
        self.max_x = max_x  # This is the maximum length boundary
        self.max_y = max_y  # This is the maximum width boundary

    def launch(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        if not (0 <= x <= self.max_x and 0 <= x <= self.max_y):       # checks if the coordinates are within boundary
            print("Coordinates are out of bounds")
        valid_directions = ["North", "South", "West","East"]
        if direction not in valid_directions:
            print("Invalid direction")
        print(f"X coordinate: {self.x},Y coordinate:{self.y},Direction:{self.direction}")  # prints out the position and direction

    # This is the Flying Method
    def fly(self):  # moving the drone based on its current position
        if self.direction == "North" and self.y < self.max_y:  # This ensures that the current y coordinate is less than the boundary
            self.y += 1  # If condition is true, It continuously moves upward
        elif self.direction == "South" and self.y > 0:  # This checks if the current y-coordinate is above the lower boundary zero.
            self.y -= 1  # If true, It continuously moves downward
        elif self.direction == "East" and self.x < self.max_x:  # This check if the current is East and is less than the length boundary
            self.x += 1  # It moves continuously to the right
        elif self.direction == "West" and self.x > 0:  # This checks if the current y coordinate is above the lover boundary
            self.x -= 1  # It moves on the opposite of the x coordinate, that is the left

    # This is moving the drone in several directions
    def right(self):
        directions = ['North', 'East', 'South', 'West']  # Initializing the different possible directions
        current_index = directions.index(self.direction)  # This goes to the direction list and takes the current position(index) of the drone.
        self.direction = directions[(current_index + 1) % 4]  # This moves to the next position in the list and wraps around to 4 which signifies all the positions

    def left(self):
        directions = ['North', 'West', 'South', 'East']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    # This will check and return the current status of the drone.
    def status(self):
        return f"Position: ({self.x}, {self.y}), Direction: {self.direction}"
