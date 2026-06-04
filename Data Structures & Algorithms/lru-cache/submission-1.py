class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0) # right most recent
        self.cap = capacity
        self.cache = {} # map key to nodes
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node): # insert at right
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right

    def remove(self, node): # rmv node from list
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
        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
