# # Дана непустая строка S, длина которой N не превышает 106. Будем считать, что элементы строки нумеруются от 1 до N.

# # Для каждой позиции i символа в строке нас будет интересовать подстрока, заканчивающаяся в этой позиции, и совпадающая 
# с некоторым началом всей строки. Вообще говоря, таких подстрок будет несколько, не меньше двух. 
# Самая длинная из них имеет длину i, она нас интересовать не будет. 
# А будет нас интересовать самая длинная из остальных таких подстрок (заметим, что такая подстрока всегда существует — в крайнем случае, 
# если ничего больше не найдется, сгодится пустая подстрока).

# # Значением префикс-функции π[i] будем считать длину этой подстроки.

# # Префикс-функция используется в различных алгоритмах обработки строк. В частности, с её помощью можно быстро решать задачу о поиске вхождения одной строки в другую («поиск образца в тексте»).

# # Требуется для всех i от 1 до N вычислить π[i].

# # Входные данные
# # Одна строка длины N, 0 < N ≤ 106, состоящая из маленьких латинских букв.

# # Выходные данные
# # Выведите N чисел — значения префикс-функции для каждой позиции, разделенные пробелом.

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


print(*prefix(str(input())))
