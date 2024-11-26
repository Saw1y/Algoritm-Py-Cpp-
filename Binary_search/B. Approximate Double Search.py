# Реализуйте алгоритм приближенного бинарного поиска.

# Входные данные
# В первой строке входных данных содержатся числа N
#  и K (0<N,K<100001). Во второй строке задаются N
#  чисел первого массива, отсортированного по неубыванию, а в третьей строке – K
#  чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2⋅10^9.

# Выходные данные
# Для каждого из K
#  чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

def bin_search(arr, x):
    left = 0
    right = len(arr) - 1
    while right - left > 1:
        m = (left + right ) // 2
        if x == arr[m]:
            return x
        elif arr[m] < x:
            left = m
        else:
            right = m
    val1 = abs(arr[left] - x)
    val2 = abs(arr[right] - x)
    if val1 == val2:
        res = arr[left]
    elif val1 < val2:
        res = arr[left]
    else:
        res = arr[right]
    return res


n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(k):
    res = bin_search(arr1 , arr2[i])
    print(res)
