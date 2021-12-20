def prme(n):
    if n in [1, 2, 3]:
        return True
    sqrtn = int(n ** (1 / 2))
    for i in range(2, sqrtn + 1):
        if n % i == 0:
            return False
      return True
