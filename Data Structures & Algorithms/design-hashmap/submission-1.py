class MyHashMap:

    def __init__(self):
        self.cap = 10000
        self.arr = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        k = key % self.cap
        prev, node = None, self.arr[k]
        if node is None:
            self.arr[k] = Node(key, value)
        else:
            while node and node.key <= key:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            new_node = Node(key, value)
            if prev:
                prev.next = new_node
            else:
                self.arr[k] = new_node
            if node:
                node.prev = new_node
            new_node.prev = prev
            new_node.next = next

    def get(self, key: int) -> int:
        k = key % self.cap
        node = self.arr[k]
        while node and node.key <= key:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        k = key % self.cap
        node = self.arr[k]
        while node and node.key <= key:
            if node.key == key:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.arr[k] = node.next
                if node.next:
                    node.next.prev = node.prev
                return

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)