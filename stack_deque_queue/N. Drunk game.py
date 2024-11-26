# В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без карт – проигрывает.

# Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту ("шестерка берет туза").

# Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды).

# Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.

# Входные данные
# Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт второго игрока. 
# Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

# Выходные данные
# Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second, после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 106 ходов игра не заканчивается, программа должна вывести слово botva.

from collections import deque

player1 = list(map(int, input().split()))
player2 = list(map(int, input().split()))

deq1 = deque()
deq2 = deque()

for i in range(len(player1)):
    deq1.append(player1[i])
    deq2.append(player2[i])
i = 0
while True:
    i += 1
    if deq1[0] == 0 and deq2[0] == 9:
        deq1.append(deq1.popleft())
        deq1.append(deq2.popleft())
    elif deq1[0] == 9 and deq2[0] == 0:
        deq2.append(deq1.popleft())
        deq2.append(deq2.popleft())
    else:
        if deq1[0] > deq2[0]:
            deq1.append(deq1.popleft())
            deq1.append(deq2.popleft())
        else:
            deq2.append(deq1.popleft())
            deq2.append(deq2.popleft())
    if len(deq1) == 0 or len(deq2) == 0 or i == 10 ** 6:
        break

if len(deq2) == 0:
    print(f"first {i}")
elif len(deq1) == 0:
    print(f"second {i}")
else:
    print("botva")