class LRUCache:

    def __init__(self, capacity: int):
        self.d = {} # key -> node
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.n_nodes = 0

    def get(self, key: int) -> int:
        print('get', key, self.d)
        node = self.pop(key)
        if node:
            self.append(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.pop(key)
        if node:
            node.value = value
        else:
            node = Node(key, value)
        self.append(node)

        if self.n_nodes > self.capacity:
            self.pop(self.head.key)

        print('put', key, self.head.key, self.d)

    def pop(self, key):
        if key in self.d:
            node = self.d[key]

            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next

            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev

            node.prev = None
            node.next = None
            self.n_nodes -= 1
            del self.d[key]

            return node
        return None

    def append(self, node):
        node.prev = self.tail
        if node.prev:
            node.prev.next = node
        node.next = None
        self.tail = node
        if not self.head:
            self.head = node
        self.n_nodes += 1
        self.d[node.key] = node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
