# Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.

# Входные данные
# В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S, F≤N), где N – количество вершин графа, S – начальная вершина, а F – конечная.
# В следующих N строках вводится по N чисел, не превосходящих 100, – матрица смежности графа, где -1 означает отсутствие ребра между 
# вершинами, а любое неотрицательное число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

# Выходные данные
# Требуется вывести последовательно все вершины одного (любого) из кратчайших путей, или одно число -1, 
# если пути между указанными вершинами не существует. В ответе примера указано количество вершин, а не сам путь. 
# Ваша программа должна выдавать именно путь.

n, s, f = map(int, input().split())
s -= 1
f -= 1

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
dist = [float("inf")] * n
dist[s] = 0
prev = [-1] * n

for _ in range(n):
    min_dist = float('inf')
    min_index = -1
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_index = i

    if min_index == -1:
        break

    visited[min_index] = True
    for i in range(n):
        if graph[min_index][i] != -1:
            new_dist = dist[min_index] + graph[min_index][i]
            if new_dist < dist[i]:
                dist[i] = new_dist
                prev[i] = min_index
if dist[f] == float('inf'):
    print(-1)
else:
    path = []
    curr = f
    while curr != -1:
        path.append(curr + 1)
        curr = prev[curr]
    print(*path[::-1])
