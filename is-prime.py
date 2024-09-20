def min_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

        if i * i > n:
            return n


def is_prime(n):
    return n == min_divisor(n)


print(1980 * 1848 / (2 ** 2 * 3 * 11))
