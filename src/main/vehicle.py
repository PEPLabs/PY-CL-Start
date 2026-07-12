# There is no need to edit this file.

class Vehicle:
    def __init__(self):
        self.current_speed = 0
        self.make = ""
        self.model = ""

    def accelerate(self):
        self.current_speed += 5
        return self.current_speed

    def honk(self):
        return "HONNNK"