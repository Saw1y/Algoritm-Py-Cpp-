# Отсортируйте данный массив. Используйте пирамидальную сортировку.

# Входные данные
# Первая строка входных данных содержит количество элементов в массиве N,  N  ≤  105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

# Выходные данные
# Выведите эти числа в порядке неубывания.
class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
            else:
                break

    def sift_down(self, i):
        while i * 2 <= self.size:
            j = i * 2
            if i * 2 + 1 <= self.size and self.heap[i * 2] > self.heap[i * 2 + 1]:
                j += 1
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
            else:
                break

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.sift_up(self.size)

    def del_min(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sift_down(1)
        return removed


heap = Heap()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    heap.insert(arr[i])

res = []
for i in range(n):
    res.append(heap.del_min())

print(*res)
