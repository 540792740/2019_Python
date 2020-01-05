'''
Faster and slower pointer

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head: return True
        fast = slow = head

        #  Find Middle node, slower pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse Second part
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first and second half:
        # When even Node: first and second half is the same
        # When odd Node: first one node less than second half
        while prev and head:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
        return True


