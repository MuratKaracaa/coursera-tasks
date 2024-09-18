def extended_gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def divide(a, b, n):
    d, k, l = extended_gcd(a, n)
    assert d == 1

    inverse = n + k

    return (b * inverse) % n
