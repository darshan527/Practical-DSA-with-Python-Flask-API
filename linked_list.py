class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            tmp = Node(data)
            tmp.next = self.head
            self.head = tmp

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            tmp = Node(data)
            self.tail.next = tmp
            self.tail = tmp

    def print_LL(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print(None)

    def to_array(self) -> list:
        n = self.head
        l = []
        while n:
            l.append(n.data)
            n = n.next
        return l


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beginning(1)
    ll.insert_beginning(2)
    ll.insert_beginning(3)
    # ll.print_LL()
    ll.insert_end(4)
    ll.insert_end(5)
    # ll.print_LL()
    lst = ll.to_array()
    print(lst)