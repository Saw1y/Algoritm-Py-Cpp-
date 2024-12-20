# Строка S была записана много раз подряд, после чего из получившейся строки взяли подстроку и дали вам. 
# Ваша задача определить минимально возможную длину исходной строки S.

# Входные данные
# На вход программы поступает строка, которая содержит только латинские буквы, длина строки не превышает 100000 символов.

# Выходные данные
# Требуется вывести одно число – ответ  на вопрос задачи.


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


s = input()
pref = prefix(s)
n = len(s)
print(n - pref[len(s) - 1])