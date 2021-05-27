

class Tester:
    def __init__(self):
        self.x = "x"
        self.y, self.z = ("y", "z")

    def __repr__(self):
        return "x={}, y={}, z={}".format(self.x, self.y, self.z)

print(Tester())
