import math
import matplotlib.pyplot as mpp

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajektory_x = []
        self.trajektory_y = []

    def advance(self):
        self.trajektory_x.append(self.x)
        self.trajektory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y, vx, vy, a, m, vm):
        super().__init__(x, y, vx, vy)
        self.a = a
        self.m = m
        self.vm = vm

    def advance(self):
        super().advance()
        if self.m > 0:
            if self.m - self.vm * MODEL_DT > 0:
                self.m -= self.vm * MODEL_DT
            else:
                self.m = 0
            self.vy += self.a * MODEL_DT


r = Rocket(0, 0, 10, 10, 5, 500, 100)
b = Body(50, 50, 5, 5)
time = 0

while time < 2:
    r.advance()
    b.advance()
    time += MODEL_DT

mpp.plot(r.trajektory_x, r.trajektory_y)
mpp.show()

mpp.plot(b.trajektory_x, b.trajektory_y)
mpp.show()