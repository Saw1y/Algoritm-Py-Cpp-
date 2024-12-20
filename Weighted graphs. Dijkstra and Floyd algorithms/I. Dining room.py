# Сегодня у студентов праздник! В одном из новых зданий университета решили открыть столовую. 
# Для этих целей требуется выбрать одно из зданий, в котором и будет располагаться столовая. 
# Чтобы студенты как можно меньше отвлекались от учёбы, было решено выбрать такое здание, 
# чтобы максимальное расстояние от него до всех остальных зданий было как можно меньше.

# Помогите найти такое здание!

# Входные данные
# В первой строке находятся два числе 𝑁
#  и 𝑀- количество зданий и количество дорог, соединяющих здания (1≤𝑁≤100,0≤𝑀≤𝑁⋅(𝑁−1)2
# ). Далее в 𝑀строках расположены описания дорог: 3 целых числа 𝑠𝑖, 𝑒𝑖, 𝑙𝑖
#  - здания, в которых начинается и заканчивается дорога и длина дороги соответственно (1≤𝑠𝑖,𝑒𝑖≤𝑁,0≤𝑙𝑖≤100, дороги двунаправленные).

# Выходные данные
# Необходимо вывести одно число - номер искомого здания. Если есть несколько зданий удовлетворяющих поставленным критериям, выберите среди них здание с наименьшим номером.

def floyd(graph, n):
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]

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


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = -1


for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s - 1][e - 1] = w
    graph[e - 1][s - 1] = w
res = floyd(graph, n)

num = 0
mn = float("inf")
for i in range(n):
    temp = max(res[i])
    if temp < mn:
        num = i
        mn = temp
print(num + 1)