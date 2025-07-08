def turn_right_90():
    Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
            Kitronik_Move_Motor.MotorDirection.FORWARD,
            speed)
    Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
        Kitronik_Move_Motor.MotorDirection.REVERSE,
        speed)
    basic.pause(turnTime)
    Kitronik_Move_Motor.stop()

# Task 2 - Add function to turn left


# This functions tells the MicroMouse to move forward until it's a specifiec
# distance from the wall, this value is stored in 'distanceToWall'.
def move_to_wall():
    while Kitronik_Move_Motor.measure() > distanceToWall:
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
    # Add you functions calls here to navigate the maze

    pass  

# DO NOT touch this code - it is needed to stop the mouse from veering to the side.
biasValue = 3
Kitronik_Move_Motor.motor_balance(Kitronik_Move_Motor.SpinDirections.RIGHT, biasValue)
Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)

# Add your variables for speed and distance to wall here
speed = 0
turnTime = 0
distanceToWall = 0


# Calls function to exit the maze
navigate_maze()