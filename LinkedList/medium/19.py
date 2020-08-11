# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        cnt = 0  # length
        while head:
            cnt += 1
            head = head.next
        head = first
        ind = cnt - n  # elem index to be removed:
        if ind == 0:
            return head.next
        while ind > 1:
            ind -= 1
            head = head.next
        head.next = head.next.next
        return first

