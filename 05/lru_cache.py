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
        self.__maximize_priority(key)

        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key not in self.cache:
            return None

        self.__maximize_priority(key)
        return super().__getitem__(key)

    def __maximize_priority(self, key):
        self.cache[key] = (
            self.cache[max(self.cache, key=self.cache.get)] + 1
            if self.cache
            else 0
        )
