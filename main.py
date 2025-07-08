# Task 2 - Please turn right
def turn_right_90():
    # Add code here
    Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
            Kitronik_Move_Motor.MotorDirection.FORWARD,
            speed)
    Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
        Kitronik_Move_Motor.MotorDirection.REVERSE,
        speed)
    basic.pause(450)
    Kitronik_Move_Motor.stop()

# Task 3 - Now turn left


# Task 5 - Move forward
def move_to_wall():
    while Kitronik_Move_Motor.measure() > distanceToWall:
        # Add Code here
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                    Kitronik_Move_Motor.MotorDirection.FORWARD,
                    speed)
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
            Kitronik_Move_Motor.MotorDirection.FORWARD,
            speed)
        basic.pause(100)
    Kitronik_Move_Motor.stop()

# Task 6 - Escape the maze!
def navigate_maze():
    turn_right_90()
    turn_right_90()

# DO NOT touch this code - it is needed to stop the mouse from veering to the side.
biasValue = 3
Kitronik_Move_Motor.motor_balance(Kitronik_Move_Motor.SpinDirections.RIGHT, biasValue)
Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)

# Add your variables for speed and distance to wall here
distanceToWall = 0

# Call your function to escape the maze
speed = 20

navigate_maze()
