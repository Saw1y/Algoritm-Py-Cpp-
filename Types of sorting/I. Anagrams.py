# Слово называется анаграммой другого слова, если оно может быть получено перестановкой его символов.
#
# Входные данные
# Даны два слова на отдельных строках. Слова состоят из строчных латинских букв и цифр. Длины слов не превышают 255.
#
# Выходные данные
# Требуется вывести "YES"  – если введенные слова являются анаграммами друг друга, "NO"  – если нет.
#
# Примечание
#
# Сложность работы программы должна быть O(n). Использование встроенной сортировки(sort, sorted), алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!

ch1 = input()
ch2 = input()

N1 = len(ch1)
N2 = len(ch2)
if N1 == N2: 
    N = N1 
else: 
    print("NO")
    exit() 

dict1 = {x: 0 for x in (set(ch1))}
dict2 = {x: 0 for x in (set(ch2))}
for i in range(N): 
    dict1[ch1[i]] += 1
    dict2[ch2[i]] += 1
if dict1 != dict2:
    print("NO")
else:
    print("YES")
