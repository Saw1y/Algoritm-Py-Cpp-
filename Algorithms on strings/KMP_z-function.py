# Найти все вхождения строки T в строку S.

# Входные данные
# Первые две строки входных данных содержат строки S  и T, соответственно. 
# Длины строк больше 0 и меньше 50000, строки содержат только строчные латинские буквы.

# Выходные данные
# Выведите номера символов, начиная с которых строка T входит в строку S, в порядке возрастания.
def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        k = max(0, min(z[i - left], right - i))
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + k > right:
            left, right = i, i + k
    return z


t = str(input())
s = str(input())

t = s + '#' + t
arr = z_func(t)
for i in range(len(arr)):
    if arr[i] == len(s):
        print(i - len(s) - 1, end=" ")
