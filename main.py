# main.py
from commandProcessor import CommandProcessor


def main():
    drone = CommandProcessor(max_x=5, max_y=5)

    max_attempts = 7
    for attempt in range(max_attempts):
        initial_input = print("Enter an initial position and direction(x,y direction)")
        x, y, direction = initial_input.split(",")

    print(f"Parsed values -x:{x}, -y:{y}, -direction:{direction}")
    drone.add_command = print(f"Launch{x},{y},{direction}:")
    print(drone.status())  # Show status
    print(f"current position is ({x}), ({y}), ({direction.upper()}")


if __name__ == "__main__":
    main()
