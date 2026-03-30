# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get to halfpoint
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the right part
        right = slow.next
        slow.next = None
        temp = None

        while right:
            nxt = right.next
            right.next = temp
            temp = right
            right = nxt
        
        first, second = head, temp
        #Combine
        while second:
            tempLeft = first.next
            tempRight = second.next
            first.next, second.next = second, tempLeft
            first, second = tempLeft, tempRight