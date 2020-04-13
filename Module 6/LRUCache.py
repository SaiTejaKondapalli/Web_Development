from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    def get(self, key):
        if key in self.cache_dict:
            self.cache_dict.move_to_end(key)
            return self.cache_dict[key]
        else:
            return -1

    def put(self,key,value):
        if self.get(key) == -1:
            if len(self.cache_dict) >= self.capacity:
                self.cache_dict.popitem(last=False)
        self.cache_dict[key] = value

    def get_cache(self):
        return self.cache_dict