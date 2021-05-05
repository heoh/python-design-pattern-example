class Motor:
    def __init__(self, name):
        self.name = name

    def set_speed(self, val):
        print(f"[{self.name}] speed: {val}")
