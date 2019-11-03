# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Iterative
        # Initialize head node, splicing node by using temp
        head = ListNode(0)
        temp = head

        # Splicing Node until there is no l1.next or l2.next
        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = l1
                temp = temp.next
                l1 = l1.next

        # when there is no Node in l2, add the rest of l1 Node
        if l1:
            temp.next = l1

        # when there is no Node in l1, add the rest of l2 Node
        if l2:
            temp.next = l2

        return head.next

        # recursive
        def mergeTwoLists1(self, l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists1(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists1(l1, l2.next)
                return l2