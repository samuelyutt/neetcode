class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1
        self.next = None
        self.prev = None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.cnts = {} # cnt -> [head node, tail node]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.detatch_node(key)
        node.cnt += 1
        self.add_node(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.detatch_node(key)
            node.value = value
            node.cnt += 1
        else:
            node = Node(key, value)

            if len(self.cache) >= self.capacity:
                # remove LFU
                lfu_cnt = min(self.cnts.keys())
                lfu = self.cnts[lfu_cnt][0]
                self.detatch_node(lfu.key)
        
        self.add_node(node)

    def detatch_node(self, key):
        node = self.cache[key]
        head, tail = self.cnts[node.cnt]

        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev

        if node == head:
            self.cnts[node.cnt][0] = node.next

        if node == tail:
            self.cnts[node.cnt][1] = node.prev

        node.prev, node.next = None, None

        if self.cnts[node.cnt][0] == None:
            del self.cnts[node.cnt]

        del self.cache[key]

        return node

    def add_node(self, node):
        if node.cnt not in self.cnts:
            self.cnts[node.cnt] = [node, node]
        else:
            _, tail = self.cnts[node.cnt]
            node.prev = tail
            self.cnts[node.cnt][1].next = node
            self.cnts[node.cnt][1] = node

        self.cache[node.key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)