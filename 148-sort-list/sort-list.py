# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        temp=head
        l.sort() 
        i = 0  
        # print(l) 
        while temp:
            temp.val = l[i]
            # print(temp.val)
            temp = temp.next
            i+=1  
        return head     
        