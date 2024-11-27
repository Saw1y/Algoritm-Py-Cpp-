# В этой задаче вам необходимо организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции:

#    a) Insert(k) – добавить в Heap число k (1 ≤  k ≤ 1000000) ;
#    b) Extract достать из Heap наибольшее число (удалив его при этом).

# Входные данные
# В первой строке содержится количество команд N (1 ≤  N ≤ 100000), далее следуют N команд, каждая в своей строке. 
# Команда может иметь  формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполенении команды Extract в структуре находится по крайней мере один элемент.
class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shift_up(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def shift_down(self, i):
        while i * 2 <= self.size:
            if i * 2 + 1 > self.size:
                j = i * 2
            else:
                j = i * 2 if self.heap[i * 2] > self.heap[i * 2 + 1] else i * 2 + 1
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.shift_up(self.size)

    def extract(self):
        if self.size == 0:
            return None
        mx = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shift_down(1)
        return mx


n = int(input())
my_heap = Heap()
for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 0:
        my_heap.insert(command[1])
    elif command[0] == 1:
        print(my_heap.extract())
    else:
        print('Error')
