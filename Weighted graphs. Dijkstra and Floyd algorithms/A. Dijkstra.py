# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

# Входные данные
# В первой строке содержатся три числа: N, S и F (1≤ N≤ 100, 1≤ S, F≤ N), где N – количество вершин графа, S – начальная вершина, а F – конечная. 
# В следующих N строках вводится по N чисел, не превосходящих 100, – матрица смежности графа, где -1 означает отсутствие ребра между вершинами, 
# а любое неотрицательное число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

# Выходные данные
# Требуется вывести искомое расстояние или -1, если пути между указанными вершинами не существует.



import heapq


def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_vertex == end:
            return dist[end]

        if dist[cur_vertex] < cur_dist:
            continue

        for neighbor, weight in graph[cur_vertex].items():
            d = cur_dist + weight
            if d < dist[neighbor]:
                dist[neighbor] = d
                heapq.heappush(pq, (d, neighbor))

    return -1


N, start, end = map(int, input().split())
graph = {i: {} for i in range(1, N + 1)}
for i in range(1, N + 1):
    weight = list(map(int, input().split()))
    for j, w in enumerate(weight):
        if w != -1:
            graph[i][j + 1] = w

print(dijkstra(graph, start, end))
