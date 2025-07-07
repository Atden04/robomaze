# Task 2 - Please turn right
def turn_right_90():
    # Add code here
    basic.pause(450)
    Kitronik_Move_Motor.stop()

# Task 3 - Now turn left


# Task 5 - Move forward
def move_to_wall():
    while Kitronik_Move_Motor.measure() > distanceToWall:
        # Add Code here
        basic.pause(100)
    Kitronik_Move_Motor.stop()

# Task 6 - Escape the maze!


# DO NOT touch this code - it is needed to stop the mouse from veering to the side.
biasValue = 3
Kitronik_Move_Motor.motor_balance(Kitronik_Move_Motor.SpinDirections.RIGHT, biasValue)
Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)

# Add your variables for speed and distance to wall here
distanceToWall = 0

# Call your function to escape the maze


# Task 4 - Object ahead!
def on_forever():
    # Add code here

basic.forever(on_forever)