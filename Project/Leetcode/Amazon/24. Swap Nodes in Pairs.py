# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # O(n) pointer change
        dummy = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            temp_a = cur.next
            temp_b = cur.next.next
            cur.next = temp_b
            temp_a.next = cur.next.next
            temp_b.next = temp_a
            cur = cur.next.next
        return dummy.next