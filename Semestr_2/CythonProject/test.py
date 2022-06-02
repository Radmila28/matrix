import work
import time


start_cy = time.time()
work.test(99999999)
end_cy = time.time()
cy_time = end_cy - start_cy

print(f'Время выполнения Cython: {cy_time}')
print('-----------------------------------')


def test(x):
    y = 0
    for i in range(x):
        y += i
    return y


start_py = time.time()
test(99999999)
end_py = time.time()
py_time = end_py - start_py
res = py_time / cy_time

print(f'Время выполнения Python {py_time}')
print(f'Cpyton быстрее в {res} раз')
