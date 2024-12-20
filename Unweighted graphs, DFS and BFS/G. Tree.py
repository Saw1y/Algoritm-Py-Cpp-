# Имеется неориентированный граф, состоящий из N вершин и M ребер. Необходимо проверить, является ли граф деревом. 
# Напомним, что дерево — это связный граф, в котором нет циклов (следовательно, между любой парой вершин существует ровно один простой путь). 
# Граф называется связным, если от одной вершины существует путь до любой другой.

# Входные данные
# Во входном файле в первой строке содержатся два целых числа N и M (1 ≤ N ≤ 100, 0 ≤ M ≤ 1000), записанные через пробел. 
# Далее следуют M различных строк с описаниями ребер, каждая из которых содержит два натуральных числа Ai и Bi (1 ≤ Ai <Bi ≤ N), где Ai и Bi — номера вершин, соединенных i-м ребром.

# Выходные данные
# В выходной файл выведите слово YES, если граф является деревом или NO в противном случае.

from sys import setrecursionlimit
setrecursionlimit(100000)


def dfs(start):
    global visited
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(v)


def paint_dfs(vertex, parent):
    global cycle
    color[vertex] = "Gray"
    for v in graph[vertex]:
        if v == parent:
            continue
        if color[v] == "White":
            paint_dfs(v, vertex)
        if color[v] == "Gray":
            cycle = True
    color[vertex] = "Black"

n, m = map(int, input().split())

if n - 1 == m:
    graph = {i + 1: set() for i in range(n)}
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    color = ["white"] * (n + 1)
    cycle = False
    for i in range(1, n + 1):
        if color[i] == "white":
            paint_dfs(i, 0)
            if cycle:
                break

    visited = [False] * (n + 1)
    dfs(1)
    print("YES" if not cycle and all(visited[1:]) else "NO")
else:
    print("NO")
