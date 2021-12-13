def prime(n):
    sqrtn = int(n ** (1/2))
    k = 0
    for i in range(1, sqrtn + 1):
        if n in [1, 2, 3]:
            k = 1
            break
        if n % i != 0:
            k = 1
        else:
            k = 0
            break
    if k == 0:
        return "составное"
    return "простое"
