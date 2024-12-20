# Дан ориентированный граф. Требуется определить, есть ли в нем цикл.

# Входные данные
# В первой строке вводится число вершин N≤ 50. Далее в N строках следуют по N чисел, каждое из которых – 0 или 1. 
# j-ое число в i-ой строке равно 1 тогда и только тогда, когда существует ребро, идущее из i-ой вершины в j-ую. Гарантируется, что на диагонали матрицы будут стоять нули.

# Выходные данные
# Выведите 0, если в заданном графе цикла нет, и 1, если он есть.

from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(start):
    global cycle
    color[start] = 'gray'
    for w in graph[start]:
        if color[w] == 'white':
            dfs(w)
        if color[w] == 'gray':
            cycle = True
    color[start] = 'black'


n = int(input())
w = [] * n
for i in range(n):
    w.append(input().split(' '))
graph = {i + 1: set() for i in range(n)}

for i in range(n):
    for j in range(n):
        if w[i][j] == '1':
            graph[i + 1].add(j + 1)

color = ['white'] * (n + 1)
cycle = False
for v in range(1, n + 1):
    if color[v] == 'white':
        dfs(v)
        if cycle:
            print(1)
            break
else:
    print(0)
