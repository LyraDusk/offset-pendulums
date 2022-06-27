import math

class Pendulum:
    def __init__(self, length, max_angle):
        self.length = length
        self.max_angle = max_angle
        self.period = 2 * math.pi * math.sqrt(self.length/9.8)
        self.angle = max_angle

    # Using the small-angle approximation for sinusoidal movement
    def update_angle(self, time):
        a_const = 2 / self.period
        new_angle = self.max_angle * math.sin(a_const * math.pi * time)
        self.angle = new_angle
        return self.angle

    def get_angle(self):
        return self.angle

    def get_length(self):
        return self.length
