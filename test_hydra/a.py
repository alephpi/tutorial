class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"A(x={self.x}, y={self.y}, z={self.z})"