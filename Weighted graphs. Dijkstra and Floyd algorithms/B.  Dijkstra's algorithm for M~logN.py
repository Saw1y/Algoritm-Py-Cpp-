# Напишите программу, которая будет находить расстояния в неориентированном взвешенном графе с неотрицательными длинами ребер, от указанной вершины до всех остальных. 
# Программа должна работать быстро для больших разреженных графов.

# Входные данные
# В первой строке входных данных задано число NUM — количество различных запусков алгоритма Дейкстры (на разных графах). 
# Далее следуют NUM блоков, каждый из которых имеет следующую структуру.

# Первая строка блока содержит два числа N и M, разделенные пробелом — количество вершин и количество ребер графа. 
# Далее следуют M строк, каждая из которых содержит по три целых числа, разделенные пробелами. 
# Первые два из них в пределах от 0 до N–1 каждое и обозначают концы соответствующего ребра, третье — в пределах от 0 до 20000 и обозначает длину этого ребра. 
# Далее, в последней строке блока, записанное единственное число от 0 до N–1 — вершина, расстояния от которой надо искать.

# Количество различных графов в одном тесте NUM не превышает 5. Количество вершин не превышает 60000, рёбер — 200000.

# Выходные данные
# Выведите на стандартный выход (экран) NUM строк, в каждой из которых по Ni чисел, разделенных пробелами — расстояния от указанной начальной вершины взвешенного 
# неориентированного графа до его 0-й, 1-й, 2-й и т. д. вершин (допускается лишний пробел после последнего числа). Если некоторая вершина недостижима от указанной начальной, вместо расстояния выводите число 2009000999 (гарантировано, что все реальные расстояния меньше).


import heapq

INF = 2009000999


def dijkstra(graph, start, n):
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex].items():
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist

NUM = int(input())
for _ in range(NUM):
    n, m = map(int, input().split())

    graph = {i: {} for i in range(n)}

    for _ in range(m):
        v1, v2, weight = map(int, input().split())
        graph[v1][v2] = weight
        graph[v2][v1] = weight

    start = int(input())

    dist = dijkstra(graph, start, n)

    for i in range(n):
        if dist[i] < INF:
            print(dist[i], end=" ")
        else:
            print(INF, end=" ")
    print()
