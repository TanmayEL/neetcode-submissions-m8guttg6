# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #go to half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse other half
        temp = None
        while slow:
            next = slow.next
            slow.next = temp
            temp = slow
            slow = next

        #join together
        left, right = head, temp
        while left and right:
            tempLeft, tempRight = left.next, right.next
            left.next, right.next = right, tempLeft
            left, right = tempLeft, tempRight

        # 1 -> 2 -> 3    4 <- 5 <- 6
