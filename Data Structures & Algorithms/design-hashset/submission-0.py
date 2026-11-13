class MyHashSet:

    def __init__(self):
        self.bit = 0

    def add(self, key: int) -> None:
        key = (1 << key)
        if not self.bit & key:
            self.bit |= key

    def remove(self, key: int) -> None:
        key = (1 << key)
        if self.bit & key:
            self.bit &= ~key

    def contains(self, key: int) -> bool:
        return bool(self.bit & (1 << key))


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)