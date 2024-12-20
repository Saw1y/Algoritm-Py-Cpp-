def floyd_warshall(graph, n):
    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


n, s, t = map(int, input().split())
s -= 1
t -= 1

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dist = floyd_warshall(graph, n)
if dist[s][t] == float("inf"):
    print(-1)
else:
    print(dist[s][t])
