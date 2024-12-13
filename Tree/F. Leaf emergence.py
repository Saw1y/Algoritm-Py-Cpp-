#  Вывод листьев
# Для полученного дерева выведите список всех листьев (вершин, не имеющих потомков) в порядке возрастания.

# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит.

# Выходные данные
# Выведите ответ на задачу.
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            curr_node = self.root
            while True:
                if key < curr_node.data:
                    if curr_node.left is None:
                        curr_node.left = Node(key)
                        break
                    curr_node = curr_node.left
                elif key > curr_node.data:
                    if curr_node.right is None:
                        curr_node.right = Node(key)
                        break
                    curr_node = curr_node.right
                else:
                    break

    def leaves(self):
        key = []
        self._leaves(self.root, key)
        return key
    
    def _leaves(self, node, key):
        if node is not None:
            if node.left is None and node.right is None:
                key.append(node.data)
            else:
                self._leaves(node.left, key)
                self._leaves(node.right, key)


if __name__ == "__main__":
    bst = BinarySearchTree()
    num = [int(x) for x in input().split()][:-1]
    for number in num:
        bst.insert(number)
    print(*bst.leaves())
