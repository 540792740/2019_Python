import collections
# Dict + Double LinkedList
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._addend(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self.dic[key] = n
        self._addend(n)

        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _addend(self, node):
        p = self.tail.prev

        # Connect p, node
        p.next = node
        node.prev = p

        # Connect node and tail
        self.tail.prev = node
        node.next = self.tail

# OrderDict
class LRUCache1(object):
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