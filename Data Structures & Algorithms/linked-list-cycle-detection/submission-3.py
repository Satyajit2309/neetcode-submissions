# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s , f = head , head 
        
        while f.next and f.next.next:
            s = s.next
            f = f.next.next

            if s.val == f.val:
                return True
        
        if not f.next or not f.next.next:
            return False
        


        