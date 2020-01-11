# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle1(self, head: ListNode) -> bool:
        def reverse_head(head):
            pre = None
            while head and head.next:
                temp = head
                head = head.next
                temp.next = pre
                pre = temp
            return head

        if head and head.next and head == reverse_head(head):
            return True
        else:
            return False
