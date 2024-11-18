import turtle
import math

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# File name setup
TEXTFILENAME = 'Turtle-draw.txt'

# Welcome message
print('TurtleDraw_xx - Part 3')
user_input = input('Enter the name of the input file (default: Turtle-draw.txt): ')
if user_input.strip():
    TEXTFILENAME = user_input.strip()

# Turtle screen setup
screen = turtle.Screen()
screen.setup(450, 450)

# Turtle setup
turtledraw = turtle.Turtle()
turtledraw.speed(0)  # Maximum speed
turtledraw.penup()   # Start with the pen up

total_distance = 0
point_current = (0, 0)  # Starting at the origin

print('Reading the file and drawing...')
try:
    with open(TEXTFILENAME, 'r') as turtleDrawTextfile:
        for line in turtleDrawTextfile:
            line = line.strip()
            print(line)
            parts = line.split()
            
            if len(parts) == 3:
                # Change color and move to the next point
                color, x, y = parts[0], int(parts[1]), int(parts[2])
                point_next = (x, y)
                turtledraw.color(color)
                turtledraw.goto(x, y)
                if turtledraw.isdown():
                    total_distance += calculate_distance(point_current, point_next)
                turtledraw.pendown()
                point_current = point_next
            elif len(parts) == 1 and parts[0].lower() == "penup":
                turtledraw.penup()
            elif len(parts) == 1 and parts[0].lower() == "pendown":
                turtledraw.pendown()
            elif len(parts) == 1 and parts[0].lower() == "stop":
                turtledraw.penup()

    print(f'Total distance traveled by the turtle: {total_distance}')

    # Display the total distance on the screen
    turtledraw.penup()
    turtledraw.goto(-200, -200)  # Bottom-left of the screen
    turtledraw.color("black")
    turtledraw.write(f"Total Distance: {total_distance:.2f}", font=("Arial", 12, "normal"))

except FileNotFoundError:
    print(f"Error: File '{TEXTFILENAME}' not found.")
except ValueError as e:
    print(f"Error processing the file: {e}")
finally:
    print("File processing complete. Closing file...")

# Wait for user interaction to close
print("Press Enter to close the window.")
turtle.done()

