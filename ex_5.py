class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_vector(self, vector):
        x, y = self.x + vector.x, self.y + vector.y
        return Vector(x, y)

    def subtract_vector(self, vector):
        x, y = self.x - vector.x, self.y - vector.y
        return Vector(x, y)

    def subtract_from_vector(self, vector):
        x, y = vector.x - self.x, vector.y - self.y
        return Vector(x, y)

    def mul_vector(self, k):
        x, y = k * self.x, k * self.y
        return Vector(x, y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"