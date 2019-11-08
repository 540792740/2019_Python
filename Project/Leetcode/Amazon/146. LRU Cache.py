    # Just dic

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.last_cache_lookup = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print(self.last_cache_lookup)
        if key not in self.cache:
            return -1
        self.last_cache_lookup.remove(key)
        self.last_cache_lookup.append(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print(self.last_cache_lookup)
        if key in self.cache:
            self.cache[key] = value
            self.last_cache_lookup.remove(key)
            self.last_cache_lookup.append(key)
            return
        else:
            if len(self.cache) == self.capacity:
                del_key = self.last_cache_lookup[0]
                self.last_cache_lookup = self.last_cache_lookup[1:]
                del self.cache[del_key]
            self.last_cache_lookup.append(key)
            self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    S = LRUCache(2)
    S.put(1,1)
    S.put(2,2)
    S.get(1)
    S.put(3,3)
    S.get(2)
    S.put(4,4)
    S.get(1)
    S.get(3)
    S.put(5, 4)