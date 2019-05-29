# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = ListNode(0)
        r = root
        while l1 != None or l2 != None:
            if l1:
                carry += l1.val
            if l2:
                carry += l2.val

            root.next = ListNode(carry % 10)
            carry //= 10
            root = root.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry == 1:
            root.next = ListNode(1)
        return r.next