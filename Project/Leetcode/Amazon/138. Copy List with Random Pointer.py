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
        """
        :type head: Node
        :rtype: Node
        """
        return copy.deepcopy(head)

    def copyRandomList1(self, head: 'Node') -> 'Node':
        # when head is None
        if not head: return None

        # Hashtable, save all node into hashtable
        mapping = {}
        temp = head
        while temp:
            mapping[temp] = Node(temp.val, None, None)
            temp = temp.next

        temp = head
        while temp:

            # Adjust pointer 'next'
            if temp.next:
                mapping[temp].next = mapping[temp.next]

            # Adjust pointer 'random'
            if temp.random:
                mapping[temp].random = mapping[temp.random]

            # Move to next Node
            temp = temp.next

        return mapping[head]

