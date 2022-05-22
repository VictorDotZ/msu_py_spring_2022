import logging


class LRUCache(dict):
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.cache = {}
        super().__init__()

        self.logger = logging.getLogger("lru_cache")
        self.logger.debug("cache object created")

    def __setitem__(self, key, value):
        self.logger.info("value: %s has been assigned to key: %s", key, value)

        if key not in self.cache:
            if len(self.cache) == self.capacity:
                low_priority_key = min(self.cache, key=self.cache.get)
                self.logger.info(
                    "item %s:%s has been removed from cache",
                    low_priority_key,
                    super().__getitem__(low_priority_key),
                )

                self.pop(low_priority_key)
                self.cache.pop(low_priority_key)
        else:
            self.logger.warning(
                "value: %s has been reassigned by value %s",
                super().__getitem__(key),
                value,
            )

        self.__maximize_priority(key)

        super().__setitem__(key, value)

    def __getitem__(self, key):
        self.logger.info("key: %s has been requested", key)
        if key not in self.cache:
            self.logger.warning("key: %s does not exist in cache", key)

            return None

        self.__maximize_priority(key)
        return super().__getitem__(key)

    def __maximize_priority(self, key):
        self.cache[key] = (
            self.cache[max(self.cache, key=self.cache.get)] + 1
            if self.cache
            else 0
        )

        self.logger.debug("key: %s priority is %s", key, self.cache[key])
