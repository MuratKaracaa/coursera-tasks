def extended_gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def diophantine(a, b, c):
    d, x, y = extended_gcd(a, b)
    print(d, x, y)
    assert c % d == 0

    t = c / d

    k = t * x
    l = t * y

    return k, l


diophantine(3, 5, 22)
