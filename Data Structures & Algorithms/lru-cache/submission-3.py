class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: ptr to node
        self.left, self.right = Node(0,0), Node(0,0) # right most recent
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node): # insert to right
        prev = self.right.prev
        self.right.prev = prev.next = node
        node.next = self.right
        node.prev = prev

    def remove(self, node): # anywhere
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:   return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
      
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
