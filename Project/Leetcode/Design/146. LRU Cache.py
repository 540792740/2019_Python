import collections
    # Just dic

class LRUCache(object):
    def __init__(self, capacity):
        self.d = collections.OrderedDict()
        self.c = capacity

    def get(self, key):
        ret = -1
        if key in self.d:
            ret, self.d[key] = self.d[key], self.d.pop(key)
        return ret

    def put(self, key, value):
        if key in self.d:
            del self.d[key]
        self.d[key] = value
        if len(self.d) > self.c:
            self.d.popitem(last=False)


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