# Дано два массива. Для каждого элемента второго массива определите, сколько раз он встречается в первом массиве.

# Входные данные
# Первая строка входных данных содержит одно число N (1 ≤ N ≤ 105) – количество элементов в первом массиве. 
# Далее идет N целых чисел, не превосходящих по модулю 109 – элементы первого массива, Далее идет количество элементов M во втором массиве и M элементов второго массива с такими же ограничениями.

# Выходные данные
# Выведите M чисел: для каждого элемента второго массива выведите, сколько раз такое значение встречается в первом массиве.

n = int(input())  
array1 = list(map(int, input().split()))  
m = int(input()) 
array2 = list(map(int, input().split()))  

count = {}
for number in array1:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

for number in array2:
    if number in count:
        print(count[number], end = " ")
    else:
        print(0, end = " ")