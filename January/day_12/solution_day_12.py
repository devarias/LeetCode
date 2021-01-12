# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ""
        while l1:
            num1 += "".join(str(l1.val))
            l1 = l1.next
        while l2:
            num2 += "".join(str(l2.val))
            l2 = l2.next
        total = str(int(num1[::-1]) + int(num2[::-1]))
        head = ListNode(total[-1])
        new = head
        for i in range(len(total) - 2, -1, -1):
            node = ListNode(total[i])
            new.next = node
            new = node
        return head
