def gcd_line(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        k, x, y = gcd_line(b % a, a) #k - остаток
    return (k, y - (b // a) * x, x)
print(gcd_line(84, 35))
