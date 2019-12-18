# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        dummy_head = ListNode(-1)
        dummy_head.next = head
        temp = dummy_head
        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy_head.next