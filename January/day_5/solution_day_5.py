# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new = ListNode(1)
        new.next = head
        tmp = new
        while tmp.next is not None and tmp.next.next is not None:
            if tmp.next.val == tmp.next.next.val:
                n = tmp.next.val
                while tmp.next is not None and tmp.next.val == n:
                    tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return new.next
