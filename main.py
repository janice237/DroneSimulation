# main.py
from commandProcessor import CommandProcessor

def main():
    drone = CommandProcessor(max_x=5, max_y=5)

    print("Welcome to the Drone Simulation!")
    print("Enter commands to control the drone:")

    while True:
       initial_input = input('Enter initial position and direction(x,y, direction):')
       x,y,direction = initial_input.strip().split(",")

       print(f"LAUNCH {x},{y},{direction.upper()}")

            return main()

if __name__ == "__main__":
    main()