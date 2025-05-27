class ListNode:

    def __init__(self, key: int, val: int, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # maps key -> ListNode(val)
        self.capacity = capacity
        self.head = self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addBeforeTail(self, node):
        prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev
        prev.next = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.addBeforeTail(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.addBeforeTail(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
