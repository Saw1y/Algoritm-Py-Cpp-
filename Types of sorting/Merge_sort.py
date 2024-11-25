# Отсортируйте данный массив, используя сортировку слиянием.
#
# Входные данные
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее идет N целых чисел, не превосходящих по абсолютной величине 109.
#
# Выходные данные
# Выведите эти числа в порядке неубывания.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr) // 2
    left = merge_sort(arr[:ind])
    right = merge_sort(arr[ind:])
    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1 
    res += left[i:] + right[j:]
    return res

N = int(input())
arr = list(map(int, input().split()))
res_arr = merge_sort(arr)
print(*res_arr)
