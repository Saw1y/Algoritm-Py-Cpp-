# В стране N городов, некоторые из которых соединены между собой дорогами. Для того, чтобы проехать по одной дороге, 
# требуется один бак бензина. В каждом городе бак бензина имеет разную стоимость. Вам требуется добраться из первого города в N-ый, 
# потратив как можно меньшее денег. Покупать бензин впрок нельзя.

# Входные данные
# В первой строке вводится число N (1≤N≤100), в следующей строке идет N чисел, i-ое из которых задает стоимость бензина в i-ом городе 
# (всё это целые числа из диапазона от 0 до 100). Затем идет число M – количество дорог в стране, далее идет описание самих дорог. 
# Каждая дорога задается двумя числами – номерами городов, которые она соединяет. 
# Все дороги двухсторонние (то есть по ним можно ездить как в одну, так и в другую сторону), между двумя городами всегда существует 
# не более одной дороги, не существует дорог, ведущих из города в себя.

# Выходные данные
# Требуется вывести одно число – суммарную стоимость маршрута или -1, если добраться невозможно.

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


n = int(input())
weights = list(map(int, input().split()))
m = int(input())

graph = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    s, f = map(int, input().split())
    graph[s][f] = weights[s - 1]
    graph[f][s] = weights[f - 1]

dist = dijkstra(graph, 1, n)

if dist == float('inf'):
    print(-1)
else:
    print(dist)
