import logging
import sys
from lru_cache import LRUCache


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s\t%(levelname)s\t%(message)s",
        filename="lru_cache.log",
    )
    lru = logging.getLogger("lru_cache")

    if len(sys.argv) > 1 and "-s" in sys.argv:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s -"
            " %(message)s"
        )
        handler.setFormatter(formatter)
        lru.addHandler(handler)

    cache = LRUCache(2)

    cache["key1"] = "value1"
    cache["key2"] = "value2"
    cache["key3"] = "value3"
