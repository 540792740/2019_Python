# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_list = []
        #   1. Save into a list
        for head in lists:
            while head:
                res_list.append(head.val)
                head = head.next

        #   2. Sort
        res_list.sort()

        #   3. Save into ListNode
        dummy = ListNode(0)
        temp = dummy

        for val in res_list:
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next

