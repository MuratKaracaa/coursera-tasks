import math


def get_coefficients(n, x, y):
    target_range = n + 1
    combs = []
    coefficients = []

    for i in range(target_range):
        combs = []
        for j in range(target_range):
            comb = math.comb(i, j)
            combs.append(comb)

    for k in range(target_range):
        coefficient = combs[k] * x ** (n - k) * y ** k
        coefficients.append(coefficient)

    return coefficients


print(get_coefficients(7, 3, -2))
