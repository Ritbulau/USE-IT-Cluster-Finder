class Vector2:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getLength(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalized(self):
        l = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector2(self.x / l, self.y / l)


def addVecs(a, b):
    return Vector2(a.x + b.x, a.y + b.y)


def multiplyVecs(a, b):
    return Vector2(a.x * b.x, a.y * b.y)


def dist(a: Vector2, b: Vector2):
    return Vector2(b.x - a.x, b.y - a.y).getLength()
