import math
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')
import matplotlib.pyplot as plt
import numpy as np
import cmath
ITERATIONS = 50


def my_cos(x):
    """
    Вычисление косинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    cos = 0
    for i in range(0, ITERATIONS):
        cos += ((-1) ** i) * (multiplier / math.factorial(2 * i))
        multiplier *= x_pow ** 2
    return cos


vs = np.vectorize(my_cos)
angles = np.r_[-40:40:0.01]
plt.plot(angles, np.cos(angles))
plt.plot(angles, vs(angles))

complex_angle = cmath.acos(5)

print(math.cos(0.4))
print(my_cos(0.4))
print(my_cos, vs)
print(cmath.cos(complex_angle))
print(my_cos(complex_angle))


plt.show()


