'''
Iterative solution and Recursive solution
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative solution
# Core: head.next = prev_node
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node