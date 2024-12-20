# Найти все вхождения строки T в строку S.

# Входные данные
# Первые две строки входных данных содержат строки S  и T, соответственно. 
# Длины строк больше 0 и меньше 50000, строки содержат только строчные латинские буквы.

# Выходные данные
# Выведите номера символов, начиная с которых строка T входит в строку S, в порядке возрастания.

def prefix(st):
    pi = [0] * len(st)
    for i in range(1, len(st)):
        curr = pi[i - 1]
        while curr > 0 and st[curr] != st[i]:
            curr = pi[curr - 1]
        if st[i] == st[curr]:
            curr = curr + 1
        pi[i] = curr
    return pi


t = str(input())
s = str(input())

t = s + '#' + t

arr = prefix(t)
for i in range(len(s), len(t)):
    if arr[i] == len(s):
        print(i - len(s) * 2, end=" ")
