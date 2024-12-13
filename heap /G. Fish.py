# Игорь работает младшим лаборантом в НИИ ихтиологии. Ему вверены n аквариумов, стоящих в ряд, в каждом из которых живет колония рыбок гуппи. Про каждую колонию заранее известна ее численность.

# В лабораторных условиях НИИ ихтиологии колония рыбок гуппи растет по следующему правилу: достигнув популяции в f
#  рыбок, колония живет в течении max(1000−f,1) секунд, после чего на свет появляется новая рыбка. От начального момента времени до рождения первой рыбки колония размера f
#  также ждет max(1000−f,1)секунд.
# Появление на свет каждой новой рыбки Игорь должен фиксировать в специальном журнале. Будем считать, что запись он делает мгновенно, но при этом он должен в момент рождения новой рыбки находиться рядом с аквариумом, в котором это произошло.

# На перемещение от одного аквариума к соседнему у Игоря уходит одна секунда. В начальный момент времени Игорь стоит около первого аквариума.

# Вычислите, в течение какого наибольшего периода времени Игорь сможет добросовестно выполнять свою работу.

# Входные данные
# В первой строке входного файла содержится целое число n
#  (2≤n≤50) - количество аквариумов с рыбками гуппи в НИИ ихтиологии. Каждая из следующих n
#  строк содержит одно целое число ai (1≤ai≤2007) - численность i-й колонии.

# Выходные данные
# В выходной файл выведите момент времени, когда родится первая рыбка гуппи, запись о рождении которой Игорь сделать не сможет.

# Примечание
# В приведенном примере Игорь сначала ждет у первого аквариума появления рыбки на 4-й секунде. После этого он бежит к третьему аквариуму (на это у него уходит 2 секунды) и как раз успевает к рождению рыбки на 6-й секунде.
# Однако вернуться к первому аквариуму, где следующая рыбка родится на 7-й секунде, он уже не успевает.

import heapq


def born(f):
    return max(1000 - f, 1)


n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
heap = []
for i in range(n):
    time = born(arr[i])
    heapq.heappush(heap, (time, i))

current_time = 0
current_position = 0

while len(heap) > 0:
    fish_time, num_a = heapq.heappop(heap)

    time_go = abs(num_a - current_position)
    if current_time + time_go > fish_time:
        print(fish_time)
        break

    current_time = fish_time
    current_position = num_a

    arr[num_a] += 1
    next_time = fish_time + born(arr[num_a])
    heapq.heappush(heap, (next_time, num_a))