from motor import Motor

class Car:
    def __init__(self):
        self.left_motor = Motor("L Motor")
        self.right_motor = Motor("R Motor")

    def go_straight(self):
        self.left_motor.set_speed(100)
        self.right_motor.set_speed(100)

    def turn_left(self):
        self.left_motor.set_speed(-50)
        self.right_motor.set_speed(50)

    def turn_right(self):
        self.left_motor.set_speed(50)
        self.right_motor.set_speed(-50)

    def go_backward(self):
        self.left_motor.set_speed(-100)
        self.right_motor.set_speed(-100)

    def stop(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)
