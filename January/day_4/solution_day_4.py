# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = l1
            tmp = l2
        else:
            head = l2
            tmp = l1
        tmp_head = head
        while tmp_head and tmp:
            if tmp_head.next and tmp_head.next.val < tmp.val:
                tmp_head = tmp_head.next
            elif tmp_head is None:
                break
            else:
                new = ListNode(tmp.val)
                new.next = tmp_head.next
                tmp_head.next = new
                tmp = tmp.next
        if tmp:
            tmp_head.next = tmp
        return head
