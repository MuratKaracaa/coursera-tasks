def extended_gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def ChineseRemainderTheorem(n1, r1, n2, r2):
    gcd, x, y = extended_gcd(n1, n2)
    lcm = (n1 * n2) // gcd

    if (r2 - r1) % gcd != 0:
        return None

    k = (r2 - r1) // gcd

    base = r1 + (k * n1 * x)
    res = ((base % lcm) + lcm) % lcm
    assert res % n1 == r1
    assert res % n2 == r2
    return res


print(ChineseRemainderTheorem(11, 3, 17, 7))
