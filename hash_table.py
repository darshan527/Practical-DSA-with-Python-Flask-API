class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size: int):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key: str):
        hashed_key = 0
        for i in key:
            hashed_key += ord(i)
            hashed_key = (hashed_key * ord(i)) % self.table_size
        return hashed_key

    def add_data(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value))
        else:
            nod = self.hash_table[hashed_key]
            while nod.next:
                nod = nod.next
            nod.next = Node(Data(key, value))

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        val = self.hash_table[hashed_key]
        if val is not None:
            if val.next is None:
                return val.data.value
            else:
                while val:
                    if val.data.key is key:
                        return val.data.value
                    val = val.next
        return None

    def print_table(self):
        print("{")
        for i in self.hash_table:
            if i is None:
                print(None)
            else:
                tmp = i
                while tmp:
                    print(f"[{tmp.data.key} : {tmp.data.value}]", end=" -> ")
                    tmp = tmp.next
                print("None")
        print("}")


if __name__ == "__main__":
    ht = HashTable(4)
    ht.add_data("title", "Jack and Jill")
    ht.add_data("body", "Hello World, learn Programming")
    ht.add_data("date", "22-3-15")
    ht.add_data("user_id", 2)
    # print(ht.get_value("title"))
    print(ht.get_value('title'))
    print(ht.get_value('body'))
    print(ht.get_value('date'))
    print(ht.get_value('user_id'))
    ht.print_table()