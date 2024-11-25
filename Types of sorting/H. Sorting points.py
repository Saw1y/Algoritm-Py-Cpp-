# Выведите все исходные точки в порядке возрастания их расстояний от начала координат.
# Создайте структуру Point и сохраните исходные данные в массиве структур Point.

# Входные данные
# Программа получает на вход набор точек на плоскости. Сначала задано количество точек n, затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки. 
# Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 103.

# Выходные данные
# Необходимо вывести  все исходные точки в порядке возрастания их расстояний от начала координат. Программа выводит только координаты точек, их количество выводить не надо.

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.space = self.x ** 2 + self.y ** 2

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_spacing(self):
        return self.space    
    
def Bubble_sort(arr):
    swapped = False
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j][2] > arr[j+1][2]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


N = int(input())
points = [ [ 0 ] * 3 ] * N
for i in range(N):
    x, y = map(int, input().split())
    coord = Point(x, y)
    points[i] = [coord.get_x() , coord.get_y(), coord.get_spacing()]
Bubble_sort(points)
for i in range(N):
    print(points[i][0], points[i][1])
