# Задан ориентированный ациклический граф с 𝑛
#  вершинами и 𝑚
#  ребрами. Также задана перестановка вершин графа. Необходимо проверить, является ли данная перестановка топологической сортировкой.

# Входные данные
# В первой строке даны два числа 𝑛
#  и 𝑚
#  — количество вершин и ребер в графе соответственно (1≤𝑛,𝑚≤105
# ). В следующих 𝑚строках заданы пары чисел 𝑢𝑖,𝑣𝑖, означающие, что в графе есть ребро из вершины 𝑢𝑖 в вершину 𝑣𝑖 .
# В последней строке задана перестановка из 𝑛 элементов.

# Выходные данные
# Выведите "YES" (без кавычек), если данная перестановка является топологической сортировкой и "NO" в противном случае.

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

swap = list(map(int, input().split()))

position = [0] * (n + 1)
for idx, vertex in enumerate(swap):
    position[vertex] = idx

ans = "YES"
for u in range(1, n + 1):
    for v in graph[u]:
        if position[u] >= position[v]:
            ans = "NO"
            break
    if ans == "NO":
        break

print(ans)
