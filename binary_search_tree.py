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

    def search_blog(self, blog_id):
        return self.search(int(blog_id), self.root)

    def search(self, id, node):
        if node is None:
            return False
        if node.data['id'] is id:
            return node.data
        else:
            if id < node.data['id']:
                return self.search(id, node.left)

            elif id > node.data['id']:
                return self.search(id, node.right)
            else:
                return False

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)


if __name__ == "__main__":
    bst = BST()
    d = {
        "body": "Hello world",
        "id": 6,
        "title": "Century share visit phone should could.",
        "user_id": 42
    }
    d1 = {
        "body": "Hello moon",
        "id": 2,
        "title": " visit phone should could.",
        "user_id": 2
    }
    bst.insert(d)
    bst.insert(d1)
    print(bst.search_blog(2))
