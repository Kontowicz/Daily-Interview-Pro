class LRUCache:
    def __init__(self, space):
        self.size = 0
        self.queue = [None] * space
        self.dict = {}
        self.val_to_key = {}

    def get(self, key):
        if key not in self.dict:
            return None
        else:
            self.dict[self.queue[0]] = self.dict[key]
            self.queue[0], self.queue[self.dict[key]] = self.queue[self.dict[key]], self.queue[0]
            self.dict[key] = 0
            return self.queue[0]

    def put(self, key, value):

        if key not in self.dict:
            self.val_to_key[value] = key
            if self.queue[self.size] != None:
                del self.dict[self.val_to_key[self.queue[self.size]]]

            self.dict[key] = self.size
            self.queue[self.size] = value

            if self.size < len(self.queue) - 1:
                self.size += 1

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3
