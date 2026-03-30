# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def insert(head, insertNode):
            temp = ListNode(0)
            temp.next = head

            tempHead = temp

            cnt = 0

            while head and head.val <= insertNode.val:
                cnt += 1
                head = head.next
            
            for i in range(cnt):
                temp = temp.next
            
            curr = temp.next
            insertNode.next = curr
            temp.next = insertNode

            return tempHead.next
        

        tempHead = head

        sorted = head
        head = head.next
        sorted.next = None

        while head:
            insertNode = head
            next = head.next
            insertNode.next = None
            head = next

            sorted = insert(sorted, insertNode)
        
        return sorted

