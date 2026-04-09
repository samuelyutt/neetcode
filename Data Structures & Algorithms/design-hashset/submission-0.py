class MyHashSet:

    def __init__(self):
        self.cap = 10000
        self.arr = [None] * self.cap

    def add(self, key: int) -> None:
        k = key % self.cap
        new_node = Node(key)
        prev, node = None, self.arr[k]
        if node is None:
            self.arr[k] = new_node
        else:
            while node is not None and node.val <= key:
                if node.val == key:
                    return
                prev, node = node, node.next
            if prev:
                prev.next = new_node
            if node:
                node.prev = new_node
            new_node.prev = prev
            new_node.next = node

    def remove(self, key: int) -> None:
        k = key % self.cap
        node = self.arr[k]
        while node is not None and node.val <= key:
            if node.val == key:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.arr[k] = node.next
                if node.next:
                    node.next.prev = node.prev
                return

    def contains(self, key: int) -> bool:
        k = key % self.cap
        node = self.arr[k]
        while node is not None and node.val <= key:
            if node.val == key:
                return True
            node = node.next
        return False

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)