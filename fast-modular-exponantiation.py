import math


def calculate(b, k, m):
    result = b % m
    for _ in range(k):
        result = (result * result) % m

    return result


def FastModularExponentiation(b, e, m):
    powers = []
    while e > 0:
        next_power = math.floor(math.log(e, 2))
        powers.append(next_power)
        e = e - 2 ** next_power

    res = 1
    for power in powers:
        res = (res * calculate(b, power, m)) % m

    return res


b = 7
k = 3
m = 1000

print(calculate(b, k, m))
print(FastModularExponentiation(b, 2 ** k, m))
print(pow(b, 2 ** k, m))
