function turn_right_90() {
    Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, speed)
    Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Reverse, speed)
    basic.pause(turnTime)
    Kitronik_Move_Motor.stop()
}

//  Task 2 - Add function to turn left
//  This functions tells the MicroMouse to move forward until it's a specifiec
//  distance from the wall, this value is stored in 'distanceToWall'.
function move_to_wall() {
    while (Kitronik_Move_Motor.measure() > distanceToWall) {
        Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, speed)
        Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, speed)
        basic.pause(100)
    }
    Kitronik_Move_Motor.stop()
}

//  Task 6 - Escape the maze!
function navigate_maze() {
    //  Add you functions calls here to navigate the maze
    
}

//  DO NOT touch this code - it is needed to stop the mouse from veering to the side.
let biasValue = 3
Kitronik_Move_Motor.motorBalance(Kitronik_Move_Motor.SpinDirections.Right, biasValue)
Kitronik_Move_Motor.setUltrasonicUnits(Kitronik_Move_Motor.Units.Centimeters)
//  Add your variables for speed and distance to wall here
let speed = 0
let turnTime = 0
let distanceToWall = 0
//  Calls function to exit the maze
navigate_maze()
