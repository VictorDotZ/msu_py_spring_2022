class LRUCache(dict):
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.cache = {}
        super().__init__()

    def __setitem__(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                low_priority_key = min(self.cache, key=self.cache.get)
                self.pop(low_priority_key)
                self.cache.pop(low_priority_key)

            for k in self.cache:
                self.cache[k] += 1
            self.cache[key] = 1
        else:
            self.cache[key] += 1

        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key not in self.cache:
            return None

        self.cache[key] += 1
        return super().__getitem__(key)
