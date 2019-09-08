class SingleLinkedListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __repr__(self):
        nval = self.next and self.next.val or None
        return f"[{self.val}:{repr(nval)}]"

class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None
    def push(self, obj):
        node = SingleLinkedListNode(obj,None)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node