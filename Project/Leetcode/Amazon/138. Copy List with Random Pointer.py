"""
Using Hashtable
"""
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]


    def copyRandomList1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return copy.deepcopy(head)

