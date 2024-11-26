# Дано кубическое уравнение ax3+bx2+cx+d=0(a≠0). Известно, что у этого уравнения ровно один корень. Требуется его найти.

# Входные данные
# Во входных данных через пробел записаны четыре целых числа: −1000≤a,b,c,d≤1000.

# Выходные данные
# Выведите единственный корень уравнения с точностью не менее 4 знаков после десятичной точки.

def f(x):
    global a, b, c, d
    return a * x * x * x + b * x * x + c * x + d


def set_interval():
    left = -1
    right = 1
    while f(left) * f(right) >= 0:
        right *= 2
        left = -right
    return left, right


def bin_search(left, right):
    eps = 1e-10
    while (right - left) > eps:
        middle = (right + left) / 2
        if f(middle) == 0:
            return middle
        elif f(middle) * f(right) > 0:
            right = middle
        else:
            left = middle
    return middle


a, b, c, d = map(int, input().split())
left, right = set_interval()
result = bin_search(left, right)
print(round(result, 4))
