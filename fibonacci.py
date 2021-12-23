import itertools


class Fibonacci:
    """По объектам этого класса можно итерироваться и получать числа фибоначи"""

    class _Fib6_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self. f1 = 1
            self.f2 = 1

        def __next__(self):
            f = self.f1
            self.f1, self.f2 = self.f2, self.f1 + self.f2
            f = self.f1
            return f

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibonacci._Fib6_iter()


fib = Fibonacci()

print(list(itertools.islice(fib, 50)))