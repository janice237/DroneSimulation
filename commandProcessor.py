from drone import Drone


def validate_command(command):  # checks the structure of the code
    valid_actions = ["launch", "fly", "North", "East", "South", "West"]
    return any(
        command.startswith(action) for action in valid_actions)  # checks if the command starts with a valid action


class CommandProcessor(Drone):
    def __init__(self, max_x=5, max_y=5):
        super().__init__(max_x, max_y)  # Inherits from the parent class
        self.execute = None
        self.commands = []
        self.error_logs = []

    # methods
    def add_command(self, command):
        if validate_command(command):  # checks if command is valid
            self.commands.append(command)
            self.execute.command(command)  # adds command to the list if it is valid
        else:
            self.error_logs.append(f"Invalid command : {command}")  # shows the error

    def execute_command(self, command):
        command_parts = command.split
        action = command_parts[0]

        if action == "Launch":
            self.launch(command_parts[1])  # This launches the drone.
        elif action == "Fly":
            self.fly()
        elif action == "Right":
            self.right()
        elif action == "Left":
            self.left()
        elif action == "Status":
            self.status()
            print(self.status())

    def launch_drone(self, parameters):
        x, y, direction = parameters.split(",")  # separates the command with commas
        self.launch(int(x), int(y), direction)  # calls the launch function from drone

        x = int(x)
        y = int(y)  # Takes the positions
