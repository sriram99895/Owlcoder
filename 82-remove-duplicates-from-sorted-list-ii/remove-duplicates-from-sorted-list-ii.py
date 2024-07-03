# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            data  = curr.val
            f = 0
            while curr.next and data == curr.next.val:
                curr = curr.next
                f= 1
            if f == 0:
                prev = curr
            else:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            curr = curr.next        
        return head                        
        