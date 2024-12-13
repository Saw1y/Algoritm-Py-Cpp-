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
            cur_node = self.root
            while True:
                if key < cur_node.data:
                    if cur_node.left is None:
                        cur_node.left = Node(key)
                        break
                    cur_node = cur_node.left
                elif key > cur_node.data:
                    if cur_node.right is None:
                        cur_node.right = Node(key)
                        break
                    cur_node = cur_node.right
                else:
                    break

    def find_two_child(self):
        key = []
        self._find_two_child(self.root, key)
        return key

    def _find_two_child(self, node, key):
        if node is not None:
            if node.left is not None and node.right is not None:
                key.append(node.data)
            self._find_two_child(node.left, key)
            self._find_two_child(node.right, key)


if __name__ == "__main__":
    bst = BinarySearchTree()
    num = [int(x) for x in input().split()][:-1]
    for number in num:
        bst.insert(number)
    children = bst.find_two_child()
    children.sort()
    print(*children)
