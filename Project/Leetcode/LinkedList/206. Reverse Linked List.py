# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):

        # Save into a arr-list, refactor Linked list, O(n)

        # Directly:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    # Recursive
    def reverseList1(self, head, prev = None):
        if not head: return prev
        temp = head.next
        head.next = prev
        return self.reverseList1(temp, head)