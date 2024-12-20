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
        
    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def bypass(self):
        key = []
        self._bypass(self.root, key)
        return key

    def _bypass(self, node, key):
        if node is not None:
            self._bypass(node.left, key)
            key.append(node.data)
            self._bypass(node.right, key)

    def find_two_max(self):
        current = self.root
        parent = None
        while current.right is not None:
            parent = current
            current = current.right
        if current.left is not None:
            current = current.left
            while current.right is not None:
                current = current.right
            return current.data
        else:
            return parent.data
if __name__ == "__main__":
    bst = BinarySearchTree()
    num = [int(x) for x in input().split()][:-1]
    for number in num:
        bst.insert(number)
    print(*bst.bypass())