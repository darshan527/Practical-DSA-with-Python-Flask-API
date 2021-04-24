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

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] is int(user_id):
                return node.data, 200
            node = node.next
        return {"Message": "No User Found with the given user_id"}, 404


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_beginning(1)
    # ll.insert_beginning(2)
    # ll.insert_beginning(3)
    # # ll.print_LL()
    # ll.insert_end(4)
    # ll.insert_end(5)
    # # ll.print_LL()
    d = {
        "address": "785 Jessica Points Suite 670\nNew Mark, UT 56553",
        "email": "Tony_Turner@email.com",
        "id": 200,
        "name": "Tony Turner",
        "phone": "7142755042122"
    }
    ll.insert_beginning(d)
    lst = ll.to_array()
    # print(lst)
    print(ll.get_user_by_id(200))