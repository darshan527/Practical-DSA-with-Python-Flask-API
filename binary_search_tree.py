from re import search


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def _insert_recursive(self, data, root):
        if data['id'] < root.data['id']:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert_recursive(data['id'], root.left)
        elif data['id'] > root.data['id']:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert_recursive(data['id'], root.right)
        else:
            return

    def search(self, id, node):
        if node is None:
            return False
        if node.data['id'] is int(id):
            return node.data
        else:
            if int(id) < node.data['id']:
                search(id, node.left)

            elif int(id) > node.data['id']:
                search(id, node.right)
            else:
                return False

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
