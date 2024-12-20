# Дана непустая строка s, длина которой N не превышает 106. Будем считать, что элементы строки нумеруются от 1 до N.

# Для каждой позиции i символа в строке определим Z-блок как наибольшую подстроку, 
# которая начинается в этой позиции и совпадает с некоторым началом всей строки s. 
# Значением Z-функции Z(i) будем считать длину этого Z-блока. (Заметим, что для первой позиции строки  Z-блок совпадает со всей строкой, 
# поэтому Z(1)=N. С другой стороны, если s[i]≠s[1], то Z(i)=0).

# Z-функция используется в различных алгоритмах обработки строк. В частности,
# с её помощью можно быстро решать задачу о поиске вхождения одной строки в другую («поиск по образцу»).

# Требуется для всех i от 1 до N вычислить Z(i).

# Входные данные
# Одна строка длины N, 0 < N ≤ 106, состоящая из маленьких латинских букв.

# Выходные данные
# N чисел, разделенные пробелами: Z(1), Z(2), ... Z(N)

def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(n):
        k = max(0, min(z[i - left], right - i))
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + k > right:
            left, right = i, i + k
    return z


print(*z_func(str(input())))
