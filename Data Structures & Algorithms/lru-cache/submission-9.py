class Node:
    def __init__(self, key, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    """
    self.lru.next --> current LRU
    self.lru.prev --> current MRU
    """
    def __init__(self, capacity: int):
        self.k = capacity
        self.lru = Node(-1)
        self.lru.next = self.lru.prev = self.lru
        self.hashmap = dict()

    def get(self, key: int) -> int:
        if not self.hashmap.get(key):
            return -1
        g = self.hashmap[key]
        g.next.prev, g.prev.next = g.prev, g.next
        g.next, g.prev = self.lru, self.lru.prev
        g.prev.next = g.next.prev = g
        return g.val

    def put(self, key: int, value: int) -> None:
        if self.k and not self.hashmap.get(key):
            self.k -= 1
        else:
            rm = self.hashmap.get(key, self.lru.next)
            rm.prev.next, rm.next.prev = rm.next, rm.prev
            rm.prev = rm.next = None
            del self.hashmap[rm.key]
            del rm
        newN = Node(key, value, self.lru.prev, self.lru)
        self.lru.prev.next = self.lru.prev = newN
        self.hashmap[key] = newN
