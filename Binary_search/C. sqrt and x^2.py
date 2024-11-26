# Найдите такое число x, что x2+√x=C, с точностью не менее 6знаков после точки.

# Входные данные
# В единственной строке содержится вещественное число 1.0≤C≤1010.

# Выходные данные
# Выведите одно число — искомый x.

def bin_search(c):
    left = 1.0
    right = 10 ** 10
    eps = 10 ** -10
    while abs(right - left) > eps:
        x = (right + left) / 2
        res = x * x + x ** 0.5
        if res == c:
            return x
        elif res > c:
            right = x
        else:
            left = x
    return x


c = float(input())
result = bin_search(c)
print(round(result, 6))
