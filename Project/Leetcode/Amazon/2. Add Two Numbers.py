'''
Questionk:
1.  input is an lined list, right?
2.  What kind of variable in class Node? node.val and node.next right?
3.

Solution:
1.  There should contains 3 steps:
    a) Firstly, while l1 and l2
    b) Secondly: when run out of one linked list: While l1 or while l2
    c) Thirdly: When run out of all l1 and l2, make sure if still has carry
                value, add a linkedList at the end.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(None)
        temp = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry % 10)
            temp = temp.next
            carry //= 10
        return head.next


    def addTwoNumbers(self, l1, l2):
        head = ListNode(None)
        temp = head
        carry = 0
        def add_rule(add_l, carry, temp):
            if add_l > 9:
                carry = 1
                add_l %= 10
            else: carry = 0
            temp.next = ListNode(add_l)
            temp = temp.next
            return temp, carry

        while l1 and l2:
            add_l = l1.val + l2.val + carry
            temp, carry = add_rule(add_l, carry, temp)
            l1 = l1.next
            l2 = l2.next

        while l1:
            if carry == 0:
                temp.next = l1
                break
            else:
                add_l = l1.val + carry
                temp, carry = add_rule(add_l, carry, temp)
                l1 = l1.next

        while l2:
            if carry == 0:
                temp.next = l2
                break
            else:
                add_l = l2.val + carry
                temp, carry = add_rule(add_l, carry, temp)
                l2 = l2.next
        if not l1 and not l2 and carry: temp.next = ListNode(1)
        return head.next