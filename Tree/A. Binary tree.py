# # Напишите программу, которая будет реализовывать действия в бинарном дереве поиска «вставить», «удалить» и «найти» (по значению). Программа должна обрабатывать запросы четырёх видов:

# # ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово «DONE», если уже есть — оставлять дерево как было и выводить слово «ALREADY».

# # DELETE n — если указанное число есть в дереве, удалять его и выводить слово «DONE», если нет — оставлять дерево как было и выводить слово «CANNOT». При удалении элемента, имеющего два сына, обязательно обменивать значение с максимальным элементом левого поддерева.

# # SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или слово «NO» (если не найдено). Дерево при этом не меняется.

# # PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в формате вывода результатов.

# # Входные данные
# # В каждой строке входных данных записан один из запросов ADD n или DELETE n или SEARCH n или PRINTTREE. 
# Гарантируется, что запросы PRINTTREE будут вызываться только в моменты, когда дерево не пустое. Общее количество запросов не превышает 1000, из них не более 20 запросов PRINTTREE.

# # Выходные данные
# # Для каждого запроса выводите ответ на него. Для запросов ADD, DELETE и SEARCH — соответствующее слово в отдельной строке. 
#   На запрос PRINTTREE надо выводить дерево, обязательно согласно такому алгоритму:

from sys import stdin


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_max(self):
        if self.root is None:
            return f'{str(None)}'
        return self._max_node(self.root).data

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def find_min(self):
        if self.root is None:
            return f'{str(None)}'
        return self._min_node(self.root).data

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

    def print_tree(self, node, level):
        if node is None:
            return None
        self.print_tree(node.left, level + 1)
        for _ in range(level):
            print('.', end='')
        print(node.data)
        self.print_tree(node.right, level + 1)
if __name__ == "__main__":
    bst = BinarySearchTree()
    num = stdin.readlines()
    for commands in num:
        commands = commands.split()
        comm = commands[0]
        if comm == "ADD":
            num = int(commands[-1])
            if bst.search(num):
                print("ALREADY")
            else:
                bst.insert(num)
                print("DONE")
        elif comm == "DELETE":
            num = int(commands[-1])
            if bst.search(num):
                bst.delete(num)
                print("DONE")
            else:
                print("CANNOT")
        elif comm == "SEARCH":
            num = int(commands[-1])
            if bst.search(num):
                result = "YES"
            else:
                result = "NO"
            print(result)
        elif comm == "PRINTTREE":
            bst.print_tree(bst.root, 0)
