# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        
        fast = head
        mid_prev = None
        mid = head
        while fast and fast.next:
            fast = fast.next.next
            mid_prev = mid
            mid = mid.next
        mid_prev.next = None

        # reverse list staring from mid, since list len > 1, mid is not None
        prev = None
        curr = mid

        while curr:
            nxt = curr.next     # save the remaining list
            curr.next = prev    # reverse this link
            prev = curr
            curr = nxt

        l2 = prev
        
        
        # consecutively concatenate
        l1 = head
        first = False
        
        while l1 and l2:
            if first:
                temp = l2.next
                l2.next = l1
                l2 = temp
                first = False
            else:
                temp = l1.next
                l1.next = l2
                l1 = temp
                first = True
        
