def prime(n):
    if n < 2:
        return False
    sqrtn = int(n ** (1 / 2))
    for i in range(2, sqrtn + 1):
        if n % i == 0:
            return False
    return True


 
a = 0
for i in range(1, 1000001):
    if prime(i):
        a += 1

print(a)
#число простых в диапозоне от 1 до миллиона: 78498
